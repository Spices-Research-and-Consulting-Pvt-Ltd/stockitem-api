pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Set Server Configuration') {
            steps {
                script {
                    try {

                        // Build and deploy using docker-compose
                        sh 'docker-compose build'
                        sh 'docker-compose up -d'

                        // Success message
                        echo 'Deployment successful!'
                        
                    } catch (Exception e) {

                        // Error message
                        echo "Error: ${e.message}"
                        error("Deployment failed!")
                    }
                }
            }
        }
    }
}
