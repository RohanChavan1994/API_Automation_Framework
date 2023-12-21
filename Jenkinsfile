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
                PATH = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts;" + "${env.PATH}"
            }
            steps {
                // Run commands using the Python path and full path to pytest
                bat 'python -m pip install -r requirements.txt'
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytest" .\\tests\\parallel\\test_full_crud_single2.py --html=report.html --alluredir=reports'
            }
        }
    }
}
