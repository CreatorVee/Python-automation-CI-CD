import boto3
import operator

client = boto3.client('ecr', region_name='eu-north-1')

repository_name = "tf-python"

# Get image details
response = client.describe_images(repositoryName=repository_name)

# Sort by pushedAt
images = sorted(
    response['imageDetails'],
    key=lambda x: x.get('imagePushedAt', ''),
    reverse=True
)

# Print image tags
print("Available image tags:")
tags = []
for img in images:
    if 'imageTags' in img:
        for tag in img['imageTags']:
            tags.append(tag)
            print(tag)

# Prompt user to choose one
selected = input("\nSelect image tag to deploy: ")

# Write selected tag to file
with open("selected_tag.txt", "w") as f:
    f.write(selected)
