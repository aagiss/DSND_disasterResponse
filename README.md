### Table of Contents

 

1. [Installation](https://github.com/aagiss/stackoverflow#installation)
2. [Project Motivation](https://github.com/aagiss/stackoverflow#motivation)
3. [File Descriptions](https://github.com/aagiss/stackoverflow#files)
4. [Results](https://github.com/aagiss/stackoverflow#results)
5. [Licensing, Authors, and Acknowledgements](https://github.com/aagiss/stackoverflow#licensing)

 

## Installation 

 

Beyond the Anaconda distribution of Python, there is a dependency on NLTK (pip install nltk).  The code should run with no issues using Python versions 3.*.

 

## Project Motivation

 

During a disaster  a huge amount of messages are generated on social media and other channels. These messages must be routed to the appropriate organization that can actually handle the request. Human editing can be slow as the number of messages is vast. Therefore machine learning is deployed. In this project we develop a solution based on data provided as part of the Udacity Data Science Nanodegree (Jul 2018 Cohort).  



## File Descriptions 

 
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

## Results

 



 

## Licensing, Authors, Acknowledgements

 

Must give credit to Udacity and Figure8 for providing this data.  Otherwise, feel free to use the code here as you would like!
