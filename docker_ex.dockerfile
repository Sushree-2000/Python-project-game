# Use the official lightweight Python image
FROM python:3.13-slim

# Install Git, Pygame dependencies, and build tools
RUN apt-get update && apt-get install -y \
    git \
    python3-dev \
    build-essential \
    libsdl2-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libsdl1.2-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    && apt-get clean

# Install Pygame
RUN pip install pygame

# Set working directory
WORKDIR /app

# Optionally copy local files in
# COPY . .

# Default command: interactive shell
CMD ["bash"]
