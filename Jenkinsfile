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
                PATH = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311;" + "${env.PATH}"
            }
            steps {
                // Run commands using the Python path and pip
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pytest -n auto .\\tests\\parallel\\test_full_crud_single2.py --html=report.html --alluredir=reports'

                allure includeProperties: false, jdk: '', results: [[path: 'reports']]
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
            }
        }
    }

    post {
        always {
            // Determine build status
            script {
                def buildStatus = currentBuild.result ?: 'SUCCESS'
                def subject = "Jenkins Build ${buildStatus}"

                // Zip the HTML report
                bat 'powershell Compress-Archive -Path .\\report\\*.html -DestinationPath report.zip'

                // Email notification after the build completes
                emailext subject: subject,
                    body: "Your Jenkins build has ${buildStatus.toLowerCase()}. Check the build status!",
                    to: 'rohanforjobs@gmail.com',
                    attachmentsPattern: '**/*.zip'
            }
        }
    }
}
