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
                bat 'set PATH=C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311;'
                bat 'python -m pip install -r requirements.txt'

                // Run the specific test case(s)
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytest" .\\tests\\parallel\\test_full_crud_single2.py --html=report.html --alluredir=reports'
            }
        }
    }
}
