# Data
In this folder is found the system data used to perform the tests for this work. The original versions of this work can be found at [IEEE14](https://labs.ece.uw.edu/pstca/pf14/pg_tca14bus.htm) and [Macedo](https://ieeexplore.ieee.org/document/7095593?denied=).

The file named "[System_IEEE_14bus_branch.txt](https://github.com/ReneJunior/final-project/blob/master/Data/System_IEEE_14bus_branch.txt)" presents the data of the system branches, with the physical characteristics of the line, such as resistance, impedance and shunting capacitors. The files "[PC.txt](https://github.com/ReneJunior/final-project/blob/master/Data/PC.txt)" and "[QC.txt](https://github.com/ReneJunior/final-project/blob/master/Data/QC.txt)", present the collected data, of the demand of the system bars. The file "[System_IEEE_14bus_node.txt](https://github.com/ReneJunior/final-project/blob/master/Data/System_IEEE_14bus_node.txt)" shows the data of the bars, indicating which will be the reference bar, load bars and generators.

With the calculated pre-processing, the file 'Data_Node.txt' appears, where the absolute peak values of demand varying in time can be found.
To simulate other systems, you can go to the database, where it was taken from the IEEE14 system and format the data in the same way as in the `System_IEEE_14bus_branch.txt`,` System_IEEE_14bus_node.txt` and `Data_Node.txt`
