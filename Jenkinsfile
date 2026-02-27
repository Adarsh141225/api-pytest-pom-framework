pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Automation') {
            steps {
                sh 'pytest --html=report.html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html'
        }
    }
}