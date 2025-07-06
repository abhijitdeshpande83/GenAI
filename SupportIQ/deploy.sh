#!/bin/bash

#Variables
ECR_URI="720332985926.dkr.ecr.us-east-1.amazonaws.com"
REPO_NAME="intent-classifier-api"
DOCKER_REPO_NAME="abhijitdeshpande83/intent-classifier-api"
IMG_TAG=${1}

#Clear ._ files 
find . -type f -name '._*' -delete

#Build Docker Image
docker buildx build --platform linux/arm64 -t $DOCKER_REPO_NAME:$IMG_TAG --push .

#Pull image locally
docker pull $DOCKER_REPO_NAME:$IMG_TAG

#Tag image for ECR
docker tag $DOCKER_REPO_NAME:$IMG_TAG $ECR_URI/$REPO_NAME:$IMG_TAG

#Login to AWS
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URI

#Push image to ECR
docker push $ECR_URI/$REPO_NAME:$IMG_TAG

#Display message
echo "Image pushed to ECR"