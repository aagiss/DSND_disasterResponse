"""
ETL of messages and categories CSV to sqlite3 db.
"""
import sys
import re
import pandas as pd
from sqlalchemy import create_engine

def extract(messages_csv, categories_csv):
    """
    extract data from messages and categories csv files.
    """
    messages = pd.read_csv(messages_csv)
    categories = pd.read_csv(categories_csv)
    return messages.merge(categories, left_on='id', right_on='id')

def transform(df):
    """
    transform column categories and remove duplicates.
    """
    column_names = set()
    for catval in df.categories[0].split(';'):
        g = re.match('^(.*)-(0|1|2)$', catval)
        assert g, catval
        column_names.add(g.group(1))
    columns = []
    for column_name in column_names:
        column = df.categories.apply(lambda x, column_name=column_name:
                                     int(re.match(r'(^|.*;)%s-(\d+)(;.*|$)' %
                                                  column_name, x).group(2)))
        df[column_name] = column
    df.drop(["categories"], axis=1, inplace=True)
    columns = ['message', 'genre'] + list(column_names)
    df.drop_duplicates(subset=columns, inplace=True)
    return df

def load(df, output_db, output_table):
    """
    load dataframe to sqlite database.
    """
    engine = create_engine('sqlite:///%s' % output_db)
    df.to_sql(output_table, engine, index=False, if_exists='replace')

def main(messages_csv, categories_csv, output_db, output_table):
    """
    the whole ETL pipeline from messages and categories csv
    to an sqlite database.
    """
    df = extract(messages_csv, categories_csv)
    df = transform(df)
    load(df, output_db, output_table)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python %s MESSAGES_CSV CATEGORIES_CSV OUTPUT.db' % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], 'messages')
