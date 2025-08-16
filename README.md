⚡ Automation with Python – AWS & Jenkins

This repository demonstrates automation of AWS services and DevOps pipelines using Python.
It contains exercises showcasing AWS resource management, EC2 deployments, Docker containers, ECR repositories, and Jenkins pipelines.

──────────────────────────────────────────────

📖 Overview of Exercises

──────────────────────────────────────────────

╔══════════════════════════════════════════════════╗
║ 🟢 EXERCISE 1: Working with Subnets in AWS ║
╚══════════════════════════════════════════════════╝

Goal: Get all subnets in your default AWS region and print the subnet IDs.

python exercise1_subnets.py


AWS CLI Equivalent:

aws ec2 describe-subnets --query 'Subnets[*].SubnetId'


Output: Prints all subnet IDs in your AWS account.

──────────────────────────────────────────────

╔══════════════════════════════════════════════════╗
║ 🟢 EXERCISE 2: Working with IAM in AWS ║
╚══════════════════════════════════════════════════╝

Goal:

List all IAM users.

Print each user’s name and last active time.

Show the most recently active user.

python exercise2_iam.py


AWS CLI Equivalent:

aws iam list-users


Output:

List of users with PasswordLastUsed timestamps

Most recently active user (ID + Name)

──────────────────────────────────────────────

╔══════════════════════════════════════════════════╗
║ 🟢 EXERCISE 3: Automating EC2 + Docker + Nginx ║
╚══════════════════════════════════════════════════╝

Goal:

Launch EC2 in default VPC

Install Docker on EC2

Start Nginx container

Open port 80

Monitor container health

python exercise3_ec2_nginx.py


AWS CLI / Commands:

# Launch EC2 instance
aws ec2 run-instances --image-id <AMI_ID> --instance-type t2.micro \
--key-name <KEY_PAIR> --security-group-ids <SG_ID> --subnet-id <SUBNET_ID>

# SSH into EC2 and install Docker
ssh -i ~/.ssh/my-key.pem ec2-user@<EC2_PUBLIC_IP> \
"sudo amazon-linux-extras install docker -y; sudo service docker start; sudo usermod -a -G docker ec2-user"

# Run Nginx container
ssh -i ~/.ssh/my-key.pem ec2-user@<EC2_PUBLIC_IP> \
"docker run -d -p 80:80 nginx"


Output:

EC2 running ✅

Nginx accessible at http://<EC2-Public-IP> 🌐

Monitoring automatically checks container health 🟢

──────────────────────────────────────────────

╔══════════════════════════════════════════════════╗
║ 🟢 EXERCISE 4: Working with ECR in AWS ║
╚══════════════════════════════════════════════════╝

Goal:

List all ECR repositories

Print repository names

List image tags for one repository (newest first)

python exercise4_ecr.py


AWS CLI / Commands:

# List all repositories
aws ecr describe-repositories

# List images for a repository
aws ecr list-images --repository-name <repo-name> --query 'imageIds[*].imageTag'


Output: Repository names + sorted image tags 🟢

──────────────────────────────────────────────

╔══════════════════════════════════════════════════╗
║ 🟢 EXERCISE 5: Python in Jenkins Pipeline ║
╚══════════════════════════════════════════════════╝

Goal: Jenkins job to fetch images from ECR and deploy to EC2.

Manual Preparation (once only):

# Start EC2 and install Docker
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Install Python & dependencies on Jenkins
sudo yum install python3 -y
sudo pip3 install boto3 paramiko

# Build & push Docker images to ECR
docker build -t my-app:1.0 ./app
docker build -t my-app:2.0 ./app
docker build -t my-app:3.0 ./app

aws ecr create-repository --repository-name my-app
aws ecr get-login-password --region us-east-1 | \
docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

docker tag my-app:1.0 <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/my-app:1.0
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/my-app:1.0
# Repeat for 2.0 and 3.0


Python/Jenkins Pipeline Command:

python exercise5_jenkins_pipeline.py


Pipeline Handles:

Fetch all images from ECR

User selects image in Jenkins UI

SSH into EC2

Run docker login

Start selected Docker container

Validate app is running 🟢

Output: Repository names + deployed image 🌐

──────────────────────────────────────────────

✅ Outcomes

By completing this project you can:

Automate AWS resources (subnets, IAM, EC2, ECR) using Python 🟢

Deploy and monitor apps in EC2 with Docker 🐳

Manage ECR images efficiently 📦

Build a Jenkins CI/CD pipeline with Python automation ⚡

──────────────────────────────────────────────

