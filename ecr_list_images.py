import boto3

# Initialize ECR client
ecr = boto3.client('ecr', region_name='eu-north-1')  # Set correct region

# 1. Get all repositories
response = ecr.describe_repositories()
repositories = response['repositories']

print("Repositories found:")
for repo in repositories:
    print("-", repo['repositoryName'])

# 2. Choose specific repository
repo_name = 'tf-python'

# 3. Try to list image details
try:
    image_response = ecr.describe_images(repositoryName=repo_name)

    if not image_response['imageDetails']:
        print(f"\nNo images found in repository '{repo_name}'.")
    else:
        images = [
            {
                'tag': detail.get('imageTags', ['<untagged>'])[0],
                'pushedAt': detail['imagePushedAt']
            }
            for detail in image_response['imageDetails']
            if 'imageTags' in detail
        ]

        # Sort images by most recent
        sorted_images = sorted(images, key=lambda x: x['pushedAt'], reverse=True)

        print(f"\nImage tags in '{repo_name}' (most recent first):")
        for img in sorted_images:
            print(f"{img['tag']} - {img['pushedAt']}")

except ecr.exceptions.RepositoryNotFoundException:
    print(f"\nRepository '{repo_name}' not found.")
