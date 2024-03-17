# Penn State Roar Collab - Notebook

## 2024.03.16
Restructed project following learning from Minneault2022 and other resources for proper file organization. Going to use consistent file hierarchy across all projects using https://github.com/patrickmineault/true-neutral-cookiecutter template

Wrote script to extract all ncore values from both systems evaluated (NiOconv2x2x2 and NiOconv4x2x2)

NCORE = 16 is used for all calculations for KPAR scaling testing as it was found to generally be the highest speed up for max #cores/node for all hardware considered.
- NOTE that only considering KPAR = # kpoints and KPAR = 1 for comparison purposes

## 2024.02.03
Started working on scaling testing for the ROAR Collab system, as I had not done this explicitly since we moved from the ROAR system. This is not meant to be comprehensive, but more so just to optimize my calculations moving forward as much as possible with simple rules

Note that ICDS has updated what the hardware is on the ROAR Collab system -->
![plot](./figures/hardware_roar_collab.png)

I confirmed that you can run up to 60 cores/node for basic, and 48 cores/node for standard.

Initial testing is just with MgO non-magnetic with PBE since this is quite cheap.


## 2024.02.05
Seems to be alot of instability in the calculation using 60 cores/node on basic, so I am going to stick with a max of 48 cores/node for both basic and standard cores moving forward

Going to revamp this since I have made a few mistakes trying to shift things around. 

Using 'full' kmesh for the NiO2x2x2 scaling (which is a kmesh of 3x3x3), going to redo all of these and delete older calculations since I am not sure if the 2x2x2 kmesh is applicable really
- the larger 128-atom supercell I will test in the future, but not for the time being since I need to finish this up and get doing other things

--> all submitted for both basic and standard, going to work on open as well for the time being since these may be different than the standard since they are 'icelake' cores

Will wait to get all of the data, but the 'icelake' processors seem to be MUCH faster than the default standard cores
- seems that a constraint can be added for standard core jobs as well to only use the icelake processors
--> to compare these, I will plot the total calculation time between the different type of processors
**> scontrol show node (shows the details of all the nodes you can use with slurm)**


## 2024.02.06
Starting to finally be able to come up with some general guidelines for my VASP calculations
- these will not be strictly true, but will rather be 'best overall' that do not require so much fiddling to get the calculations running properly

1. Unless performing small calculations (less than 50 atoms) and/or a very large number of calculations where you need to optimize the efficiency, *always use the max number of cores/node*
    - basic = 64 cores/node (3500MB/core max memory)
    - standard = 48 cores/node
    - if an out-of-memory (OOM) error occurs, you can lower the number of cores/node and increase the memory/core
2. NCORE = (cores/node) / 2
    - NCORE = cores/node showed decreased performance in all test cases
    - similar results found according to Yale HPC (https://docs.ycrc.yale.edu/clusters-at-yale/guides/vasp/)
3. KPAR = min(IBZKPTS, NODES)
    - I was unable to come up with a more detailed suggestion than this that I found online
    - KPAR should always be able to divide the number of kpoints evenly however
    - while this provides an easy rule, it is most definitely possible to acheive great performance with more fine tuning of KPAR on a per calculation type basis
        - ex. usually get a performance increase using KPAR = 2 for an even number of kpoints, even if only on one node
4. Use one node unless you have a *need* to use more
    - there is a fairly large dropoff of efficiency when greater than one node is used, so multi-node calculations should only be used for time-sensitive calculations, or extremely large calculations
        - these provide a good opportunity (and maybe the best opportunity) to use the burst allocation