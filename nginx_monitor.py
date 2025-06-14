import boto3
import paramiko
import time
import requests
from datetime import datetime

# === Configuration ===
KEY_NAME = "my-app-key"
KEY_PATH = "/home/veek06/.ssh/id_rsa"
AMI_ID = "ami-01e27d968e66a4cf5"
INSTANCE_TYPE = "t3.micro"
SECURITY_GROUP_NAME = "myapp-sg"
SUBNET_ID = "subnet-0157047c68847fc5c"
INSTANCE_NAME = "my-app-server"
REGION = "eu-north-1"
VPC_ID = "vpc-0ec372439da5fd113"
MAX_FAILURES = 5

# === Set up Boto3 ===
ec2 = boto3.resource("ec2", region_name=REGION)
client = boto3.client("ec2", region_name=REGION)

# === Get security group ID using VPC filter ===
def get_security_group_id(name, vpc_id):
    try:
        response = client.describe_security_groups(
            Filters=[
                {'Name': 'group-name', 'Values': [name]},
                {'Name': 'vpc-id', 'Values': [vpc_id]}
            ]
        )
        groups = response['SecurityGroups']
        if not groups:
            raise Exception(f"Security group {name} not found in VPC {vpc_id}")
        return groups[0]['GroupId']
    except Exception as e:
        print(f"Failed to get security group ID for '{name}': {e}")
        print("Exiting due to security group error.")
        exit(1)

sg_id = get_security_group_id(SECURITY_GROUP_NAME, VPC_ID)

# === 1. Launch EC2 Instance ===
print("Launching new EC2 instance...")
instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MinCount=1,
    MaxCount=1,
    NetworkInterfaces=[{
        "DeviceIndex": 0,
        "SubnetId": SUBNET_ID,
        "AssociatePublicIpAddress": True,
        "Groups": [sg_id],
    }],
    TagSpecifications=[{
        "ResourceType": "instance",
        "Tags": [{"Key": "Name", "Value": INSTANCE_NAME}]
    }]
)[0]

print("Waiting for instance to start...")
instance.wait_until_running()
instance.reload()
public_ip = instance.public_ip_address
print(f"Instance is running with public IP: {public_ip}")

# === 2. Wait for SSH to be ready ===
print("Waiting 60 seconds for SSH to be ready...")
time.sleep(60)

# === 3. SSH into instance, install Docker, run Nginx ===
def ssh_connect(ip, key_path):
    key = paramiko.RSAKey.from_private_key_file(key_path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username="ec2-user", pkey=key)
    return ssh

print("Connecting to instance via SSH...")
ssh = ssh_connect(public_ip, KEY_PATH)

commands = [
    "sudo yum update -y",
    "sudo amazon-linux-extras install docker -y",
    "sudo service docker start",
    "sudo usermod -aG docker ec2-user",
    "docker pull nginx",
    "docker run -d -p 80:80 --name nginx nginx"
]

print("Installing Docker and starting Nginx...")
for cmd in commands:
    print(f"> {cmd}")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())

ssh.close()

# === 4. Monitor Nginx and restart if it fails ===
def monitor_nginx(ip):
    print("Monitoring Nginx...")
    fail_count = 0
    while True:
        try:
            r = requests.get(f"http://{ip}")
            print(f"[{datetime.now()}] HTTP check: {r.status_code}")
            if r.status_code != 200:
                fail_count += 1
            else:
                fail_count = 0
        except Exception as e:
            print(f"[{datetime.now()}] Connection error: {e}")
            fail_count += 1

        if fail_count >= MAX_FAILURES:
            print("Nginx failed 5 times, restarting container...")
            ssh = ssh_connect(ip, KEY_PATH)
            ssh.exec_command("docker restart nginx")
            ssh.close()
            fail_count = 0

        time.sleep(60)

monitor_nginx(public_ip)
