pipeline {
    agent {
        label 'test'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from the provided GitHub repository
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Modr3d/api_unittest.git']]])
                }
            }
        }

        stage('Build and Test API') {
            steps {
                script {
                    // Build and test API
                    sh 'pip install -r requirements.txt' // Install dependencies
                    sh 'python app.py &'
                    sh 'sleep 5' // Wait for API to start

                    // Run unit tests
                    sh 'python test_unit.py'
                }
            }
        }

        stage('Build and Test Robot Framework') {
            steps {
                script {
                    // Clone the Robot Framework repo
                    git 'https://path/to/robotframework/repo.git'

                    // Run Robot Framework tests
                    sh 'robot test_robot.robot'
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build and push Docker image to GitLab registry
                    sh 'docker build -t registry.gitlab.com/your-username/your-image-name .'
                    sh 'docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD registry.gitlab.com'
                    sh 'docker push registry.gitlab.com/your-username/your-image-name'
                }
            }
        }

        // stage('Push ⬆️') {
        //     steps {
        //         sh 'docker push cheiby/jenkins-assingment:lastest'
        //     }
        // }
        // stage('Clean Workspace') {
        //     steps {
        //         echo 'DownTime'
        //         sh 'docker compose -f ./docker-compose.dev.yaml down'
        //         sh 'docker system prune -a -f'
        //     }
        // }
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