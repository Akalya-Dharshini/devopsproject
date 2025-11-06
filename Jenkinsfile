pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        GIT_REPO = 'https://github.com/Akalya-Dharshini/devopsproject.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo '📦 Cloning repository...'
                git branch: 'main', url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image for Flask app...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Deploy Application with Docker Compose') {
            steps {
                echo '🚀 Deploying with Docker Compose...'
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful! Flask app is live on port 5000.'
        }
        failure {
            echo '❌ Build or Deployment failed. Check logs in Jenkins console.'
        }
    }
}
