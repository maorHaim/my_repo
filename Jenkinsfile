pipeline {
    agent {label 'slave1'}
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs : [[
                        url: 'https://github.com/maorHaim/my_repo.git',
                        credentialsId: ''
                    ]]
                ])
            }
        }

        stage('Clone repo') {
            steps {
                sh "git clone https://github.com/maorHaim/my_repo.git"
            }
        }
   
        stage('Build image') {
            steps {
                sh "sudo docker build -t flask_project:1.0 ./my_repo/project"
            }
        }
        
        stage('Test'){
            steps {
                script {
                    def result = sh(script: "curl -sSf http://localhost:5000/maor", returnStatus: true)
                    if (result == 0) {
                        echo 'Docker image build and run successful.' 
                    } else { 
                        error 'Docker image build and run failed.'
                    }
                }
            }
            post {
                   success {
                     echo 'Deploying Docker image'
                       agent {
                          label 'agentp1'
                       }
                      sh "sudo docker run -d -p 5000:5000 flask_project:1.0"
                  }
              }
        }
    }
    post {
        always {
            deleteDir()
            sh 'sudo docker stop $(sudo docker ps -q --filter ancestor=flask_project:1.0)'
        }
    }
}
