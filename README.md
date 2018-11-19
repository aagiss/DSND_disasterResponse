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
</pre>

## Running the code <a name="running"></a>

* ETL: <pre>cd data; python process_data.py messages.csv categories.csv messages.db</pre>
* Training: <pre>cd models; python train_classifier.py messages.db classifier.pkl</pre>
* Web App: <pre>cd app; python run.py</pre> (open browser at http://localhost:3001)

## Licensing, Authors, Acknowledgements <a name="licensing"></a>

 

Must give credit to Udacity and Figure8 for providing this data.  Otherwise, feel free to use the code here as you would like!
