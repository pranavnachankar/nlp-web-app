from flask import Flask, render_template, request, redirect
from db import Database
import api

app = Flask(__name__)
dbo = Database()


@app.route('/')
def index():
  return render_template('login.html')


@app.route('/register')
def register():
  return render_template('register.html')


@app.route("/perform_registration", methods=['post'])
def perform_registration():
  name = request.form.get('user_ka_name')
  email = request.form.get('user_ka_email')
  password = request.form.get('user_ka_password')

  response = dbo.insert(name, email, password)
  if response:  #response == 1
    return render_template('login.html',
                           message='Registration Successful, Kindly login')
  else:
    return render_template('register.html', message='Email already exists')


@app.route('/perform_login', methods=['post'])
def perform_login():
  email = request.form.get('user_ka_email')
  password = request.form.get('user_ka_password')

  response = dbo.search(email, password)

  if response:
    return redirect("/profile")
  else:
    # return "Incorrect email/password"
    return render_template('login.html', message='Incorrect email/password')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    # return "NER hoga yaga"
    return render_template('ner.html')
  

@app.route('/perform_ner', methods=['post'])
def perform_ner():
  text = request.form.get('ner_text')
  response = api.ner(text)
  print(response) #internal_ner_response
  return render_template("ner.html", ner_response=response)

app.run(host='0.0.0.0', port=81, debug=True)
