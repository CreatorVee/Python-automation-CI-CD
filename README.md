#  Automation with Python – AWS & Jenkins  

## 🛠️ Tech Stack  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/) [![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/) [![EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)](https://aws.amazon.com/ec2/) [![ECR](https://img.shields.io/badge/AWS%20ECR-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ecr/) [![IAM](https://img.shields.io/badge/AWS%20IAM-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/iam/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/) [![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.linux.org/) [![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) [![Paramiko](https://img.shields.io/badge/Paramiko-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.paramiko.org/)  

---


This repository demonstrates **automation of AWS services** and **DevOps pipelines** using **Python** .  

**It contains exercises showcasing:** 

 AWS resource management  
 EC2 deployments  
 Docker containers  
 ECR repositories   
 Jenkins pipelines 

---

#  Problem & Solution

 ❌The Problem

- Managing AWS resources manually through the console or CLI is time-consuming and error-prone.

- Deploying applications often involves repeating the same setup steps (EC2 provisioning, Docker installs, security groups).

- Handling multiple services (EC2, ECR, IAM) and integrating them with Jenkins pipelines can quickly become complex.

✅ The Solution

- This repo provides a Python-driven automation toolkit that:

- Uses Boto3 and Paramiko to interact with AWS services programmatically.

- Demonstrates how to script EC2 provisioning, IAM management, ECR image handling, and container deployment.

- Integrates with Jenkins pipelines to enable continuous deployment.

- Reduces manual effort, ensures consistency, and accelerates DevOps workflows.

---

#  Overview of Exercises  

---

🟢 ***EXERCISE 1: Working with Subnets in AWS***

**Goal:**  
- Get all subnets in your default AWS region and print the subnet IDs.  

**Run Command:**  

python exercise1_subnets.py

AWS CLI Equivalent:

aws ec2 describe-subnets --query 'Subnets[*].SubnetId'


Output:
 Prints all subnet IDs in your AWS account.


---

# 🟢EXERCISE 2: Working with IAM in AWS

Goal:

List all IAM users.

Print each user’s name and last active time.

Show the most recently active user.

Run Command:

python exercise2_iam.py


AWS CLI Equivalent:

aws iam list-users


Output:
 List of users with PasswordLastUsed timestamps
 Most recently active user (ID + Name)

---

 # 🟢 EXERCISE 3: Automating EC2 + Docker + Nginx

Goal:

- Launch EC2 in default VPC.

- Install Docker on EC2.

- Start Nginx container.

- Open port 80.

- Monitor container health.

Run Command:

- python exercise3_ec2_nginx.py


AWS CLI / Commands:

-  Launch EC2 instance

aws ec2 run-instances --image-id <AMI_ID> --instance-type t2.micro \
--key-name <KEY_PAIR> --security-group-ids <SG_ID> --subnet-id <SUBNET_ID>


- Install Docker

ssh -i ~/.ssh/my-key.pem ec2-user@<EC2_PUBLIC_IP> \
"sudo amazon-linux-extras install docker -y; sudo service docker start; sudo usermod -a -G docker ec2-user"


-  Run Nginx container

ssh -i ~/.ssh/my-key.pem ec2-user@<EC2_PUBLIC_IP> "docker run -d -p 80:80 nginx"


Output:
✅ EC2 running
 Nginx accessible at http://<EC2_PUBLIC_IP>
🟢 Monitoring checks container health

---


 # 🟢EXERCISE 4: Working with ECR in AWS

Goal:

- List all ECR repositories.

- Print repository names.

- List image tags for one repository (newest first).

 Run Command:

- python exercise4_ecr.py


AWS CLI / Commands:

-  List all repositories

aws ecr describe-repositories


- List images for a repository

aws ecr list-images --repository-name <REPO_NAME> --query 'imageIds[*].imageTag'


Output:
 Repository names + sorted image tags 🟢

---

 # 🟢EXERCISE 5: Python in Jenkins Pipeline

Goal:
Create a Jenkins job to fetch images from ECR and deploy to EC2.

Manual Preparation (once only):

-  Start EC2 & install Docker

sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user


- Install Python & dependencies on Jenkins

sudo yum install python3 -y
sudo pip3 install boto3 paramiko


-  Build & push Docker images to ECR

docker build -t my-app:1.0 ./app
docker build -t my-app:2.0 ./app
docker build -t my-app:3.0 ./app


aws ecr create-repository --repository-name my-app
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com


docker tag my-app:1.0 <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/my-app:1.0
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/my-app:1.0



-  Repeat for versions 2.0 and 3.0.

**Run Pipeline Command**:

- python exercise5_jenkins_pipeline.py

---

# Short pipeline summary

Pipeline Handles:

 Fetch all images from ECR
 User selects image in Jenkins UI
 SSH into EC2 & run docker login
 Start selected Docker container
 Validate app is running


Output:
 **Repository names +  deployed image**
 ---
 # Photographic evidence
**Through Jnekins pipeline**
 
<img width="1369" height="820" alt="2025-05-21_02h40_21" src="https://github.com/user-attachments/assets/9cb8299f-07f8-440a-bf86-be0aabd39eaa" />



---

#  ✅Personal Study Notes & Learnings

Through this project, I learned:

- Boto3 Mastery: Writing Python scripts to manage AWS resources programmatically.

- IAM Security Awareness: Importance of tracking user activity and least-privilege access.

- Infrastructure as Code Mindset: Automating repetitive manual setups (EC2, Docker installs, security rules).

- Docker on EC2: Best practices for running and monitoring containers in the cloud.

- CI/CD Concepts with Jenkins: Using pipelines to pull ECR images, deploy to EC2, and validate running apps.

- Troubleshooting & Debugging: Handling IAM permission errors, SSH connection issues, and Docker failures.

DevOps Thinking: Viewing cloud resources as part of a repeatable, automated workflow rather than manual tasks.

 This repo serves as both a hands-on DevOps lab and a personal knowledge base for future reference.


---
# VISUAL PROCESS

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/714b6ed9-5249-47a9-abf8-875a9548ace4" />

---
