pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --alluredir=reports/allure-reports'
            }
        }
        stage('Generate Report') {
            steps {
                sh 'allure generate reports/allure-reports --clean -o reports/allure-html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'reports/allure-html/**', fingerprint: true
            publishHTML(target: [
                reportDir: 'reports/allure-html',
                reportFiles: 'index.html',
                reportName: 'Allure Report'
            ])
        }
    }
}
