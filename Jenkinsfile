pipeline {
    agent any

    stages {
        stage('Test Email') {
            steps {
                emailext subject: 'Test Email Subject',
                    body: 'Test Email Body',
                    to: 'ka22ej3777@gmail.com'
            }
        }
    }
}
