pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                //
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                //
                sh 'docker build -t sdet-framework-image .'
            }
        }
        stage('Run Automation') {
            steps {
                //
                sh 'docker run sdet-framework-image'
            }
        }
    }
    post {
        always {
            //
            archiveArtifacts artifacts: 'report.html'
        }
    }
}