import requests
import argparse

def validate_app(ec2_ip):
    url = f'http://{ec2_ip}/health'  # replace with your app's real health endpoint if different
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Deployment validated: app is running!")
        else:
            print(f"App returned status code: {response.status_code}")
    except Exception as e:
        print(f"Validation failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ec2-ip', required=True)
    args = parser.parse_args()

    validate_app(args.ec2_ip)
