Dictionary Flask Application

This project is a simple Flask web application that allows users to query the Merriam-Webster dictionary API to get definitions of words.
Files and Directories

    dict_flask: Binary executable file built using PyInstaller.
    dict_flask.py: Python script containing the Flask application logic.
    CI.yml: GitHub Actions workflow file for Continuous Integration (CI).
    templates/index.html: HTML template for the search form page.
    templates/result.html: HTML template for displaying search results.
    requirements.txt: List of Python dependencies required by the application.
    Dockerfile: Dockerfile for building a Docker image of the application.

Usage
Running Locally

    Ensure you have Python installed on your system.

    Install the required Python packages:



pip install -r requirements.txt

Run the Flask application:



    python3 dict_flask.py

    Open a web browser and go to http://localhost:5000 to access the application.

Running with Docker

    Build the Docker image:

    

docker build -t dictionary-flask-app .

Run the Docker container:



    docker run -p 5000:5000 dictionary-flask-app

    Open a web browser and go to http://localhost:5000 to access the application.

CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions. The workflow (CI.yml) consists of the following steps:

    Checkout the repository.
    Set up Python environment.
    Install PyInstaller.
    Build the Flask application.
    Build the Docker image.
    Push the Docker image to Docker Hub.

