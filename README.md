# Application of Newton's methods for solving load flow problems
## Introduction
  This repository was created to facilitate the reproducibility of the article with the same name. You can find the source code, with instructions for its use, versions of the article, and all the structures used until the time of publication. Along with the license taken by the authors.
The files are organized as follow:
* /Data - System files used;
* /deliver - The executable paper and experiment's codes;
* /dev - Notes and codes used during this research;
* /figures - Figures used for the development of the work.
## Workflow
<img src="https://github.com/ReneJunior/final-project/blob/master/figures/WorkFlow.svg" width="100">

## Software and libraries used
Before attempting to reproduce the work, note the specifications used:

* Programming Language: [Python 3.6.5](https://www.python.org/downloads/release/python-365/) 
* Mathematical library: [Numpy](https://numpy.org/)
* Graphic library: [Matplotlib](https://matplotlib.org/)
* Documentation: [Jupyter Notebook](https://jupyter.org/)

### Installation instructions
The installation of the Python version is easily found on the website mentioned. In the case of libraries, you must use the terminal and the commands below for installation:
```
pip install numpy
pip install matplotlib
```
For the installation of the jupyter notebook it is possible to find the instructions on the [website](https://jupyter.org/install) or follow the steps below. It will be important for viewing and executing the reproducibility document.
```
pip install jupyterlab
pip install notebook
```

## Data
The data comes in an analysis carried out between half-hour intervals, repeating this process for three days (72 hours). As we will calculate the load flow for the transmission system, it will be necessary to perform a processing, for the collection of the peak, for each of the bars.

## Instructions for reproduction
As previously mentioned, the paper reproductive is located in the "deliver" folder. To run the experiment, follow the steps:
1. Have correctly performed all the installations previously requested.
2. Clone this repository to your desktop.
3. Boot the Jupyter Notebook from the terminal.
4. Navigate to the deliver folder and locate the preprocessing file called "Reproduction_procedures.ipynb", and run it.
5. After performing pre-processing, locate the file "Paper_code.ipynb".
6. Run all the codes inside, in order, and find the descriptor results in the article.

Ps: To best performance, clone the entire repository and follow the instructions previously mentioned.
