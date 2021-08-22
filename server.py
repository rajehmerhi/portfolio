import os
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

#smart way of doing it using this code
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#This function will let you write the 3 fields of the contact form to a database.txt file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

#This function will let you write the 3 fields of the contact form to a database.csv file
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data)
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'Something went wrong. Try again!'

#old fashion way, repetition
# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')