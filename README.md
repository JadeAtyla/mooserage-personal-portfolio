<h1 align="center">Mooserage Personal Portfolio (Flask Web App)</h1>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-setup-and-running">Setup & Running</a> &#xa0; | &#xa0;
  <a href="#file_folder-project-structure">Project Structure</a> &#xa0; | &#xa0;
</p>

<br>

## :dart: About ##

This is a personal portfolio website built using the Flask web framework in Python. It serves as a dynamic showcase of personal information, skills, projects, challenges, future plans, and a resume, along with a functional contact form. The application uses Jinja2 for templating and serves static assets (CSS, JS, images). All dynamic content for the various sections is efficiently loaded from a `static/data/data.json` file, making content updates straightforward.

## :sparkles: Features ##

:heavy_check_mark: **Dynamic Content Loading:** All textual and structured data for pages like About, Skills, Projects, Challenges, Plans, and Resume is loaded from a central `data.json` file.

:heavy_check_mark: **About Page:** Presents personal details, family information, and hobbies.

:heavy_check_mark: **Skills Page:** Displays a comprehensive list of skill sets and acquired certifications.

:heavy_check_mark: **Projects Page:** Showcases a portfolio of personal projects with descriptions.

:heavy_check_mark: **Challenges Page:** Details various challenges and learning experiences undertaken.

:heavy_check_mark: **Plans Page:** Outlines future goals, aspirations, and development plans.

:heavy_check_mark: **Resume Page:** Provides a structured view of educational background and professional experiences.

:heavy_check_mark: **Contact Form:** A fully functional contact form allowing visitors to send messages directly via email. This feature requires specific SMTP configuration.

:heavy_check_mark: **Response Compression:** Integrates Flask-Compress to automatically compress HTTP responses (HTML, CSS, JS, JSON) using Brotli, Gzip, or Deflate, improving loading times and bandwidth usage.

## :rocket: Technologies ##

The following key technologies and libraries were used in the development of this project:

-   **Python:** The core programming language for the backend logic.
-   **Flask:** A lightweight and flexible WSGI web application framework used for building the web application.
-   **Jinja2:** A powerful and designer-friendly templating language for Python, used for rendering HTML pages.
-   **Flask-Compress:** A Flask extension that provides various compression algorithms (Gzip, Deflate, Brotli) for HTTP responses, optimizing performance.
-   **python-dotenv:** Used for loading environment variables from a `.env` file, ensuring sensitive information like API keys and email credentials are not hardcoded.
-   **smtplib:** Python's standard library module for sending emails using the Simple Mail Transfer Protocol (SMTP), used for the contact form functionality.
-   **email.mime.text:** A module from Python's email package used to create email messages with plain text content.

## :white_check_mark: Requirements ##

Before you can run this project, ensure you have the following installed:

-   **Python 3.x** (recommended Python 3.8 or higher)
-   **pip** (Python package installer, usually comes with Python)
-   **Git** (for cloning the repository)

All specific Python dependencies are listed in `requirements.txt` and will be installed in the setup process.

## :checkered_flag: Setup and Running ##

Follow these steps to get the Flask portfolio application up and running on your local machine:

1.  **Clone the repository:**
    Open your terminal or command prompt and run:
    ```bash
    git clone https://github.com/JadeAtyla/mooserage-personal-portfolio.git
    cd mooserage-personal-portfolio
    ```

2.  **Create a virtual environment (highly recommended):**
    A virtual environment isolates your project's Python dependencies from other projects.
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    With your virtual environment activated, install all required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables:**
    The application uses environment variables for sensitive information (like the Flask secret key and email credentials).
    * Create a new file named `.env` in the root directory of your project (the same directory as `app.py`).
    * Add the following lines to your `.env` file, replacing the placeholder values with your actual information:
        ```dotenv
        FLASK_SECRET_KEY="your_super_secret_key_here"
        EMAIL="your_sender_email@gmail.com"
        EMAIL_PASSWORD="your_email_app_password"
        ```
    * **Important Note on `EMAIL_PASSWORD`:**
        * If you are using **Gmail** and have **2-Factor Authentication (2FA)** enabled on your Google account, you **must** generate an "App password" to use here instead of your regular Gmail account password. You can typically generate an App password from your Google Account security settings (`myaccount.google.com/security`).
        * Ensure the `EMAIL` variable is set to the email address you will use to send messages from the contact form. This email will be used as the `From` address. The `Reply-To` address will be the sender's email from the contact form.

6.  **Run the application:**
    You can run the Flask development server using:
    ```bash
    flask run
    ```
    Alternatively, you can run the `app.py` directly:
    ```bash
    python app.py
    ```

7.  **Access the application:**
    Once the server starts, open your web browser and navigate to:
    `http://127.0.0.1:5000` (or `http://localhost:5000`)

## :file_folder: Project Structure ##

The project follows a standard Flask application structure:

```bash
.
├── app.py                  # Main Flask application file, defines routes and logic.
├── requirements.txt        # Lists all Python dependencies required for the project.
├── .env                    # Environment variables for configuration (e.g., secret key, email credentials).
├── static/                 # Directory for static assets like CSS, JavaScript, images, and data.
│   ├── css/                # Contains CSS stylesheets.
│   ├── js/                 # Contains JavaScript files.
│   ├── images/             # (Optional) For any images used in the portfolio.
│   └── data/
│       └── data.json       # JSON file holding all dynamic content for the portfolio pages.
└── templates/              # Directory for Jinja2 HTML templates.
├── about.html          # Template for the About page.
├── skills.html         # Template for the Skills page.
├── projects.html       # Template for the Projects page.
├── challenges.html     # Template for the Challenges page.
├── plans.html          # Template for the Plans page.
├── resume.html         # Template for the Resume page.
├── contact.html        # Template for the Contact page.
└── base.html           # Base template that other HTML files extend for common layout elements.
```
&#xa0;

<a href="#top">Back to top</a>
