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