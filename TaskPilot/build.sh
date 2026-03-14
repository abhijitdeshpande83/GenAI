#!/bin/bash

#Clear ._ files 
find . -type f -name '._*' -delete

#Variables
ECR_URI="720332985926.dkr.ecr.us-east-1.amazonaws.com"
DOCKER_USER=${1}
IMG_TAG=${2}

#Build Docker Image
docker buildx build --platform linux/arm64 -t $DOCKER_USER/task-pilot:$IMG_TAG --push .

#Pull image locally
docker pull $DOCKER_USER/task-pilot:$IMG_TAG 

#Tag image for ECR
docker tag $DOCKER_USER/task-pilot:$IMG_TAG $ECR_URI/task-pilot:$IMG_TAG

#Login to AWS
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URI

#Push image to ECR
docker push $ECR_URI/task-pilot:$IMG_TAG

#Dispaly message
echo "------ Image pushed to ECR ------"