"""
Train the pipeline to classify messages
"""
import sys
import re
import pickle
import json
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def tokenize(text):
    """
    lowercase and nltk word tokenizer, also remove stopwords
    and punctuation and finally lemmatize
    """
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    return [WordNetLemmatizer().lemmatize(w)
            for w in word_tokenize(text)
            if w not in stopwords.words("english")]

def build_model():
    """
    Create pipeline and gridsearch
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(SGDClassifier(tol=1e-3, max_iter=1000)))
    ])
    params = {
        'clf__estimator__alpha': [0.00001, 0.00002, 0.00005, 0.0001,
                                  0.0002, 0.0005, 0.0008, 0.001],
        'clf__estimator__penalty': ['none', 'l2'],
        'clf__estimator__average': [True, False],
        'clf__estimator__loss': ['hinge', 'squared_hinge', 'log', 'modified_huber'],
        'clf__estimator__class_weight': [None, 'balanced']
    }
    cv = GridSearchCV(pipeline, param_grid=params)
    return cv

def get_train_test(input_db, input_table):
    """
    Load messages from input_db and table and split train test
    """
    engine = create_engine('sqlite:///%s' % input_db)
    df = pd.read_sql_table(input_table, engine)
    X = df['message']
    y = df.drop(['id', 'message', 'original', 'genre'], axis=1)
    columns = y.columns
    fixed_columns = []
    normal_columns = []
    for col in columns:
        if y[col].unique().shape[0] > 1:
            normal_columns.append(col)
        else:
            fixed_columns.append(col)
    y.drop(fixed_columns, axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y.values)
    return X_train, X_test, y_train, y_test, normal_columns, fixed_columns

def print_results(classifier_pkl, X_test, y_test):
    """
    Print precision, recall and f1-measure for all classes
    """
    with open(classifier_pkl, 'rb') as g:
        clf = pickle.load(g)
    with open(classifier_pkl+'.columns', 'r') as g:
        columns = json.load(g)
    y_pred = clf.predict(X_test)
    for i, col in enumerate(columns['normal_columns'] + columns['fixed_columns']):
        if i < len(columns['normal_columns']):
            col_y_test = y_test[:, i]
            col_y_pred = y_pred[:, i]
            shown = False
            for label in np.unique(col_y_pred):
                if label == 0:
                    continue
                precision = precision_score(col_y_test, col_y_pred, labels=[label], average='micro')
                recall = recall_score(col_y_test, col_y_pred, labels=[label], average='micro')
                f1 = f1_score(col_y_test, col_y_pred, labels=[label], average='micro')
                print('%s-%d:' % (col, label), 'precision: %.2lf%%,' % (100.0 * precision),
                      'recall: %.2lf%%,' % (100.0 * recall),
                      'f1: %.2lf%%' % (100.0 * f1))
                shown = True
            if not shown:
                print(col, 'precision: N/A',
                      'recall: N/A',
                      'f1: N/A',
                      'ALL PREDICTIONS ARE 0')
        else:
            print(col, 'precision: N/A',
                  'recall: N/A',
                  'f1: N/A',
                  'ALL TRAINING SAMPLES BELONG TO SINGLE CLASS')


def main(input_db, input_table, output_pkl):
    """
    Load data from input_db and table, build pipeline,
    do gridsearch, store model and print result stats
    """
    cv = build_model()
    X_train, X_test, y_train, y_test, normal_columns, fixed_columns = \
            get_train_test(input_db, input_table)
    cv.fit(X_train, y_train)
    with open(output_pkl, 'wb') as g:
        g.write(pickle.dumps(cv.best_estimator_))
    with open(output_pkl+'.columns', 'w') as g:
        g.write(json.dumps({'normal_columns': normal_columns,
                            'fixed_columns': fixed_columns}))
    print_results(output_pkl, X_test, y_test)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python %s MESSAGES_DB OUTPUT_PIPELINE_PKL' % sys.argv[0])
        sys.exit(0)
    main(sys.argv[1], 'messages', sys.argv[2])
