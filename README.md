### Table of Contents

 

1. [Installation](https://github.com/aagiss/DSND_disasterResponse#installation)
2. [Project Motivation](https://github.com/aagiss/DSND_disasterResponse#motivation)
3. [File Descriptions](https://github.com/aagiss/DSND_disasterResponse#files)
4. [Results](https://github.com/aagiss/DSND_disasterResponse#results)
5. [Running the code](https://github.com/aagiss/DSND_disasterResponse#running)
6. [Licensing, Authors, and Acknowledgements](https://github.com/aagiss/DSND_disasterResponse#licensing)

 

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


## Results <a name="results"></a>

<pre>
missing_people-1: precision: 100.00%, recall: 2.78%, f1: 5.41%
tools precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
cold-1: precision: 96.67%, recall: 18.12%, f1: 30.53%
security precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
fire-1: precision: 75.00%, recall: 4.84%, f1: 9.09%
aid_related-1: precision: 78.37%, recall: 66.92%, f1: 72.19%
shops precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
military-1: precision: 75.68%, recall: 11.62%, f1: 20.14%
buildings-1: precision: 74.34%, recall: 25.77%, f1: 38.27%
other_infrastructure precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
medical_products-1: precision: 74.29%, recall: 23.21%, f1: 35.37%
hospitals precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
storm-1: precision: 72.48%, recall: 64.86%, f1: 68.46%
electricity-1: precision: 75.00%, recall: 7.63%, f1: 13.85%
request-1: precision: 83.18%, recall: 55.86%, f1: 66.84%
water-1: precision: 78.40%, recall: 60.92%, f1: 68.56%
money-1: precision: 63.64%, recall: 5.11%, f1: 9.46%
aid_centers precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
clothing-1: precision: 74.00%, recall: 37.37%, f1: 49.66%
other_aid-1: precision: 80.00%, recall: 0.45%, f1: 0.90%
food-1: precision: 82.10%, recall: 73.80%, f1: 77.73%
death-1: precision: 71.52%, recall: 39.10%, f1: 50.56%
earthquake-1: precision: 91.27%, recall: 80.17%, f1: 85.36%
weather_related-1: precision: 84.80%, recall: 69.71%, f1: 76.52%
related-1: precision: 83.75%, recall: 95.41%, f1: 89.20%
related-2: precision: 50.00%, recall: 1.96%, f1: 3.77%
search_and_rescue-1: precision: 82.61%, recall: 10.44%, f1: 18.54%
floods-1: precision: 90.41%, recall: 51.56%, f1: 65.67%
shelter-1: precision: 82.97%, recall: 51.89%, f1: 63.85%
infrastructure_related precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
transport-1: precision: 84.44%, recall: 12.93%, f1: 22.42%
refugees-1: precision: 64.71%, recall: 14.67%, f1: 23.91%
medical_help-1: precision: 72.09%, recall: 17.22%, f1: 27.80%
other_weather-1: precision: 66.67%, recall: 3.58%, f1: 6.80%
direct_report-1: precision: 75.40%, recall: 44.30%, f1: 55.81%
offer precision: N/A recall: N/A f1: N/A ALL PREDICTIONS ARE 0
child_alone precision: N/A recall: N/A f1: N/A ALL TRAINING SAMPLES BELONG TO SINGLE CLASS
</pre>

## Running the code <a name="running"></a>

* ETL: <pre>cd data; python process_data.py messages.csv categories.csv messages.db</pre>
* Training: <pre>cd models; python train_classifier.py messages.db classifier.pkl</pre>
* Web App: <pre>cd app; python run.py</pre> (open browser at http://localhost:3001)

## Licensing, Authors, Acknowledgements <a name="licensing"></a>

 

Must give credit to Udacity and Figure8 for providing this data.  Otherwise, feel free to use the code here as you would like!
