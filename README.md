# psu-roarcollab

Information about the Penn State Roar Collab HPC. Useful for tracking Sinnott group and MRSEC IRG2 allocation balances, available hardware, and VASP scaling performance.

## Allocation Balances
![plot](/results/alloc_balances.png)

## Available Hardware
|cpu codename       |memory type|cores/node |memory/node (gb)   |memory/core (gb)   |partitions             |
|:---               |:---       |:---       |:---               |:---               |:---                   |
|*sapphirerapids*   |basic      |64         |255                |3.98               |open, sla-prio, burst  |
|*icelake*          |standard   |48         |500                |10.42              |open, sla-prio, burst  |
|*cascadelake*      |standard   |48         |350                |7.29               |open, sla-prio, burst  |

The 'icelake' standard cores should be used preferably over the 'cascadelake' in most cases for VASP calculations, as the NiO scaling calculations were almost always less time when using the 'icelake' standard cores:
![plot](./results/kpar_times_allNiO.png)

Some research on the different Intel codenames would indicate that the 'icelake' series is newer than 'cascadelake', so these findings make sense. The 'icelake' hardware can be called using `--constraint = icelake` in the slurm submission script.

## VASP General Scaling Rules on PSU Roar Collab
1. Use all of the cores/node available unless running relatively 'small' calculations (< ~20 atoms)
2. A single node should be used in most routine cases, and *never* use more nodes than kpoints
3. KPAR should be the number of nodes (and a factor of kpoints)
4. NCORE performance is general best for `NCORE = 16` and can be used for all hardware types