[![CI](https://github.com/nogibjj/706_Week01_YL/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/706_Week01_YL/actions/workflows/cicd.yml)

# 706_Week09_YL

This repository includes the main tasks for Week 1:

* `Makefile` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.
* `.devcontainer` includes a Dockerfile and `devcontainer.json`. The `Dockerfile` within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.
* `Workflows` includes GitHub Actions, which contain configuration files for setting up automated build, test, and deployment pipelines for your project.
* `.gitignore` is used to specify which files or directories should be excluded from version control when using Git.
* `README.md` is the instruction file for the readers.
* `lib.py` is a Python file that contains the main function.
* `test_lib.py`  is a test file for `lib.py` that can successfully run in IDEs.
* `requirements.txt` is to specify the dependencies (libraries and packages) required to run the project.
* `script.py`
* `test_script.py`
* `week09.ipynb`


## Project description
* Set up a cloud-hosted Jupyter Notebook and perform data manipulation: I utilized the online 2018 world cup prediction dataset to perform data manipulate on a cloud-hosted notebook.

## Google Colab link
https://colab.research.google.com/drive/1fus8xRiPSJ7X7A_9RsfepjNb85l1Vzps?usp=sharing

## Project environment

* Use codespace for scripting
* Container built in `devcontainers` and virtual environment activated via `requirements.txt`
* Open Google Colab for reading the dataset and scripting in Python

## Check format & errors

1. make format

2. make lint

3. make test