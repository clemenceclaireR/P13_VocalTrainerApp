# P13_MinimalPairApp

## Presentation

### Compatibility

This application uses Mozilla Web Speech API for playing sounds directly from the word written.
Though its scope or compatibility is quite broad, you can experience some troubles with Opera or 
Firefox on Linux.
Its guaranteed to work on Chrome. 

##Installation

### Install on Debian 

#### PostgreSQL Database

    apt install postgresql postgresql-client

#### Dependencies

    pip install -r requirements.txt
    
#### Get the database ready

Run the migrations and migrate command in order to build the tables :

    python manage.py makemigrations    
    python manage.py migrate    


Then insert data:
    
    psql -U <user> -h localhost -d vocal_trainer -f insert_data_postgres.sql
 You can also copy and paste their content in your application.
 
 
### Tests
 
Tests are configured to run on chrome driver. Download the chrome driver
matching the version currently installed on your computer :
https://chromedriver.chromium.org/downloads

We provides the __run_tests.sh__ file which will executes tests for each app and will generate
the coverage report.

Note : We chose to run tests separately for each application. The reason is that a common
database setUp has been define in order to be used by all TestCas classes without having
to recreate instances everytime (or almost!). However, Selenium classes does not 
support it well. The first Selenium class test will use it, but the data persistence is lost
for all Selenium classes which run after.
Having one Selenium class by application, running it separately makes this problem obsolete.
Otherwise, one solution is to recreate the necessary instances in the Selenium class SetUp.
