pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://your-repo-url'
            }
        }

        stage('User Input') {
            steps {
                script {
                    env.IMAGE_TAG = input(
                        message: "Choose the image tag to deploy",
                        parameters: [
                            choice(name: 'TAG', choices: ['1.0', '2.0', '3.0'], description: 'Pick an image version')
                        ]
                    )
                }
            }
        }

        stage('Deploy via Python') {
            steps {
                sh """
                    python3 deploy_from_ecr.py << EOF
                    ${IMAGE_TAG}
                    EOF
                """
            }
        }
    }
}
