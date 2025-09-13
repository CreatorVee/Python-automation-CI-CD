environment {
    VENV_DIR = 'venv'
    EC2_IP = credentials('ec2-instance-ip')
    SSH_KEY = credentials('ssh-private-key')
}

stages {
    stage('Setup Python Environment') {
        steps {
            sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
            '''
        }
    }
    
    stage('Fetch Images from ECR') {
        steps {
            script {
                sh ". ${VENV_DIR}/bin/activate && python3 ecr_list_images.py > images.txt"
                def images = readFile('images.txt').trim().split("\\n")
                def userChoice = input message: 'Select image tag to deploy:', parameters: [
                    choice(name: 'IMAGE_TAG', choices: images.join('\n'), description: 'Choose an image tag')
                ]
                env.SELECTED_IMAGE_TAG = userChoice
                echo "User selected image: ${userChoice}"
            }
        }
    }
    
    stage('Deploy to EC2') {
        steps {
            sh """
                . ${VENV_DIR}/bin/activate && python3 deploy_to_ec2.py \\
                --image-tag ${env.SELECTED_IMAGE_TAG} \\
                --ec2-ip ${EC2_IP} \\
                --ssh-key ${SSH_KEY}
            """
        }
    }
    
    stage('Validate Deployment') {
        steps {
            sh """
                . ${VENV_DIR}/bin/activate && python3 validate_deployment.py --ec2-ip ${EC2_IP}
            """
        }
    }
}
