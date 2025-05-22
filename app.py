from flask import Flask, redirect, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    with open("static/data/data.json", "r") as file:
        data = json.load(file)
    
    families = data.get("familyData", [])
    hobbies = data.get("hobbiesData", [])
    personal = data.get("personalData", [])
    skills = data.get("skillSet", [])
    return render_template("index.html", families=families, hobbies=hobbies, personal=personal, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)