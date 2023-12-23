pipeline {
    agent any

    stages {
        stage('Test Email') {
            steps {
                emailext subject: 'Test Email Subject',
                    body: 'Test Email Body',
                    to: 'rohanforjobs@gmail.com'
            }
        }
    }
}
