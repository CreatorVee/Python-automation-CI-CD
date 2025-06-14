pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('jenkins_aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins_aws_secret_access_key')
        AWS_DEFAULT_REGION = 'eu-north-1'
        VENV_DIR = '.venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install boto3 paramiko requests
                '''
            }
        }

        stage('Fetch Images from ECR') {
            steps {
                script {
                    // Run your Python script that lists ECR images
                    sh ". ${VENV_DIR}/bin/activate && python3 ecr_list_images.py > images.txt"

                    // Read the images.txt file into a Groovy list
                    def images = readFile('images.txt').trim().split("\\n")

                    // Let user select one image tag
                    def userChoice = input message: 'Select image tag to deploy:', parameters: [
                        choice(name: 'IMAGE_TAG', choices: images.join('\n'), description: 'Choose an image tag')
                    ]

                    // Save choice in environment for next stages
                    env.SELECTED_IMAGE_TAG = userChoice
                    echo "User selected image: ${userChoice}"
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sh """
                    . ${VENV_DIR}/bin/activate && python3 deploy_to_ec2.py --image-tag ${env.SELECTED_IMAGE_TAG} --ec2-ip 16.171.62.9 --ssh-key ~/.ssh/id_rsa
                    """
                }
            }
        }

        stage('Validate Deployment') {
            steps {
                script {
                    sh """
                    . ${VENV_DIR}/bin/activate && python3 validate_deployment.py --ec2-ip 16.171.62.9
                    """
                }
            }
        }
    }
}
