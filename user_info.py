import boto3
from datetime import datetime

# Create IAM client
iam = boto3.client('iam')

# Get list of users
response = iam.list_users()

most_recent_user = None
most_recent_time = None

print("IAM Users and Last Active Time:")
print("-" * 40)

for user in response['Users']:
    username = user['UserName']
    user_id = user['UserId']
    last_used = user.get('PasswordLastUsed')

    if last_used:
        print(f"User: {username}, Last Active: {last_used}")
        if not most_recent_time or last_used > most_recent_time:
            most_recent_time = last_used
            most_recent_user = {'UserName': username, 'UserId': user_id, 'LastUsed': last_used}
    else:
        print(f"User: {username}, Last Active: Never")

print("\nMost Recently Active User:")
print("-" * 40)
if most_recent_user:
    print(f"User ID: {most_recent_user['UserId']}")
    print(f"Username: {most_recent_user['UserName']}")
    print(f"Last Active: {most_recent_user['LastUsed']}")
else:
    print("No users have logged in yet.")
