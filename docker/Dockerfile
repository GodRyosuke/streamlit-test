FROM python:3.10
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils git curl vim unzip openssh-client wget \
    build-essential cmake \
    libopenblas-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    sudo

RUN sudo apt-get upgrade -y && sudo apt-get update
RUN pip install --upgrade pip
RUN pip install streamlit