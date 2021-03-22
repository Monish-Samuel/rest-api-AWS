pipeline {
    agent any

    stages {
        stage('Docker Image Build'){
            steps{
                bat 'docker build -t github_api .'
            }
        }
        stage('Docker Hub image Tagging'){
            steps{
                bat 'docker tag github_api:latest monish7/github_api'
            }
        }
    }
}
