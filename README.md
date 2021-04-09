# P13_MinimalPairApp

## Presentation

### Compatibility

This application uses Mozilla Web Speech API for playing sounds directly from the written word.
Though its scope or compatibility is quite broad, you can experience some troubles with Chromium or 
Firefox on Linux.
Its guaranteed however to work on Chrome. 

Here are the results of our own observations:

|             |  Windows 10   | Debian 10 |  MacOS | Android | iPhone |
|----------   |:-------------:|----------:|-------:|--------:|-------:|
| Chrome      |  OK           | OK        | OK     | OK      | OK     |
| Chromium    |  OK           | X         | N/A    | N/A     | N/A    |
| Firefox     |  OK           | Action required (see below) |  OK     | OK     | OK     |
| Edge        |  OK           |       OK  | OK     | OK      | OK     |
| Safari      |  ---          |       --- | OK     | ---     | OK     |
| Opera       |  OK           | X         | OK     | X       | OK     |
| Brave       |  OK           | X         | OK     | OK      | OK     |

#### Firefox on Linux troubleshooting

The following libraries have to be installed on your system
in order to provide voices that your browser will use :

    sudo apt install espeak
    sudo apt install espeak-ng
    sudo apt install speech-dispatcher

Unfortunately, it seems to have no effect on Chromium browser.

See also details compatibility information on Web Speech API official page : 
https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API#Browser_compatibility

## Installation

### Get the repository

Pull this repository.

### PostgreSQL Database

#### On Debian

    apt install postgresql postgresql-client

#### On Windows or MacOS

Get the installer on the official page.

#### Dependencies

    pip install -r requirements.txt

/!\ On MacOS, you might need to add Postgres on path :

    export PATH=$PATH:/Library/PostgreSQL/<version>/bin 
    
#### Get the database ready

Run the migrations and migrate command in order to build the tables :

    python manage.py makemigrations    
    python manage.py migrate    


Then insert data:
    
    psql -U <user> -h localhost -d vocal_trainer -f insert_data_postgres.sql

 
### Tests
 
Tests are configured to run on chrome driver. Download the chrome driver
matching the version currently installed on your computer :
https://chromedriver.chromium.org/downloads

We provides the __run_tests.sh__ file which will executes tests for each app and will generate
the coverage report (line breaks are in unix format).

Note : We chose to run tests separately for each application. The reason is that a common
database setUp has been define in order to be used by all TestCas classes without having
to recreate instances everytime (or almost!). However, Selenium classes does not 
support it well. The first Selenium class test will use it, but the data persistence is lost
for all Selenium classes which run after.
Having one Selenium class by application, running it separately makes this problem obsolete.
Otherwise, one solution is to recreate the necessary instances in the Selenium class SetUp.
