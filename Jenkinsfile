pipeline {
    // vm2
    agent {
        label 'test'
    }
    stages {
        stage('Clone simple-api repository') {
            steps {
                git url: 'https://github.com/SoftDevGroup4/simple-api.git', branch: 'main' //clone git from branch main
            }
        }

        stage('Build and Test API') {
            steps {
                script {
                    // Build and test API
                    sh 'pip install -r requirements.txt ' // Install dependencies
                    sh 'python3 app.py &' //run app.py (API)
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
                        git url: 'https://github.com/SoftDevGroup4/simple-api-robot.git', branch: 'main' //clone git from branch main
                    }
                    sh 'cd ./robot3 && robot test_robot.robot' //run robot_test
                }
            }
        }

        // #build image
        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh 'docker login'
                    sh 'docker build -t baitoeykp/cicd:lastest .' //build image dockerhubUser/imageName:version (Dockerfile)
                    sh 'docker push baitoeykp/cicd:lastest' // push to docker hub
                }
            }
        }

        stage('Clean Workspace') { //delete old version
            steps {
                sh 'docker compose down' //down container
                sh 'docker system prune -a -f'
            }
        }
        stage('compose up') {
            steps {
                sh 'docker compose up -d --build' //build container (compose.yaml)
            }
        }

        //vm3
        stage('Running Preprod') {
            agent {
                label 'preprod'
            }
            steps {
                sh 'docker compose down && docker system prune -a -f && docker compose up -d --build' //(compose.yaml)
            }
        }
    }
}
