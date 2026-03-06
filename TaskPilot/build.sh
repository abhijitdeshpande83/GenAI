#!/bin/bash

#Clear ._ files 
find . -type f -name '._*' -delete

#Variables
DOCKER_USER=${1}
IMG_TAG=${2}

#Build Docker Image
docker buildx build --platform linux/arm64 -t $DOCKER_USER/task-pilot:$IMG_TAG --push .