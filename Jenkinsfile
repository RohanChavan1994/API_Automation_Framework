pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                // Set up Python and install dependencies
                bat 'set path="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\"'
                bat 'set path="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\"'
                bat 'pip install -r requirements.txt'

                // Run the specific test case(s)
                bat 'pytest .\\tests\\parallel\\test_full_crud_single2.py --html=report.html --alluredir=reports'
            }
        }
    }
}
