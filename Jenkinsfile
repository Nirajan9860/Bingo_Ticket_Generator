pipeline {
    agent { label 'jenkins_slave-56.12' }
 
    environment {
        REGISTRY_URL = 'harbor.nirajan.local'
        IMAGE_NAME = 'bingo'
        IMAGE_TAG = "v${BUILD_NUMBER}"
        HARBOR_CREDENTIALS = credentials('HARBOR_CREDENTIALS') // Jenkins credential ID
    }
 
    options {
        skipDefaultCheckout()
    }
 
    stages {
 
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/Nirajan9860/Bingo_Ticket_Generator.git'
            }
        }
 
        stage('Build Docker Image') {
            steps {
                
                script {
                    sh """
                        docker build -t ${REGISTRY_URL}/bingo/${IMAGE_NAME}:${IMAGE_TAG} .
                    """
                }
                
            }
        }
 
        stage('Login to Harbor') {
            steps {
                script {
                    sh """
                       docker login ${REGISTRY_URL} -u admin -p Harbor12345
                    """
                }
            }
        }
 
        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                        docker push ${REGISTRY_URL}/bingo/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }
 
        stage('Cleanup') {
            steps {
                script {
                    sh """
                        docker rmi ${REGISTRY_URL}/sachin/${IMAGE_NAME}:${IMAGE_TAG} || true
                    """
                }
            }
        }
    }
    // Post actions to handle pipeline completion
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