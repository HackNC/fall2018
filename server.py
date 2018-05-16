from flask import Flask, render_template, request, redirect, url_for
from requests import post
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email
from config import *

app = Flask(__name__)

# rate limiting by remote address
# default limit is 1 request per second
limiter = Limiter(
    app,
    key_func = get_remote_address,
    default_limits = ["1/1seconds"]
)

# wtform validation class for email
class EmailForm(Form):
    email = StringField('Email Address', [DataRequired(), Email()])

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html')

    # validates email with wtforms
    form = EmailForm(request.form)
    if not form.validate():
        return render_template('index.html', msg='Sorry, that email address is not valid.')

    # writes email to external file
    email = request.form['email']
    f = open('email_list', 'a')
    f.write(email + ",\n")
    f.close()

    try:
        EMAIL_SHEET_SCRIPT_URL
    except NameError:
        print("Google Sheet script URL is not defined.")
    except:
        print("Unknown error on Google Sheet script request")
    else:
        if not EMAIL_SHEET_SCRIPT_URL == "":
            # posts email to Google Sheets using Google script web app endpoint
            # endpoint should be set in config.py
            sheetRequest = post(EMAIL_SHEET_SCRIPT_URL, request.form)

    ## optional do something on Sheets success/failure
    # respMsg = "There was an error submitting your email, please try again later."
    # if sheetRequest.ok:
    #     respMsg = "Thank you for your interest in HackNC, we'll follow up with more information soon!"

    return render_template('index.html', msg="Thank you for your interest in HackNC, we'll follow up with more information soon!")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = DEBUG)