from psu_roarcollab.vasp_outputs import get_total_cpu_time
import pandas as pd

hardware_types = ["bc_sapphirerapids", "sc_icelake", "sc_cascadelake"]
systems = ["NiOconv2x2x2", "NiOconv4x2x2"]

print(f"\nGetting CPU times for NCORE values...")

for system in systems:
    calcpath = f"../calcs/{system}/ncore_singlenode"
    datapath = f"../data/{system}/ncore_singlenode"

    print(f"\n--- {system} ---")

    for hardware_type in hardware_types:
        print(f"\n{hardware_type} ->")

        ncores = [1, 8, 16, 24, 32, 48, 64]
        cores = [1, 8, 16, 24, 32, 48, 64]

        if hardware_type[0:2] == "sc": # sc only have max of 48 cores/node
            ncores = ncores[:-1]
            cores = cores[:-1]

        data = {"num_cores": cores}

        for ncore in ncores:
            times = []

            for core in cores:
                outcarpath = f"{calcpath}/{hardware_type}/ncore{ncore}/{core}core/OUTCAR"
                cputime = get_total_cpu_time(outcarpath)
                print(f"ncore = {ncore}, core = {core}\t-> {cputime}\tsec")
                times.append(cputime)
            data[f"ncore{ncore}"] = times
        
        df_times = pd.DataFrame(data)
        print(f"{df_times}")
        df_times.to_csv(f"{datapath}/{hardware_type}.csv", index=False)