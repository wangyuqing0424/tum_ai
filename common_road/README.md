# CommonRoad Search: Search-based Motion Planner with Motion Primitives

This is a programming exercise of the lecture **Fundamentals of Artificial Intelligence (IN2406)** delivered at the Department of Informatics, TUM. The task is to implement a heuristic function and/or a search algorithm with motion primitives to solve motion planning problems in [CommonRoad](https://commonroad.in.tum.de/). The following search algorithms are already implemented in our framework:

|Uninformed Search Algorithms &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Informed Search Algorithms &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
|-----------------------------|---------------------------|
|Breadth First Search <br /> Depth First Search <br /> Depth-limited Search <br />   Uniform Cost Search (Dijkstra)      |Greedy Best First Search <br />  A* Search                  |

The code is written in Python 3.7 and has been tested on Ubuntu 18.04. As the first step, clone this repository with:

```sh
$ git clone https://gitlab.lrz.de/tum-cps/commonroad-search.git
```

## :bookmark_tabs: Table of Contents
* [Ways to run](#arrow_forward-ways-to-run)
    * [Local installation](#computer-local-installation)
    * [Virtual machine (VM)](#cloud-virtual-machine)
    * [Docker](#whale-docker)
* [Getting Started](#chart_with_upwards_trend-getting-started)
* [Useful Tools](#wrench-useful-tools)
* [Questions & Answers](#grey_question-questions-and-answers)

## :arrow_forward: Ways to run

We provide 3 ways to run the software framework: **local installation**, **virtual machine (VM)**, or a **docker container**. Please refer to the table below for the supported platforms:

| Platform                | [Local](#computer-local-installation) &nbsp; &nbsp; | [VM](#cloud-virtual-machine) &nbsp; &nbsp; | [Docker](#whale-docker) &nbsp; &nbsp; |
| --------------------------- | ----------------- | ------------------| -----------------|
| **Ubuntu** 18.04/20.04      | :heavy_check_mark:| :heavy_check_mark:|:heavy_check_mark:|
| **MacOS** 10.13 or higher   | :heavy_check_mark:| :heavy_check_mark:<sup>2</sup>|:heavy_check_mark:|
| **Windows**                 | :heavy_multiplication_x:<sup>1</sup> | :heavy_check_mark:|:heavy_check_mark:|

<sup>1</sup>: _It is possible to run the CommonRoad software on Windows, however, the evaluation of submissions from Windows on our server
has not been tested. We therefore don't recommend a local installation on Windows for this exercise._

<sup>2</sup>: _The VM image has only been tested on MacOS with an Intel chip. **For Macs with M1 chip we can not provide a VM at the moment**. We therefore recommend the other two options._


## :computer: Local installation

_(skip this section if you intend to run the code in the virtual machine or in the docker container.)_

We recommend using [Anaconda](https://www.anaconda.com/) to manage your environment. A guide for managing python environments with Anaconda can be found [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

**Note for MacOS M1 Users: We recommend to use the 64-bit Anaconda Installer (graphical or command-line) instead of the Anaconda (M1) installer**

After installing Anaconda, create a new environment with:
``` sh
$ conda create -n commonroad-py37 python=3.7 -y
```

Here the name of the environment is called **commonroad-py37**. You may also change this name as you wish. In such case, don't forget to change it in the following commands as well. **Always activate** this environment before you do anything related:

```sh
$ conda activate commonroad-py37
```
Install `Jupyter Notebook` and supplementary modules:
```sh
$ conda install jupyter ipykernel ipywidgets sphinx scipy -y
```

With older versions of `Jupyter` you might need to run the following commands:
```sh
$ jupyter nbextension install --py widgetsnbextension --user
$ jupyter nbextension enable widgetsnbextension --user --py
```
Then, switch to the cloned commonroad-search folder on your machine with:
```sh
$ cd <your_local_address>/commonroad-search
```

And install the dependencies listed in `requirements.txt` with:
```sh
$ pip install -r requirements.txt
```

Optional: We install `Imagemagick` (only required for saving GIF animations of solutions) via:

```sh
# Ubuntu
$ sudo apt-get install imagemagick imagemagick-doc -y

# MacOS
$ brew install imagemagick
```

If you are using PyCharm, set **commonroad-py37** as environment in PyCharm as well in: _PyCharm -> Preferences/Settings -> Project -> Python Interpreter -> Add Interpreter -> Add Local Interpreter 
-> Conda Environment_


## :cloud: Virtual machine
A [VirtualBox](https://www.virtualbox.org/) image is available in which all the necessary packages have been installed. 
The virtual machine image can be downloaded via [this](https://syncandshare.lrz.de/getlink/fiT5GTiqWNogNVWQ3Dya9w/) link. 
The downloading and the default login passwords are both `commonroad`. 
You can update to the latest commit with typing the command in the `commonroad-search/` folder:

```sh
$ git pull
```


## :whale: Docker
A docker file and a docker image is available if you wish to run the code in a docker container. 
Refer to `docker/README.md` for further instructions. Minimum system requirements are listed [here](https://docs.docker.com/desktop/).




## :chart_with_upwards_trend: Getting Started

Full description of the exercise is provided in `exercise_guide.pdf`. 

To proceed with the tutorials, open a terminal in `commonroad-search/` folder, and launch Jupyter Notebook kernel with:

```shell
$ jupyter notebook
```

In the pop-up tab (or: open http://localhost:9000/ if ran with docker, otherwise http://localhost:8888/, in the explorer), navigate to `tutorials/` and follow the tutorials one by one. After that, you may proceed with the exercise itself (see exercise guide for more details).

## :wrench: Useful Tools
If you are new here, it's worth to take a look at the following tools:
- [Jupyter Notebook](): an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. An introduction can be found [here](https://realpython.com/jupyter-notebook-introduction/).
- [PyCharm](https://www.jetbrains.com/pycharm/): one of the best Python IDEs on the market. It is free for students. A tutorial video can be seen [here](https://www.youtube.com/watch?v=56bPIGf4us0&list=PLX4nwNAsU8OJUuLvmUvxpg-bdPqYVODGU).
- [GitKraken](https://www.gitkraken.com/): a powerful and elegant multi-platform graphical interface for Git, as an alternative to the command line. It is free for students (with GitHub account). An introduction to GitKraken can be found [here](https://www.youtube.com/c/Gitkraken/playlists).
## :grey_question: Questions and Answers 

If you encountered any problem, please raise it in the [CommonRoad Forum](https://commonroad.in.tum.de/forum/) so that other students can also benefit from the answers to your questions.
