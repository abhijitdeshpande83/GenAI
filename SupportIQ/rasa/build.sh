#!/bin/bash
set -e  # Exit on error

#Variables
DOCKER_REPO_NAME1=${1}
IMG_TAG1=${2}
DOCKER_REPO_NAME2=${3}
IMG_TAG2=${4}


#Clear ._ files 
find . -type f -name '._*' -delete

#Build Docker image
docker buildx build --platform linux/amd64 -f Dockerfile.rasa -t $DOCKER_REPO_NAME1:$IMG_TAG1 --push .

docker buildx build --platform linux/amd64 -f Dockerfile.actions -t $DOCKER_REPO_NAME2:$IMG_TAG2 --push .

#Display message
echo "Images built and pushed successfully!"