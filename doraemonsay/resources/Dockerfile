FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN echo "# Colour the bash prompt" >> ~/.bashrc && \
    echo "PS1='\${debian_chroot:+(\$debian_chroot)}\\[\033[01;32m\\]\\u@\\H\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ '" >> ~/.bashrc && \
    echo "" >> ~/.bashrc

RUN apt-get update && \
    apt-get install python3-pip git iproute2 ffmpeg curl unzip libgl1 -y

RUN python3 -m pip install -U pip

RUN apt-get -qq purge "python2.7*" -y

# Cleanup apt, and make python3 the default python
RUN apt-get -qq autoremove -y  && apt clean && \
    rm -f /usr/bin/python && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/* && rm -rf ~/.cache/pip

WORKDIR /workspace

ADD . /workspace

