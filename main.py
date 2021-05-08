from flask import Flask,render_template,request,abort,send_file,Response
from werkzeug.utils import secure_filename
from flask_autoindex import AutoIndex
import os
import requests
import time 
import subprocess
from subprocess import check_output

app=Flask(__name__, template_folder='.')
SITE_NAME=""
ppath="/"
@app.route("/")
def main():
  if request.method == 'GET':
    out = os.popen('cat index.html').read()
    return (out)
@app.route('/whois',methods=['GET'])
def whois():
  param = request.args.get("q")
  response_upper = os.popen('./whois ' + param).read()
  response_lower = response_upper.lower()
  return ("<pre>" + response_lower + "</pre>")
  
@app.route('/status')
def status():
  response_upper = os.popen('bash stats.sh').read()
  response_lower = response_upper.lower()
  return ("<pre>" + response_lower + "</pre>")
  
@app.route('/upload', methods = ['POST', 'GET'])
def form():
  if request.method == 'POST':
     f = request.files['file']
     f.save(secure_filename(f.filename))
     return ("uploaded " + f.filename) 
  elif request.method == 'GET': 
    return render_template('index.html')
'''
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "File saved successfully"
        '''

app.run(host='0.0.0.0', port=5000)