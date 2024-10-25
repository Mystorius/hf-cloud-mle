#!/bin/bash

# Variables (modify these for your environment)
IMAGE_NAME="hf-transformers-cuda"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Test the Docker image locally with or without GPU
if docker run --gpus=all $IMAGE_NAME; then
    echo "Docker container ran successfully with GPU support."
else
    echo "GPU support not available. Running without GPU..."
    docker run $IMAGE_NAME
fi