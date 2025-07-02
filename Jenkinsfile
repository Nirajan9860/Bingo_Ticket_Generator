pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Replace with your build tool, e.g., Gradle, Maven, npm, etc.
                echo 'Building the project...'
                python3 main.py
            }
        }

        
        stage('Deploy') {
            steps {
                // Replace with your deployment steps
                echo 'Deploying the application...'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}