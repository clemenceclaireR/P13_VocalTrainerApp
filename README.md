# P13_MinimalPairApp

## Presentation

##Installation

### Install on Debian 

#### MySQL Database
You have to run this command before installing 
__requirements.txt__ file, otherwise __mysqlclient__ library
installation will fail:

    sudo apt install default-libmysqlclient-dev


#### PostgreSQL Database

    apt install postgresql postgresql-client

#### Dependencies

    pip install -r requirements.txt
    
#### Get the database ready

Run the migrations and migrate command in order to build the tables :

    python manage.py makemigrations    
    python manage.py migrate    

Once your tables ready, insert the data with the script in tools/sql_scripts.
According to your database, the files contains the command to write in your 
terminal. For MySQL :
 
    mysql -u <user> -p < insert_data_mysql.sql 
    
Or, for PostgreSQL:
    
    psql -U <user> -h localhost -d vocal_trainer -f insert_data_postgres.sql
 You can also copy and paste their content in your application.