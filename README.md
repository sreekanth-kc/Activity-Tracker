# README.md
    Simple application for track user activities.
 
 
 ####Requirements

   - [Python3](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
    
   - [virtual environment](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/)
    
   - [pip3](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)



 ####Install the dependencies
 
    Create a Python3 Virtual environment.
    
    pip install -r requirements.txt 
 
 ####Changes in settings.py
    -Create a database in MySQL and add that details in User_Activity_Tracker/local_settings.py 
 
 ####Run Migration
 
    
    python manage.py makemigrations user_activity

    python manage.py migrate
 
 ####Custom management command to populate the database with dummy data.
    
    python manage.py loadtable user_activity/fixtures/Users.json user_activity/fixtures/ActivityPeriod.json
 
 ####Run Server  
    
    python manage.py runserver
 
 
 ####API for get activity log.
 
    /api/getuseractivity
 
 ####To deploy the code in Google Cloud AppEngine:

    gcloud beta app deploy app.yaml --project <project_name>