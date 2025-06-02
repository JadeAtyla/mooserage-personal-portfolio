import json
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash
from flask_compress import Compress

load_dotenv()

app = Flask(__name__)
# Flask secret key for session management and flashing messages
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "your_fallback_secret_key")

# Initialize Flask-Compress for HTTP response compression
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
COMPRESS_LEVEL = 6 # Default compression level
COMPRESS_MIN_SIZE = 500 # Minimum size for a response to be compressed
Compress(app)

# Load portfolio data from data.json once when the application starts
with open("static/data/data.json", "r") as file:
    portfolio_data = json.load(file)

@app.route("/")
@app.route("/about")
def about():
    # Extracts relevant data for the about page from the loaded portfolio_data
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
    # Extracts skill and certification data for the skills page
    skills_set = portfolio_data.get("skillSet", [])
    certificates = portfolio_data.get("certificationData", [])
    return render_template("skills.html",
                           active_page="skills",
                           skills=skills_set,
                           certificates=certificates)

@app.route("/projects")
def projects():
    # Extracts projects data for the projects page
    projects_data = portfolio_data.get("projectsData", [])
    return render_template("projects.html",
                           active_page="projects",
                           projects=projects_data)

@app.route("/challenges")
def challenges():
    # Extracts challenges data for the challenges page
    challenges_data = portfolio_data.get("challengesData", [])
    return render_template("challenges.html",
                           active_page="challenges",
                           challenges=challenges_data)

@app.route("/plans")
def plans():
    # Extracts plans data for the plans page
    plans_data = portfolio_data.get("plansData", [])
    return render_template("plans.html",
                           active_page="plans",
                           plans=plans_data)

@app.route("/resume")
def resume():
    # Extracts education and experience data for the resume page
    schools_data = portfolio_data.get("schoolsData", [])
    experiences_data = portfolio_data.get("experiencesData", [])
    return render_template("resume.html",
                           active_page="resume",
                           schools=schools_data,
                           experiences=experiences_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Handles form submission for contact page (POST request)
    if request.method == "POST":
        name = request.form.get("fullname")
        email = request.form.get("email")
        message = request.form.get("message")

        # Sender email configured via environment variable
        sender_email = os.environ.get("EMAIL")
        # Fixed recipient email for all contact form submissions
        receiver_email = "jamadigal@gmail.com"

        # Check if sender email is configured
        if not sender_email:
            flash("Server email not configured. Cannot send message.", "danger")
            print("Error: EMAIL environment variable not set.")
            return redirect("/contact")

        # Compose email body and headers
        body_text = f"Greetings Jade, I'm {name} ({email}).\n\nMessage:\n{message}"
        msg = MIMEText(body_text)
        msg["Subject"] = "Portfolio Contact Form Submission"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Reply-To"] = email # Allows direct reply to the sender's email

        try:
            # Establish secure SMTP connection and send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, os.environ.get("EMAIL_PASSWORD"))
                server.sendmail(sender_email, receiver_email, msg.as_string())
            flash("Message sent successfully!", "success")
        except Exception as e:
            # Log and flash error if email sending fails
            print(f"Error sending email: {e}")
            flash("Failed to send message.", "danger")
        return redirect("/contact") # Redirect after POST to prevent resubmission

    # For GET requests, simply render the contact page
    return render_template("contact.html", active_page="contact")

# Run the Flask application in debug mode if executed directly
if __name__ == "__main__":
    app.run(debug=True)
