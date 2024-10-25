# Use an NVIDIA base image with CUDA 11.8 (or newer) and cuDNN support, compatible with H100 GPUs
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Set up environment variables for Python and CUDA
ENV DEBIAN_FRONTEND=noninteractive

# Install essential dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Hugging Face Transformers and Accelerate for GPU support
RUN pip3 install --upgrade pip \
    && pip3 install transformers accelerate torch

# (Optional) Copy project files to container, here would be your project files
COPY . /app
WORKDIR /app

# Test script to ensure CUDA and PyTorch are working with Hugging Face
COPY test_script.py /app/test_script.py

# Run the test script when the container starts
CMD ["python3", "test_script.py"]