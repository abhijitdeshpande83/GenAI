#!/bin/bash

#Clear ._ files 
find . -type f -name '._*' -delete

#Variables
ECR_URI="720332985926.dkr.ecr.us-east-1.amazonaws.com"
DOCKER_USER=${1}
IMG_TAG=${2}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e979f2f (feat: add docker file)
#Docker login
docker login
=======
#Build Docker Image
docker buildx build --platform linux/arm64 -t $DOCKER_USER/task-pilot:$IMG_TAG --push .

#Pull image locally
docker pull $DOCKER_USER/task-pilot:$IMG_TAG 

#Tag image for ECR
docker tag $DOCKER_USER/task-pilot:$IMG_TAG $ECR_URI/task-pilot:$IMG_TAG
>>>>>>> 0648ecc (feat: add docker file)
<<<<<<< HEAD
=======
#Docker login
docker login
>>>>>>> d759b50 (feat: udpate docker file to execute lambda_function)
=======
>>>>>>> e979f2f (feat: add docker file)

#Login to AWS
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URI

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e979f2f (feat: add docker file)
#Build and push to both registries
docker buildx build --platform linux/amd64 --provenance=false \
        -t $DOCKER_USER/task-pilot:$IMG_TAG -t $ECR_URI/task-pilot:$IMG_TAG --push .
=======
#Push image to ECR
docker push $ECR_URI/task-pilot:$IMG_TAG
>>>>>>> 0648ecc (feat: add docker file)
<<<<<<< HEAD
=======
#Build and push to both registries
docker buildx build --platform linux/amd64 --provenance=false \
        -t $DOCKER_USER/task-pilot:$IMG_TAG -t $ECR_URI/task-pilot:$IMG_TAG --push .
>>>>>>> d759b50 (feat: udpate docker file to execute lambda_function)
=======
>>>>>>> e979f2f (feat: add docker file)

#Dispaly message
echo "------ Image pushed to ECR ------"