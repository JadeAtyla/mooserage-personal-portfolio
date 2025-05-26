from flask import Flask, redirect, render_template, request, flash
import json
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages


@app.route("/")
def index():
    with open("static/data/data.json", "r") as file:
        data = json.load(file)
    
    families = data.get("familyData", [])
    hobbies = data.get("hobbiesData", [])
    personal = data.get("personalData", [])
    skills = data.get("skillSet", [])
    projects = data.get("projectsData", [])
    schools = data.get("schoolsData", [])
    experiences = data.get("experiencesData", [])
    challenges = data.get("challengesData", [])
    plans = data.get("plansData", [])
    return render_template("index.html", families=families, hobbies=hobbies, personal=personal, skills=skills, projects=projects, schools=schools, experiences=experiences, challenges=challenges, plans=plans)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("fullname")
    email = request.form.get("email")
    message = request.form.get("message")
    # Compose email
    body = f"Greetings Jade, I'm {name},\n {message}"
    msg = MIMEText(body)
    msg["Subject"] = "Portfolio Contact Form Submission"
    msg["From"] = email
    msg["To"] = "jamadigal@gmail.com"

    # Send email (configure your SMTP server here)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.environ.get("EMAIL"), "lckw vdkp gttd txpw")#os.environ.get("EMAIL_PASSWORD"))
            
            server.sendmail(email, "jamadigal@gmail.com", msg.as_string())
        flash("Message sent successfully!", "success")
    except Exception as e:
        print(f"Error sending email: {e}")  # Log the error
        print(os.environ.get("EMAIL"), os.environ.get("APP_PASSWORD"))  # Log the email and password for debugging
        flash("Failed to send message.", "danger")
    return redirect("/#contact")

if __name__ == "__main__":
    app.run(debug=True)