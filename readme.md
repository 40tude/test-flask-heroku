* ATTENTION heroku do not allow "_" in project name
    * Use "-" instead
* conda create --name test-flask-heroku python=3.12 -y
* conda activate test-flask-heroku
* create directory test-flask-heroku
* code .
* create file mypy.ini
* create file test-flask-heroku.py
* conda install flask mypy -y
* Strike F5 in VScode
* Should be running locally
* From VSCode commit on github 
* 
* pip list --format=freeze > requirements.txt
    * At the end of requirements.txt add the line gunicorn==23.0.0
    * I have to do that because I run WIN11 and I can't install gunicorn
    * gunicorn is only used in "production" on heroku
* create file Procfile
* create runtime.txt
* From VSCode commit to github
* Terminal
    * heroku login
    * heroku create test-flask-heroku
    * git remote add heroku https://git.heroku.com/test-flask-heroku.git
    * git push heroku main
    * heroku open