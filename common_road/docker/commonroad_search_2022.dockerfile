FROM continuumio/anaconda3

RUN conda create -n commonroad-py37 python=3.7
# add command to bashrc
RUN echo "conda activate commonroad-py37" > ~/.bashrc
# # link python3 to python3.7
# RUN rm /usr/bin/python3 && ln -sf python3.7 /usr/bin/python3
# install packages
RUN apt-get update && apt-get install \
    imagemagick -y \
    python3-dev -y \
    make \
    build-essential \
    m4 \
    socat \
    tk-dev -y

RUN bash -ic 'pip install jupyter tqdm imageio pyyaml ipywidgets networkx'

# create and switch to commonroad directory
WORKDIR /commonroad

# install requirements of commonroad-search
RUN git clone https://gitlab.lrz.de/tum-cps/commonroad-search.git && \
    cd commonroad-search && pip install -r requirements.txt
# switch back to commonroad directory
WORKDIR /commonroad

# set entrypoint for docker image
# == this is the safer option
# ENTRYPOINT bash -c "\
# conda activate commonroad-py37 &&\
# cd /commonroad-search/notebooks;\
# socat TCP-LISTEN:8888,fork TCP:127.0.0.1:9000 &\
# jupyter notebook --ip 0.0.0.0 --no-browser --allow-root --port 9000 "

# == this is the more convenient option
ENTRYPOINT bash -c "source activate commonroad-py37 &&\
    jupyter notebook --ip 0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''"
