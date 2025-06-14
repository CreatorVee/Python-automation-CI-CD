import boto3

# Create an EC2 client using the default region
ec2 = boto3.client('ec2')

# Get all subnets
response = ec2.describe_subnets()

# Print the subnet IDs
print("Subnet IDs in your default region:")
for subnet in response['Subnets']:
    print(subnet['SubnetId'])
