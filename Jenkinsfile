pipeline {
  agent any
  environment {
    IMAGE = "ghcr.io/alexandrupasat/tiny-web-app:latest"
  }
  stages {
    stage('Checkout'){ steps { checkout scm } }
    stage('Build'){ steps { sh 'docker build -t $IMAGE .' } }
    stage('Login to GHCR'){
      steps {
        withCredentials([usernamePassword(credentialsId: 'ghcr', usernameVariable: 'USER', passwordVariable: 'TOKEN')]) {
          sh 'echo $TOKEN | docker login ghcr.io -u $USER --password-stdin'
        }
      }
    }
    stage('Push'){ steps { sh 'docker push $IMAGE' } }
    stage('Deploy'){
      steps {
        sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy.yml'
      }
    }
  }
}
