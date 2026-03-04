pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/2004Shivam/MedicureEnhanced.git'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('medicure-tests') {
                    sh 'mvn clean test'
                }
            }
        }

    }
}