pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'eu-north-1'
        ECR_URL = '353545917196.dkr.ecr.eu-north-1.amazonaws.com'
        REPO_NAME = 'tf-python'
        EC2_USER = 'ec2-user'
        EC2_HOST = '16.171.62.9'
        SSH_KEY_PATH = '~/.ssh/id_rsa'
    }

    stages {
        stage('Install Python Dependencies') {
    steps {
        sh '''
            python3 -m venv .venv
            . .venv/bin/activate
            pip install boto3 paramiko
        '''
    }
}

stage('Fetch Images from ECR') {
    steps {
        sh '. .venv/bin/activate && python3 ecr_list_images.py'
    }
}

        stage('Input: Choose Image Tag') {
            steps {
                script {
                    def selectedTag = input message: 'Select image to deploy:', parameters: [
                        string(name: 'TAG', defaultValue: 'latest', description: 'Image tag')
                    ]
                    writeFile file: 'selected_tag.txt', text: selectedTag
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    def selectedTag = readFile('selected_tag.txt').trim()
                    def image = "${ECR_URL}/${REPO_NAME}:${selectedTag}"
                    def commands = """
                        aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${ECR_URL}
                        docker pull ${image}
                        docker stop tf-app || true
                        docker rm tf-app || true
                        docker run -d --name tf-app -p 80:80 ${image}
                    """.stripIndent()

                    // Write deploy.sh
                    writeFile file: 'deploy.sh', text: commands

                    // Copy and run on EC2
                    sh """
                        chmod 600 ${SSH_KEY_PATH}
                        scp -o StrictHostKeyChecking=no -i ${SSH_KEY_PATH} deploy.sh ${EC2_USER}@${EC2_HOST}:/home/${EC2_USER}/deploy.sh
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY_PATH} ${EC2_USER}@${EC2_HOST} 'bash deploy.sh'
                    """
                }
            }
        }

        stage('Validate Deployment') {
            steps {
                sh 'curl -I http://16.171.62.9'
            }
        }
    }
}
