pipeline {
    agent {
        label 'test'
    }
    stages {
        stage('Build and Test API') {
            steps {
                script {
                    // Build and test API
                    sh 'pip install -r requirements.txt' // Install dependencies
                    sh 'python3 app.py &'
                    sh 'sleep 5' // Wait for API to start

                    // Run unit tests
                    sh 'python3 test_unit.py'
                }
            }
        }

        stage('Build and Test Robot Framework') {
            steps {
                script {
                    dir('./robot3/') {
                        git branch: 'main', credentialsId:'b6e295a8-1e05-4bf3-aa88-ee540cc4c56b', url: 'https://gitlab.com/sdp2092409/robot.git'
                    }
                    sh 'cd ./robot3 && robot test_robot.robot'
                }
            }
        }
        // #build image
        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh'docker login'
                    sh 'docker build -t cicd/sdp:lastest .'
                    sh 'docker push cicd/sdp:lastest'
                }
            }
        }
        stage('Clean Workspace') {
            steps {
                sh 'docker compose down'
                sh 'docker system prune -a -f'
            }
        }
        stage('compose up') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
        stage('Running Preprod') {
            agent {
                label 'preprod'
            }
            steps {
                sh 'docker compose down && docker system prune -a -f && docker compose up -d --build'
            }
        }
    }
}
