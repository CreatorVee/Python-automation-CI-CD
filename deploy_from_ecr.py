import boto3
import paramiko
import requests

# Config
region = "eu-north-1"
repo_name = "tf-python"
ec2_host = "YOUR_EC2_PUBLIC_IP"
ec2_user = "ubuntu"
pem_file = "/path/to/your-key.pem"

# 1. Get ECR image tags
ecr = boto3.client('ecr', region_name=region)
images = ecr.describe_images(repositoryName=repo_name)['imageDetails']
tags = sorted([img['imageTags'][0] for img in images if 'imageTags' in img])

print("Available image tags:")
for i, tag in enumerate(tags):
    print(f"{i + 1}. {tag}")

# 2. Ask user which tag
choice = int(input("Select an image tag by number: ")) - 1
selected_tag = tags[choice]
print(f"Selected: {selected_tag}")

# 3. SSH to EC2 using Paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ec2_host, username=ec2_user, key_filename=pem_file)

# 4. Docker login
cmds = [
    f"aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {ecr.meta.endpoint_url.replace('https://', '')}",
    f"docker pull 353545917196.dkr.ecr.eu-north-1.amazonaws.com/{repo_name}:{selected_tag}",
    f"docker run -d -p 80:80 353545917196.dkr.ecr.eu-north-1.amazonaws.com/{repo_name}:{selected_tag}"
]

for cmd in cmds:
    print(f"Running: {cmd}")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode(), stderr.read().decode())

ssh.close()

# 5. Validate
try:
    r = requests.get(f"http://{ec2_host}")
    if r.status_code == 200:
        print("App deployed and reachable!")
    else:
        print(f"App responded with code: {r.status_code}")
except Exception as e:
    print(f"Error reaching app: {e}")
