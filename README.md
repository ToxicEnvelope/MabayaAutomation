# MabayaAutomation
Simple Automation Exam Solution

---

## Overview
```
In order to run the tests in this repository, 
you'll need to ensure that you're local environmemt 
is set correctly.

** We use Python3.9.X as base version **
 
follow the desciption below on how to set your environment.
```
---
## Install Python
```
In order to install Python3.9.X
You should navigate to 'https://python.org/downloads'
and download the latest version.
```
---
## Environment & Dependencies
```
You need to create a Virtual Environment for which 
the source code will need to be run in.
To create a new virtual environmnet , use the following command:

python3 -m venv /path/to/project/root/folder

-------------------------------------------------------------------------------- 

I've set all the dependencies in one file
which is located at the ROOT of the project.

The filename is 'requirements.txt' ; 
In order to install all dependencies you should use the following command:

pip install -r requirements.txt
```
---
## Executing Tests - UI and Integration 
```
Once you've installed Python3.9.x , 
created a virtual environment and installed all dependencies 
it is time to run the automated tests ; 

make sure you're located in the project root folder, 
then run the following command:


pytest ./tests/                     <- to run all tests
pytest ./tests/test_my_module.py    <- to run a specific test module
```
---
## Executing Tests - Loads
```
Once you've installed Python3.9.x , 
created a virtual environment and installed all dependencies 
it is time to run the automated tests ;

make sure you're located in the project root folder, 
then run the following command:

locust --locustfile tests/test_loads.py --host https://17eac024-8de4-4e85-982e-4f95d52cedd2.mock.pstmn.io --spawn-rate 1 --users 100000 --run-time 5m --show-task-ratio --html --headless     <- to run our load tests
```
