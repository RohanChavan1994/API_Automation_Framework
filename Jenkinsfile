pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            environment {
                PATH = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311;" + "${env.PATH}"
            }
            steps {
                // Run commands using the Python path and pip
                bat 'python -m pip install -r requirements.txt'
                bat 'pytest .\\tests\\parallel\\test_full_crud_single2.py --html=report.html --alluredir=reports'
            }
        }
    }
}
