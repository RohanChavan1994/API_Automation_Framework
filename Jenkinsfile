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
                bat 'python -m pytest -n auto .\\tests\\parallel\\test_full_crud_single2.py --html=.\\html_report\\report.html --alluredir=reports'

                allure includeProperties: false, jdk: '', results: [[path: 'reports']]
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'html_report', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])

                script {
                    // Define the paths to be compressed
                    def path1 = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Pipeline-API-Automation\\allure-report"
                    def path2 = "C:\\ProgramData\\Jenkins\\.jenkins\\jobs\\Pipeline-API-Automation\\htmlreports"

                    // Combine paths into a single comma-separated string
                    def combinedPaths = "\"${path1}\",\"${path2}\""

                    // Compress-Archive using the combined paths
                    bat "powershell Compress-Archive -Force -Path ${combinedPaths} -DestinationPath reports.zip"

                    // Define the path to the specific ZIP file to be attached
                    // def attachment = "${env.WORKSPACE}\\reports.zip"

                    def buildStatus = currentBuild.result ?: 'SUCCESS'
                    def subject = "Jenkins Build ${buildStatus}"

                    // Email notification after the build completes
                    mail to: 'jenkinsemailsetup@gmail.com',
                        subject: subject,
                        body: "Your Jenkins build has ${buildStatus.toLowerCase()}. Check the build status!",
                        attachments: "reports.zip"
                }
            }
        }
    }
}
