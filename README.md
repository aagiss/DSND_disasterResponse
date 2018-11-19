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
missing_people-1: precision: 63.64%, recall: 10.00%, f1: 17.28%
cold-1: precision: 85.71%, recall: 8.57%, f1: 15.58%
fire-1: precision: 66.67%, recall: 12.90%, f1: 21.62%
aid_related-1: precision: 77.68%, recall: 67.54%, f1: 72.26%
military-1: precision: 59.26%, recall: 7.17%, f1: 12.80%
buildings-1: precision: 84.15%, recall: 19.94%, f1: 32.24%
medical_products-1: precision: 90.91%, recall: 14.16%, f1: 24.51%
storm-1: precision: 75.17%, recall: 54.90%, f1: 63.46%
electricity-1: precision: 88.89%, recall: 14.55%, f1: 25.00%
request-1: precision: 85.13%, recall: 57.56%, f1: 68.68%
water-1: precision: 75.14%, recall: 61.16%, f1: 67.44%
money-1: precision: 85.71%, recall: 3.82%, f1: 7.32%
clothing-1: precision: 77.55%, recall: 35.19%, f1: 48.41%
other_aid-1: precision: 57.89%, recall: 1.28%, f1: 2.50%
food-1: precision: 82.25%, recall: 71.35%, f1: 76.42%
death-1: precision: 77.70%, recall: 37.95%, f1: 51.00%
earthquake-1: precision: 89.63%, recall: 78.70%, f1: 83.81%
weather_related-1: precision: 86.17%, recall: 68.20%, f1: 76.14%
related-1: precision: 83.07%, recall: 95.75%, f1: 88.96%
related-2: precision: 100.00%, recall: 6.25%, f1: 11.76%
search_and_rescue-1: precision: 75.00%, recall: 8.47%, f1: 15.23%
floods-1: precision: 91.24%, recall: 46.64%, f1: 61.73%
shelter-1: precision: 83.69%, recall: 48.09%, f1: 61.08%
transport-1: precision: 82.98%, recall: 13.04%, f1: 22.54%
refugees-1: precision: 80.00%, recall: 13.21%, f1: 22.67%
medical_help-1: precision: 66.39%, recall: 15.05%, f1: 24.53%
other_weather-1: precision: 100.00%, recall: 0.27%, f1: 0.54%
direct_report-1: precision: 81.77%, recall: 46.12%, f1: 58.98%
child_alone precision: N/A recall: N/A f1: N/A ALL TRAINING SAMPLES BELONG TO SINGLE CLASS

</pre>

## Running the code <a name="running"></a>

* ETL: cd data; python process_data.py messages.csv categories.csv output.db
* Training: cd models; python train_classifier.py output.db classifier.pkl
* Web App: cd app; python run.py (open browser at http://localhost:3001)

## Licensing, Authors, Acknowledgements <a name="licensing"></a>

 

Must give credit to Udacity and Figure8 for providing this data.  Otherwise, feel free to use the code here as you would like!
