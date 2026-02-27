pipeline {
    agent {
        // This launches a clean Python environment for your commands
        docker { image 'python:3.9-slim' }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Now pip is guaranteed to exist because we are in the python image
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Run Automation') {
            steps {
                // This generates your report
                sh 'pytest --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            // This ensures the report is saved to the Jenkins UI
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}