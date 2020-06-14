# Application of Newton's methods for solving load flow problems
## Introduction
  This repository was created to facilitate the reproducibility of the article with the same name. You can find the source code, with instructions for its use, versions of the article, and all the structures used until the time of publication. Along with the license taken by the authors.
The files are organized as follow:
* /Data - System files used;
* /deliver - The executable paper and experiment's codes;
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
This second part is where the pre-processing of the initial data will be performed. The file "PC.txt" and "QC.txt" have the data of 14 expensive bars, found varying in time. Each measurement is equivalent to a reading taken every half hour, for 72 hours, totaling 144 data per bar. For the calculations, the absolute peak demand data will be used, so the code below accomplishes this, and writing this data in a new file called "Data_Node.txt".

## Instructions for reproduction
