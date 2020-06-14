# Application of Newton's methods for solving load flow problems
## Introduction
  This repository was created to facilitate the reproducibility of the article with the same name. You can find the source code, with instructions for its use, versions of the article, and all the structures used until the time of publication. Along with the license taken by the authors.
The files are organized as follow:
* /Data - System files used;
* /deliver - ;
* /dev - Notes and codes used during this research;
* /figures - Figures used for the development of the work;

## Software and libraries used
Before attempting to reproduce the work, note how specifications used:
1. Programming Language: [Python 3.6](https://www.python.org/) 
2. Mathematical library:[Numpy](https://numpy.org/)
3. Graphic library:[Matplotlib](https://matplotlib.org/)
4. Documentation:[Jupyter Notebook](https://jupyter.org/)

### Installation instructions
The installation of the Python version is easily found on the website mentioned. In the case of libraries, you must use the terminal and the commands below for installation:
```
pip install numpy
pip install matplotlib
```
For the installation of the jupyter notebook it is possible to find the instructions on the [website](https://jupyter.org/install) or follow the steps below.It will be important for viewing and executing the reproducibility document.
```
pip install jupyterlab
pip install notebook
```

## Data
The data files are divided into three: system data, bar identification and time demand file. As the load flow problem will be solved, it will be necessary to first find the peak system power.
![Newton Fast Decoupled Flowchart ](figures/Demand.png)
![Newton Fast Decoupled Flowchart ](figures/Flowchart_FastDecopled.png)
