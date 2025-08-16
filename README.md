# ⚡ Automation with Python – AWS & Jenkins

This repository demonstrates automation of AWS services and DevOps pipelines using Python.  
It contains exercises showcasing AWS resource management, EC2 deployments, Docker containers, ECR repositories, and Jenkins pipelines.

---

## 📖 Overview of Exercises

### 🟢 EXERCISE 1: Working with Subnets in AWS
**Goal:** Get all the subnets in your default AWS region and print the subnet IDs.
```bash
python exercise1_subnets.py
# ✔️ Output: Prints all subnet IDs in your AWS account


---


🟢 EXERCISE 2: Working with IAM in AWS

Goal:

Get all IAM users in your AWS account

Print each user’s name and last active time

Show the most recently active user

python exercise2_iam.py
# ✔️ Output:
# List of users with PasswordLastUsed timestamps
# The most recently active user (ID + Name)


---


🟢 EXERCISE 3: Automating EC2 + Docker + Nginx Monitoring

Goal:

Start an EC2 instance in the default VPC

Wait until the instance is fully initialized

Install Docker on the EC2 instance

Start an Nginx container

Open port 80 for browser access

Create a scheduled monitoring function that:

Sends requests to the Nginx app

Restarts the container if 5 consecutive failures occur

python exercise3_ec2_nginx.py
# ✔️ Output:
# EC2 instance running
# Nginx accessible at http://<EC2-Public-IP>
# Monitoring task automatically checking container health


---


🟢 EXERCISE 4: Working with ECR in AWS

Goal:

Get all repositories in Amazon ECR

Print repository names

Choose a repository and list all its image tags, sorted by date (newest first)

python exercise4_ecr.py

---

🟢 EXERCISE 5: Python in Jenkins Pipeline

Goal: Create a Jenkins job that fetches available images from ECR and deploys them to EC2.

Manual Preparation (once only):

Start an EC2 instance and install Docker

Install Python, pip, and dependencies in Jenkins

Build and push 3 Docker images (1.0, 2.0, 3.0) to ECR

Jenkins Pipeline Steps (automated):

Fetch all images from the ECR repo (Python script)

User selects an image in Jenkins UI (via input step)

Python script SSHs into EC2 server

Run docker login to authenticate with ECR

Start the selected Docker container on EC2

Validate that the app is running and accessible

python exercise5_jenkins_pipeline.py

# ✔️ Output:
# Repository names
# For one repo → sorted image tags (latest tag first)


 aws ec2 describe-subnets --query 'Subnets[*].SubnetId'
aws iam list-users
aws ecr describe-repositories
aws ecr list-images --repository-name <repo-name> --query 'imageIds[*].imageTag'


✅ Outcomes
By completing this project, you will:

Automate AWS resources (subnets, IAM, EC2, ECR) using Python (boto3)

Deploy and monitor apps in EC2 with Docker

Learn ECR image management

Build a Jenkins CI/CD pipeline with Python-based automation



