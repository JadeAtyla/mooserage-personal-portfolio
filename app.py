import json
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash

# Import Flask-Compress
from flask_compress import Compress #

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "your_fallback_secret_key")

# Initialize Flask-Compress
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript'] #
COMPRESS_LEVEL = 6 # Default is 6, can be 1 (fastest) to 9 (best compression)
COMPRESS_MIN_SIZE = 500 # Only compress responses larger than 500 bytes
Compress(app) #

# Load data from data.json once when the app starts
with open("static/data/data.json", "r") as file:
    portfolio_data = json.load(file)

@app.route("/")
@app.route("/about")
def about():
    # Data is already loaded, just extract what's needed for the about page
    families = portfolio_data.get("familyData", [])
    hobbies = portfolio_data.get("hobbiesData", [])
    personal = portfolio_data.get("personalData", [])
    return render_template("about.html",
                           active_page="about",
                           families=families,
                           hobbies=hobbies,
                           personal=personal)

@app.route("/skills")
def skills():
    skills_set = portfolio_data.get("skillSet", [])
    certificates = portfolio_data.get("certificationData", [])
    return render_template("skills.html",
                           active_page="skills",
                           skills=skills_set, # Renamed to avoid conflict with template variable 'skills'
                           certificates=certificates)

@app.route("/projects")
def projects():
    projects_data = portfolio_data.get("projectsData", [])
    return render_template("projects.html",
                           active_page="projects",
                           projects=projects_data)

@app.route("/challenges")
def challenges():
    challenges_data = portfolio_data.get("challengesData", [])
    return render_template("challenges.html",
                           active_page="challenges",
                           challenges=challenges_data)

@app.route("/plans")
def plans():
    plans_data = portfolio_data.get("plansData", [])
    return render_template("plans.html",
                           active_page="plans",
                           plans=plans_data)

@app.route("/resume")
def resume():
    schools_data = portfolio_data.get("schoolsData", [])
    experiences_data = portfolio_data.get("experiencesData", [])
    return render_template("resume.html",
                           active_page="resume",
                           schools=schools_data,
                           experiences=experiences_data)

@app.route("/contact", methods=["GET", "POST"]) # Added GET for direct access to contact page
def contact():
    if request.method == "POST":
        name = request.form.get("fullname")
        email = request.form.get("email")
        message = request.form.get("message")

        # Compose email
        # It's better to send the email from your configured EMAIL environment variable
        # and set reply-to or a note about the sender in the message body.
        sender_email = os.environ.get("EMAIL")
        receiver_email = "jamadigal@gmail.com" # This is your fixed recipient email

        if not sender_email:
            flash("Server email not configured. Cannot send message.", "danger")
            print("Error: EMAIL environment variable not set.")
            return redirect("/contact") # Redirect back to contact page

        body_text = f"Greetings Jade, I'm {name} ({email}).\n\nMessage:\n{message}"
        msg = MIMEText(body_text)
        msg["Subject"] = "Portfolio Contact Form Submission"
        msg["From"] = sender_email # Your email address
        msg["To"] = receiver_email
        msg["Reply-To"] = email # Allows you to reply directly to the sender

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, os.environ.get("EMAIL_PASSWORD"))
                server.sendmail(sender_email, receiver_email, msg.as_string())
            flash("Message sent successfully!", "success")
        except Exception as e:
            print(f"Error sending email: {e}")
            flash("Failed to send message.", "danger")
        return redirect("/contact") # Redirect to the GET route of contact page
    # For GET requests, just render the contact page
    return render_template("contact.html", active_page="contact")


if __name__ == "__main__":
    app.run(debug=True)