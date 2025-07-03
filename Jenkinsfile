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
                        docker rmi ${REGISTRY_URL}/bingo/${IMAGE_NAME}:${IMAGE_TAG} || true
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
            mail to: 'nirajanp9860@gmail.com',
             subject: "Jenkins Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: "Good news!\n\nThe Jenkins pipeline '${env.JOB_NAME}' build #${env.BUILD_NUMBER} has succeeded.\n\nCheck details at: ${env.BUILD_URL}"
        }
        failure {
            echo 'Pipeline failed.'
            mail to: 'nirajanp9860@gmail.com',
             subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: "Unfortunately, the Jenkins pipeline '${env.JOB_NAME}' build #${env.BUILD_NUMBER} has failed.\n\nCheck details at: ${env.BUILD_URL}"
        }
    }
}