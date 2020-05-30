# README.md
    Simple application for track user activities.
 ####Install the dependencies
 
    Create a Python3 Virtual environment.
    
    pip install -r requirements.txt 
 ##
 
 
 Run Migration
 
    
    python manage.py makemigrations

    python manage.py migrate
 
 Run Server  
    
    python manage.py runserver
 
 Custom management command to populate the database with dummy data.
    
    python manage.py loadtable user_activity/fixtures/Users.json user_activity/fixtures/ActivityPeriod.json
 
 API for get activity log.
 
    /api/getuseractivity
 
 To deploy the code in Google Cloud AppEngine:

    gcloud beta app deploy app.yaml --project <project_name>