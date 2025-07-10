# Base image
FROM ubuntu:22.04

LABEL maintainer="Sushree Subhadra Sahoo"

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system packages
RUN apt-get update && apt-get install -y \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    wget \
    tzdata \
    python3 python3-pip python3-dev python3-venv \
    x11-apps \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libsm6 libxext6 libxrender1 libx11-6 \
    libglib2.0-0 libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Symlink `python` to `python3`
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Python libraries
RUN pip3 install --no-cache-dir \
    flask \
    pygame \
    jupyter \
    jupyterlab

# COPY requirements.txt .
# RUN pip install -r requirements.txt

RUN pip install pandas

# Set working directory
WORKDIR /app

# Copy startup script and make executable
COPY start.sh ./start.sh
RUN chmod +x ./start.sh

# Expose Flask (5000) and Jupyter (8888) ports
EXPOSE 5000
EXPOSE 8888

# Use bash to run the script (recommended)
CMD ["bash", "./start.sh"]