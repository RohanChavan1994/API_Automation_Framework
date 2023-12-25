pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                // Run commands using the Python path and pip
                python -m pip install -r requirements.txt
                bat 'python -m pytest -n auto .\\tests\\parallel\\test_full_crud_single2.py --html=report.html --alluredir=reports'

                allure includeProperties: false, jdk: '', results: [[path: 'reports']]
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])

                script {
                    def buildStatus = currentBuild.result ?: 'SUCCESS'
                    println(buildStatus)
                    def subject = "Jenkins Build ${buildStatus}"
                    println(subject)

                    // Zip the HTML report
                    bat 'powershell Compress-Archive -Force -Path C:\\ProgramData\\Jenkins\\.jenkins\\jobs\\Pipeline-API-Automation\\htmlreports\\HTML_20Report\\report.html -DestinationPath report.zip'

                    // Email notification after the build completes
                    emailext subject: subject,
                        body: "Your Jenkins build has ${buildStatus.toLowerCase()}. Check the build status!",
                        to: 'ka22ej3777@gmail.com',
                        attachmentsPattern: '**/*.zip'
                }
            }
        }
    }
}
