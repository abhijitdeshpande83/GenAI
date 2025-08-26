#!/bin/bash
set -e  # Exit on error

#Variables
DOCKER_USER=abhijitdeshpande83
DOCKER_REPO_NAME1=rasa_server
IMG_TAG1=${1}
DOCKER_REPO_NAME2=rasa_actions
IMG_TAG2=${2}


#Clear ._ files 
find . -type f -name '._*' -delete

#Build Docker image
docker buildx build --platform linux/amd64 -f Dockerfile.rasa -t $DOCKER_USER/$DOCKER_REPO_NAME1:$IMG_TAG1 --push .

docker buildx build --platform linux/amd64 -f Dockerfile.actions -t $DOCKER_USER/$DOCKER_REPO_NAME2:$IMG_TAG2 --push .

#Display message
echo "Images built and pushed successfully!"