FROM ubuntu:22.04

LABEL maintainer="Sushree Subhadra Sahoo"

ENV DEBIAN_FRONTEND=noninteractive

# Base tools
RUN apt-get update && apt-get install -y \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# SDL + Python Dev Tools
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev \
    python3-venv x11-apps \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libsm6 libxext6 libxrender1 libx11-6 \
    libglib2.0-0 libgl1-mesa-glx \
    && apt-get clean

# Symlink python -> python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Python Libraries
RUN pip3 install --no-cache-dir pygame django

WORKDIR /app

CMD ["bash"]

