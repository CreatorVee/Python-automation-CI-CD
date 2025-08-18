# ⚡ Automation with Python – AWS & Jenkins  

This repository demonstrates **automation of AWS services** and **DevOps pipelines** using **Python** 🐍.  

It contains exercises showcasing:  
✅ AWS resource management  
✅ EC2 deployments  
✅ Docker containers 🐳  
✅ ECR repositories 📦  
✅ Jenkins pipelines ⚙️  

---

## 🛠️ Tech Stack  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)  
![EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)  
![ECR](https://img.shields.io/badge/AWS%20ECR-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)  
![IAM](https://img.shields.io/badge/AWS%20IAM-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)  
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)  
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)  
![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)  
![Paramiko](https://img.shields.io/badge/Paramiko-3776AB?style=for-the-badge&logo=python&logoColor=white)  

<div style="border-top: 4px solid black; margin: 30px 0;"></div>

---

# 📖 Overview of Exercises  

---

╔══════════════════════════════════════════════════════╗  
║ 🟢 **EXERCISE 1: Working with Subnets in AWS** 🌐     ║  
╚══════════════════════════════════════════════════════╝  

**Goal:**  
- Get all subnets in your default AWS region and print the subnet IDs.  

**Run Command:**  
```bash
python exercise1_subnets.py

AWS CLI Equivalent:

aws ec2 describe-subnets --query 'Subnets[*].SubnetId'


Output:
📜 Prints all subnet IDs in your AWS account.

══════════════════════════════════════════════════════╗
║ 🟢 EXERCISE 2: Working with IAM in AWS 🔐 ║
╚══════════════════════════════════════════════════════╝

Goal:

List all IAM users.

Print each user’s name and last active time.

Show the most recently active user.

Run Command:

python exercise2_iam.py


AWS CLI Equivalent:

aws iam list-users


Output:
👤 List of users with PasswordLastUsed timestamps
🏆 Most recently active user (ID + Name)

╔══════════════════════════════════════════════════════╗
║ 🟢 EXERCISE 3: Automating EC2 + Docker + Nginx 🖥️ ║
╚══════════════════════════════════════════════════════╝

Goal:

Launch EC2 in default VPC.

Install Docker on EC2.

Start Nginx container.

Open port 80.

Monitor container health.

Run Command:

python exercise3_ec2_nginx.py


AWS CLI / Commands:

➡️ Launch EC2 instance

aws ec2 run-instances --image-id <AMI_ID> --instance-type t2.micro \
--key-name <KEY_PAIR> --security-group-ids <SG_ID> --subnet-id <SUBNET_ID>


➡️ Install Docker

ssh -i ~/.ssh/my-key.pem ec2-user@<EC2_PUBLIC_IP> \
"sudo amazon-linux-extras install docker -y; sudo service docker start; sudo usermod -a -G docker ec2-user"


➡️ Run Nginx container

ssh -i ~/.ssh/my-key.pem ec2-user@<EC2_PUBLIC_IP> "docker run -d -p 80:80 nginx"


Output:
✅ EC2 running
🌍 Nginx accessible at http://<EC2_PUBLIC_IP>
🟢 Monitoring checks container health

╔══════════════════════════════════════════════════════╗
║ 🟢 EXERCISE 4: Working with ECR in AWS 📦 ║
╚══════════════════════════════════════════════════════╝

Goal:

List all ECR repositories.

Print repository names.

List image tags for one repository (newest first).

Run Command:

python exercise4_ecr.py


AWS CLI / Commands:

➡️ List all repositories

aws ecr describe-repositories


➡️ List images for a repository

aws ecr list-images --repository-name <REPO_NAME> --query 'imageIds[*].imageTag'


Output:
📦 Repository names + sorted image tags 🟢

╔══════════════════════════════════════════════════════╗
║ 🟢 EXERCISE 5: Python in Jenkins Pipeline ⚙️ ║
╚══════════════════════════════════════════════════════╝

Goal:
Create a Jenkins job to fetch images from ECR and deploy to EC2.

Manual Preparation (once only):

➡️ Start EC2 & install Docker

sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user


➡️ Install Python & dependencies on Jenkins

sudo yum install python3 -y
sudo pip3 install boto3 paramiko


➡️ Build & push Docker images to ECR

docker build -t my-app:1.0 ./app
docker build -t my-app:2.0 ./app
docker build -t my-app:3.0 ./app

aws ecr create-repository --repository-name my-app
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

docker tag my-app:1.0 <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/my-app:1.0
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/my-app:1.0


➡️ Repeat for versions 2.0 and 3.0.

Run Pipeline Command:

python exercise5_jenkins_pipeline.py


Pipeline Handles:
🔍 Fetch all images from ECR
👨‍💻 User selects image in Jenkins UI
🔑 SSH into EC2 & run docker login
▶️ Start selected Docker container
🟢 Validate app is running

Output:
📦 Repository names + 🚀 deployed image

✅ Outcomes

By completing this project you will:

⚡ Automate AWS resources (Subnets, IAM, EC2, ECR) using Python

🐳 Deploy and monitor apps in EC2 with Docker

📦 Manage ECR images efficiently

⚙️ Build a Jenkins CI/CD pipeline with Python automation



