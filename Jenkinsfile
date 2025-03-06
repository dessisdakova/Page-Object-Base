pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                git branch: "main", url: "https://github.com/dessisdakova/Page-Object-Base.git"
            }
        }

        stage("Create and activate venv") {
            steps {
                sh "python3 -m venv venv"
                sh "source .venv/bin/activate"
            }

        stage("Install dependencies for tests") {
            steps {
                sh "pip install -r requirements.txt"
            }

        stage("Run tests") {
            steps {
                sh "pytest -v"
            }
        }
    }
}