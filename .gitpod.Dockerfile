FROM gitpod/workspace-full

USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && \
#     sudo apt-get install -yq bastet && \
#     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/

USER root
RUN sudo apt-get update
RUN sudo apt-get install -y docker
RUN sudo apt-get install -y chromium-browser

USER gitpod
# FROM python:3
RUN pip install -U pip
RUN pip install selenium
COPY entrypoint.sh entrypoint.sh
COPY app.py app.py
CMD entrypoint.sh
USER gitpod
