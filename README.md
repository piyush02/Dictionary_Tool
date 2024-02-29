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

Authentication with DictionaryAPI.com

To authenticate with the Merriam-Webster dictionary API, the script requires an API key. This API key is stored as the API_KEY variable in the script. The API key is used to include the key parameter in the API request URL, allowing access to the API's features.

Usage
Running Locally

    Ensure you have Python installed on your system.

    Install the required Python packages:



pip install -r requirements.txt

Run the Flask application:



    python3 dict_flask.py

    Open a web browser and go to http://localhost:5000 to access the application.
Without Python Installed

    Simply run the binary executable dict_flask:
    ./dict_flask



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

Continuous Deployment (CD) Workflow

This GitHub Actions workflow automates the deployment process for the dictionary application to an AWS EKS Kubernetes cluster. It performs the following steps:

    Checkout Code: Checks out the code from the main branch of the repository.

    Set up AWS CLI: Installs and configures the AWS CLI tool for interacting with Amazon Web Services.

    Login to AWS EKS: Uses the aws eks command to authenticate with the AWS EKS cluster and download the kubeconfig file.

    Apply Namespace: Applies the Kubernetes namespace configuration to the cluster.

    Create Docker Registry Secret: Creates a Kubernetes secret for accessing the Docker registry. This secret is used to pull Docker images during deployment.

    Apply Deployment: Applies the Kubernetes deployment configuration (dict_flask.yaml) to the cluster, which deploys the Flask application as a Kubernetes deployment.

Usage
Triggering the Workflow

The CD workflow is triggered manually. To trigger the workflow, follow these steps:

    Navigate to the "Actions" tab in your GitHub repository.

    Select the "Continuous Deployment" workflow.

    Click on the "Run workflow" button.

Input Parameters

The workflow does not require any input parameters. All necessary configuration values are stored securely as GitHub secrets.
Workflow Outputs

This workflow does not produce any output.
Secrets

The following secrets must be configured in the repository settings:

    AWS_ACCESS_KEY_ID: The AWS access key ID for authenticating with AWS.
    AWS_SECRET_ACCESS_KEY: The AWS secret access key for authenticating with AWS.
    AWS_DEFAULT_REGION: The AWS region where the EKS cluster is located.
    DOCKER_REGISTRY_SERVER: The URL of the Docker registry server.
    DOCKER_USER: The username for authenticating with the Docker registry.
    DOCKER_PASSWORD: The password for authenticating with the Docker registry.
    DOCKER_EMAIL: The email address associated with the Docker registry account.
    YOUR_EKS_CLUSTER_NAME: The name of your AWS EKS cluster.

Ensure that these secrets are securely stored and managed.
Workflow Structure

The workflow is defined in the .github/workflows/cd.yml file in the repository. It consists of several steps, each performing a specific deployment task.
Workflow Triggers

The workflow is triggered manually. It does not run automatically on push events.
Conclusion

This CD workflow automates the deployment process for the dictionary application to an AWS EKS Kubernetes cluster, making it easy to deploy changes quickly and consistently.

Unit Testing for Dictionary Flask App

This repository contains unit tests for testing the functionality of the Dictionary Flask App. The unit tests are written in Python using the unittest framework and the unittest.mock module for mocking external dependencies.
File Structure

    dict_flask.py: The main Flask application file containing the routes and logic for interacting with the Merriam-Webster Dictionary API.
    unit_test.py: The unit test file containing test cases for testing the functionality of the Flask application.
    venv/: Virtual environment directory for managing Python dependencies.

Running the Tests

To run the unit tests, follow these steps:

    Clone the Repository: Clone this repository to your local machine.

    

git clone https://github.com/your-username/your-repository.git

Navigate to the Repository Directory: Change your current directory to the cloned repository.


cd your-repository

Activate Virtual Environment (Optional): If you prefer to use a virtual environment, activate it using the following command.


source venv/bin/activate

Install Dependencies: Install the required dependencies using pip.


pip install -r requirements.txt

bash

    python unit_test.py

Test Cases

The unit tests cover the following scenarios:

    Testing the index route to ensure it returns the correct HTML content.
    Testing the search route with a valid word to verify the response.
    Testing the search route with a non-existent word to verify the error message.
    Testing the get_definition function with a successful API response.
    Testing the get_definition function with an error response from the API.

Mocking External Dependencies

The unit tests use the unittest.mock.patch decorator to mock external dependencies such as the requests.get method. This allows the tests to run independently of external services, ensuring reliable and consistent results.


