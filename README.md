### Table of Contents

 

1. [Installation](https://github.com/aagiss/DSND_disasterResponse#installation)
2. [Project Motivation](https://github.com/aagiss/DSND_disasterResponse#motivation)
3. [File Descriptions](https://github.com/aagiss/DSND_disasterResponse#files)
4. [Imbalanced Classes](https://github.com/aagiss/DSND_disasterResponse#imbalanced)
5. [Results](https://github.com/aagiss/DSND_disasterResponse#results)
6. [Running the code](https://github.com/aagiss/DSND_disasterResponse#running)
7. [Licensing, Authors, and Acknowledgements](https://github.com/aagiss/DSND_disasterResponse#licensing)

 

## Installation <a name="installation"></a>

 

Beyond the Anaconda distribution of Python, the following must be installed:
<pre>
conda install -c anaconda sqlalchemy
conda install -c anaconda pandas
conda install -c anaconda scikit-learn
conda install -c anaconda nltk
conda install -c anaconda plotly
conda install -c anaconda flask
</pre>

Pip installing the same packages and running the code using Python versions 3.* should produce no issues.


## Project Motivation <a name="motivation"></a>

 

During a disaster a huge number of messages are generated on social media and other channels. These messages must be routed to the appropriate organization that can actually handle the message and take some action. Routing by humans can be slow as the number of messages is vast. Therefore machine learning is deployed. In this project we develop a solution based on data provided as part of the Udacity Data Science Nanodegree (Jul 2018 Cohort).  



## File Descriptions <a name="files"></a>

 
<pre>
- app # a Flask enabled web app showcasing results
  | - template
  | |- master.html  # main page of web app
  | |- go.html  # classification result page of web app
  |- run.py  # Flask file that runs app
- data # data used for this task and ETL code
  |- disaster_categories.csv  # data to process 
  |- disaster_messages.csv  # data to process
  |- process_data.py
  |- InsertDatabaseName.db   # database to save clean data to
- models # the Machine Learning Pipeline used
  |- train_classifier.py
  |- classifier.pkl  # saved model 
- README.md
</pre>


## Imbalanced Classes <a name="imbalanced"></a>

Due to the nature of the problem some classes have very few instances compared to the whole bulk of messages. In other words there are just too few instances of messages for some classes. To deal with this problem during GridSearch we are not optimizing parameters for accuracy but rather for F-measure for the non-zero classes. More specificially because the cost of loosing one message is much greater that the cost of having some spam we do use a beta of 0.5 to favour recall over precision.

We actually implemented a custom scorer with the following code:
<pre>
def my_scorer(y_test, y_pred):
    TP = np.logical_and(y_test == y_pred, y_pred != 0).sum()
    FP = np.logical_and(y_test != y_pred, y_pred != 0).sum()
    FN = np.logical_and(y_test != y_pred, y_test != 0).sum()
    precision = float(TP)/float(TP+FP) if TP+FP > 0 else 0
    recall = float(TP)/float(TP+FN) if TP+FN > 0 else 0
    b = 0.5
    return (b+1)*precision*recall/(b*precision+recall)
</pre>

## Results <a name="results"></a>

<pre>
missing_people-1: precision: 81.25%, recall: 18.57%, f1: 30.23%
tools precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
cold-1: precision: 72.00%, recall: 26.47%, f1: 38.71%
security precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
fire-1: precision: 81.82%, recall: 23.08%, f1: 36.00%
aid_related-1: precision: 74.66%, recall: 70.42%, f1: 72.48%
shops precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
military-1: precision: 64.71%, recall: 22.00%, f1: 32.84%
buildings-1: precision: 76.19%, recall: 31.46%, f1: 44.53%
other_infrastructure-1: precision: 50.00%, recall: 0.66%, f1: 1.31%
medical_products-1: precision: 70.48%, recall: 24.67%, f1: 36.54%
hospitals-1: precision: 0.00%, recall: 0.00%, f1: 0.00%
storm-1: precision: 75.43%, recall: 62.28%, f1: 68.23%
electricity-1: precision: 56.52%, recall: 18.18%, f1: 27.51%
request-1: precision: 78.78%, recall: 58.34%, f1: 67.04%
water-1: precision: 73.71%, recall: 66.50%, f1: 69.92%
money-1: precision: 68.57%, recall: 15.38%, f1: 25.13%
aid_centers precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
clothing-1: precision: 75.00%, recall: 48.39%, f1: 58.82%
other_aid-1: precision: 62.82%, recall: 11.37%, f1: 19.25%
food-1: precision: 82.44%, recall: 73.97%, f1: 77.97%
death-1: precision: 75.14%, recall: 45.48%, f1: 56.67%
earthquake-1: precision: 88.04%, recall: 80.24%, f1: 83.96%
weather_related-1: precision: 84.33%, recall: 72.78%, f1: 78.13%
related-1: precision: 85.09%, recall: 93.03%, f1: 88.88%
related-2: precision: 83.33%, recall: 18.18%, f1: 29.85%
search_and_rescue-1: precision: 64.52%, recall: 10.87%, f1: 18.60%
floods-1: precision: 91.44%, recall: 57.50%, f1: 70.60%
shelter-1: precision: 81.00%, recall: 52.21%, f1: 63.50%
infrastructure_related-1: precision: 50.00%, recall: 1.37%, f1: 2.67%
transport-1: precision: 73.75%, recall: 20.07%, f1: 31.55%
refugees-1: precision: 65.08%, recall: 20.40%, f1: 31.06%
medical_help-1: precision: 55.94%, recall: 22.29%, f1: 31.88%
other_weather-1: precision: 73.81%, recall: 8.66%, f1: 15.50%
direct_report-1: precision: 73.65%, recall: 48.09%, f1: 58.19%
offer precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
child_alone precision: N/A recall: N/A f1: N/A ALL TRAINING SAMPLES BELONG TO SINGLE CLASS
</pre>

## Running the code <a name="running"></a>

* ETL: <pre>cd data; python process_data.py messages.csv categories.csv messages.db</pre>
* Training: <pre>cd models; python train_classifier.py messages.db classifier.pkl</pre>
* Web App: <pre>cd app; python run.py</pre> (open browser at http://localhost:3001)

## Licensing, Authors, Acknowledgements <a name="licensing"></a>

 

Must give credit to Udacity and Figure8 for providing this data.  Otherwise, feel free to use the code here as you would like!
