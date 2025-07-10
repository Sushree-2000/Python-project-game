#!/bin/bash
# xhost +local:docker

# docker run -it --rm \
#   -e DISPLAY=$DISPLAY \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
#   -v "$(pwd)":/app \
#   --name my-python-dev \
#   my-python-dev-image


# xhost +local:docker
# docker run -it --rm \
#   -e DISPLAY=$DISPLAY \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
#   -v "$(pwd)":/app \
#   python-proj-game-ml



xhost +local:docker

docker run -it --rm \
  --name game_flask_server \
  -e DISPLAY=$DISPLAY \
  --net=host \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$(pwd)":/app \
  python-proj-game-ml



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


# to build docker
# docker build -t python-proj-game-ml .


# to start running the container

# docker run -it -p 5000:5000 -p 8888:8888 -v /home/sushreesubhadrasahoo/Documents/my_things/Python-project-game:/app -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --name my_game_ml_dev python-proj-game-ml bash
# docker start -ai my_game_ml_dev  (this is to start the container)
# jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root   (to run the jupyter server)