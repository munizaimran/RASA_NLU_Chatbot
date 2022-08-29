HOW TO RUN THE CHATBOT

open anaconda cmd as admin
open the project directory in anaconda cmd (C:\Users\Muniza\FYP\Weatherbot_Tutorial-master\Full Code-NEW>)
make a virtual environment with python version 3.6.12
conda activate new6
run the following commands in sequence:
pip install -r requirements1.txt
python -m spacy.en.download all
python nlu_model.py
npm i -g rasa-nlu-trainer
python train_init.py
python train_online.py
python run_bot.py

***creating a Flask API***

pip install rasa==0.1.1
pip install flask
rasa run -m models --enable-api
flask run
#new cmd:
python run_bot.py


****to run the bot****

running 'python run_bot.py' after all the above steps will make it run directly 
OR
apphh.py is the flask api file that also calls the chatbot on cmd when you run 'python apphh.py' after all the above steps


**** DEPLOYING ON HEROKU****
npm install -g heroku
heroku --version
heroku login
activate virtual env new6 ( so that chatbot api can work as per its requirements)
follow all the steps on the blog: https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb:

python wsgi.py
git init
heroku git:remote -a talktohelp
git add .
git commit -am "sample text"
git push heroku master

***
$ heroku login
$ heroku git:clone -a talktohelp 
$ cd talktohelp
$ git add .
$ git commit -am "make it better"
$ git push heroku master


main api is in the main.py file in app folder


ERRORS BEING FACED AT THE MOMENT:

-  python version not compatible when pushing the pplication
-  had to work with python version 3.6.12 for the chatbot but this is throwing an error when working with heroku
-  hence unable to push and thus deploy the bot on heroku

THE WAY FORWARD:

connect the chatbot to flutter app
ui for chatbot is ready
connect heroku to github where project is uploaded



***

<html>
  <head>
    <title>CHATBOT</title>
  </head>
  <body>
    <h1>CHATBOT</h1>
    <form>
      <label for="text">You:</label><br>
      <input type="text" id="text" name="text"><br>
      {{val}}
    </form>
  </body>
</html> 
