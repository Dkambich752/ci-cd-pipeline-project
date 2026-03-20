pipeline {
    
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This command pulls your python files from GitHub to the EC2 server
                checkout scm
            }
        }
        stage('Run Automated Tests') {
            steps {
                echo 'Starting Pytest for Telemetry Logic...'
                // This command tells Ubuntu to run python test file using pytest
                sh 'pytest TelemetryTest.py'
            }
        }
        stage('Quality Gate Results') {
            steps {
                echo 'Logic Verified. Quality Gate: PASSED.'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Quality Gate Passed! Deploying telemetry logic...'
            }
        }
    }
}
