# Application of Newton's methods for solving load flow problems
## Introduction
  This repository was created to facilitate the reproducibility of the article with the same name. You can find the source code, with instructions for its use, versions of the article, and all the structures used until the time of publication. Along with the license taken by the authors.
The files are organized as follow:
* `/Data` - System files used;
* `/deliver` - The executable paper and experiment's codes;
* `/dev` - Notes and codes used during this research;
* `/figures` - Figures used for the development of the work.

## Data
The data comes in an analysis carried out between half-hour intervals, repeating this process for three days (72 hours). As we will calculate the load flow for the transmission system, it will be necessary to perform a processing, for the collection of the peak, for each of the bars. The original versions of this work can be found at [IEEE14](https://labs.ece.uw.edu/pstca/pf14/pg_tca14bus.htm) and [Macedo](https://ieeexplore.ieee.org/document/7095593?denied=).

## Software and libraries used
Before attempting to reproduce the work, note the specifications used:

* Programming Language: [Python 3.6.5](https://www.python.org/downloads/release/python-365/) 
* Library
  - Mathematical: [Numpy](https://numpy.org/)
  - Graphic: [Matplotlib](https://matplotlib.org/)
* Documentation: [Jupyter Notebook](https://jupyter.org/)
* Distribution: [Oracle VM VirtualBox](https://www.virtualbox.org/)
* Code: [Git](https://git-scm.com/downloads)

## Distribution
This work has two ways to be reproduced, the first using a virtual machine and the second is by manually installing the programs.

### Virtual Machine

For this format, it is necessary to have installed the program [Oracle VM VirtualBox](https://www.virtualbox.org/). With the software installed, [download](https://drive.google.com/file/d/13OT-HSYDu1Z0tJ6tnEO1_fHR-GQa4rGO/view?usp=sharing) the virtual machine created to reproduce this work. The password required to access it is below.

Password = `1234`

With the virtual machine open and logged in, skip to step to the instruction *Instructions for reproduction* and follow the steps using the virtual machine.

### Manually Installing

For manual installation of tools and libraries, follow the instructions below.

#### Installation instructions 
The installation of the Python version is easily found on the website mentioned, but I was careful to select the option of "path" at the time of installation. If you have chosen to reproduce the work "manually", you must first check if your "pip install" is up to date, with the command
```
python -m pip install --upgrade pip
```
After updating the "pip install", you must restart the terminal, closing and opening it again. To start installing the libraries, go to the terminal and use the installation commands below:
```
pip install numpy
pip install matplotlib
```
For the installation of the jupyter notebook it is possible to find the instructions on the [website](https://jupyter.org/install) or follow the steps below. It will be important for viewing and executing the reproducibility document.
```
pip install jupyterlab
pip install notebook
```
Also install Git, to be able to clone this repository.

## Instructions for reproduction
As previously mentioned, the paper reproductive is located in the "deliver" folder. To run the experiment, follow the steps:
1. At the beginning of this repository, there is a green button described in the `clone`. Click on it and copy the generated link.
2. Open the terminal and type the combination below, replacing `***` with the copied link.
```
git clone ***
```
3. Boot the Jupyter Notebook from the terminal, with the command.
```
jupyter notebook
```
4. Navigate to the delivery folder called `final-project`, enter the folder, locate the pre-processing file called` / deliver` and look for the file `Reproduction_procedures.ipynb`, and run all the codes. In each code block, the text description of what is being done.
5. After performing pre-processing, locate the file `Paper_code.ipynb`, and do the same process for preprocessing. This file also describes what the code is doing
6. Run all the codes inside, in order, and find the descriptor results in the article.

To try to reproduce the computational time spent, necessary to find the point of operation of the system, it is suggested to use the codes that are located in the `dev` folder. The code files have the same names as the repeatability process described above and you must use python's IDLE, where it is installed together with the tool.

Ps: In the course of this work, some tests were performed using a machine with a Linux operating system. The reproduction process on this machine could not be completed, generating an error in the syntax code. If this occurs, try to use a virtual machine.
