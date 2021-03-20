pipeline {
    agent any

    stages {
        stage('Docker Image Build'){
            steps{
                bat 'docker build -t github_api .'
            }
        }
    }
}