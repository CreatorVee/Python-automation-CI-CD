import paramiko
import argparse
import os  # <- needed to read environment variables

def deploy_image(ec2_ip, ssh_key_path, image_tag):
    ecr_url = os.environ.get("ECR_URL")  # get ECR URL from environment
    if not ecr_url:
        raise ValueError("ECR_URL environment variable is not set")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ec2_ip, username='ec2-user', key_filename=ssh_key_path)

    commands = [
        f'aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin {ecr_url}',
        f'docker pull {ecr_url}/tf-python:{image_tag}',
        f'docker stop tf-python-container || true',
        f'docker rm tf-python-container || true',
        f'docker run -d --name tf-python-container -p 80:80 {ecr_url}/tf-python:{image_tag}'
    ]

    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        print(stderr.read().decode())

    ssh.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ec2-ip', required=True)
    parser.add_argument('--ssh-key', required=True)
    parser.add_argument('--image-tag', required=True)
    args = parser.parse_args()

    deploy_image(args.ec2_ip, args.ssh_key, args.image_tag)

