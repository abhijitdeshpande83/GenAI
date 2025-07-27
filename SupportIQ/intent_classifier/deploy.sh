#!/bin/bash

#Variables
ECR_URI="720332985926.dkr.ecr.us-east-1.amazonaws.com"
ECR_REPO_NAME=${1}
DOCKER_FILE_NAME=${2}
DOCKER_REPO_NAME=${3}
IMG_TAG=${4}

#Clear ._ files 
find . -type f -name '._*' -delete

#Build Docker Image
docker buildx build --platform linux/arm64 -f $DOCKER_FILE_NAME -t $DOCKER_REPO_NAME:$IMG_TAG --push .

#Pull image locally
docker pull $DOCKER_REPO_NAME:$IMG_TAG

#Tag image for ECR
docker tag $DOCKER_REPO_NAME:$IMG_TAG $ECR_URI/$ECR_REPO_NAME:$IMG_TAG

#Login to AWS
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URI

#Push image to ECR
docker push $ECR_URI/$ECR_REPO_NAME:$IMG_TAG

#Display message
echo "Image pushed to ECR"