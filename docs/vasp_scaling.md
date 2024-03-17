# VASP Scaling

## VASP General Scaling Rules
1. Use all of the cores/node available unless running simple 'small' calculations
2. A single node should be used in most routine cases, and *never* use more nodes than kpoints
3. KPAR should be the number of nodes (and a factor of kpoints)
4. NCORE should be 1/2 of the cores/node for a given CPU
5. *icelake* is faster than *cascadelake* (older hardware) for standard memory jobs, but must be called explictly with the *--constraint=icelake* tag in slurm submission script