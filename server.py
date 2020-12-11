'''flask web server implementation for website'''

# make sure to put this in dev mode for debugging:
# 'export FLASK_ENV=development'
# 'export FLASK_APP=server.py'
#Run server with: 'flask run' or 'python -m flask run'
import os.path
from datetime import date
#import sqlite3
#TODO: I'd love to use this ORM but its broken on my system
import time
from flask_sqlalchemy import sqlalchemy
# import sqlalchemy
import csv
import pymongo
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

#TODO: I'd love to use this ORM but its broken on my system

# Base = declarative_base()

# engine = create_engine('sqlite:///messaes.db', echo =  True)

def time_stamp(data):
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    data["date"] = d2

@app.route('/')
def root_node():
    return render_template('./index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(f'./{pagename}')

@app.route('/art/<string:artpagename>')
def html_page_art(artpagename):
    return render_template(f'./{artpagename}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            time_stamp(data)
            easy_file_write(data)
            # write_to_file(data)
            write_to_csv(data)
            return "form submitted", redirect('./thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        print('error! Try again')
        return redirect('/thankyou.html')

def easy_file_write(data):
    if os.path.isfile('./database.txt'):
        print("file FOUND!!!!!!!**********!!!!!!!")
    else:
        print('NO file found!!!!!!!!!!!!!*********!!!!!!!')
        f = open('./databaase.txt', "a+")
        for key, value in data.items():
            f.write(f'{key} : {value} \n')
        f.close()

# @app.route('/submit_form', methods=['POST', 'GET'])
# def write_to_file(data):
#     with open('./database.txt', mode='a') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database2.write(f'|\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a+') as database3:
        date = data["date"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([date, email, subject, message])

# def write_to_db(data):
#     email = data["email"]
#     subject = data["subject"]
#     message = data["message"]
#     file = database2.write(f'|\n{email},{subject},{message}')
