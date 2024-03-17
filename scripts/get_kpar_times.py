# only considering kpar = 1 and kpar = #nodes

from psu_roarcollab.vasp_outputs import get_total_cpu_time
import pandas as pd

hardware_types = ["bc_sapphirerapids", "sc_icelake", "sc_cascadelake"]
systems = ["NiOconv2x2x2", "NiOconv4x2x2", "NiOconv4x4x2"]
kpars = [1, "nodes"]

print(f"\nGetting CPU times for KPAR values...")

for system in systems:
    calcpath = f"../calcs/{system}/kpar_multinode"
    datapath = f"../data/{system}/kpar_multinode"

    print(f"\n--- {system} ---")

    if system == "NiOconv2x2x2":
        nodes = [1, 2, 3, 6]
    elif system == "NiOconv4x2x2":
        nodes = [1, 2, 8]
    elif system == "NiOconv4x4x2":
        nodes = [1, 2, 6]
    
    for hardware_type in hardware_types:
        print(f"\n{hardware_type} ->")

        data = {"num_nodes": nodes}

        for kpar in kpars:
            times = []

            for node in nodes:
                outcarpath = f"{calcpath}/{hardware_type}/kpar{kpar}/{node}node/OUTCAR"
                cputime = get_total_cpu_time(outcarpath)
                print(f"kpar = {kpar}, node = {node}\t-> {cputime}\tsec")
                times.append(cputime)
            data[f"kpar{kpar}"] = times
        
        df_times = pd.DataFrame(data)
        print(f"{df_times}")
        df_times.to_csv(f"{datapath}/{hardware_type}.csv", index=False)

print("\nSuccess!\n")
