#!/bin/bash
# xhost +local:docker

# docker run -it --rm \
#   -e DISPLAY=$DISPLAY \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
#   -v "$(pwd)":/app \
#   --name my-python-dev \
#   my-python-dev-image


xhost +local:docker
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$(pwd)":/app \
  my-python-dev



# # If you want to keep the container running between sessions:
# xhost +local:docker
# docker run -it \
#   -e DISPLAY=$DISPLAY \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
#   -v "$(pwd)":/app \
#   --name my-python-container \
#   my-python-dev

# # Then next time, instead of starting a new one, just:
# docker start -ai my-python-container