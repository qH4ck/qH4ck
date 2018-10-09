FROM ubuntu:latest

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update && apt-get -y upgrade

# Basic
RUN mkdir /home/q4hck
RUN apt-get install -y git sudo
WORKDIR "/home/qh4ck"
# Snail :)
RUN git clone https://github.com/samueleunipi/snail
WORKDIR "/home/qh4ck/snail"
RUN bash install.sh
RUN rm /root/.snail/theme.snail /root/.snail/greetings.snail
COPY ./theme.snail /root/.snail/theme.snail
COPY ./greetings.snail /root/.snail/greetings.snail

# Miscellaneous
RUN apt-get install -y binwalk

