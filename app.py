from configparser import ConfigParser
from flask import Flask,request,render_template,redirect,flash
from flask_mail import Mail, Message

app = Flask(__name__)

mail=Mail(app)

config=ConfigParser()
config.read("config.ini")

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config["account"]["username"]
app.config['MAIL_PASSWORD'] = config["account"]["password"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def resume():
    return render_template("resume.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/form",methods=["POST"])
def form():
    name=request.form["user_name"]
    message=request.form["user_email"]
    num=request.form["user_phone"]
    info=request.form["user_comments"]

    msg = Message('Resume Contact', sender = sender_email_id_in_quotes, recipients = [message])
    msg.body = "Hey "+name+" wants you to contact  for the following details "+num+" Mail: "+message+" info is "+info
    mail.send(msg)
    return render_template("output.html",name=name)


if __name__=='__main__':
    app.run(debug=True)
