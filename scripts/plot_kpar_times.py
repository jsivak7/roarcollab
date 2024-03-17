import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 400
plt.rcParams['figure.figsize'] = [6, 4]
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.25

hardware_types = ["bc_sapphirerapids", "sc_cascadelake", "sc_icelake"]
systems = ["NiOconv2x2x2", "NiOconv4x2x2", "NiOconv4x4x2"]

for system in systems:
    for hardware_type in hardware_types:
        data = pd.read_csv(f"../data/{system}/kpar_multinode/{hardware_type}.csv")
        print(data)
        plt.plot(data.num_nodes, data.kparnodes, label=hardware_type, marker='s')
    plt.xlabel("# nodes")
    plt.ylabel("cpu time (sec)")
    plt.title(f" {system} ({hardware_type})", weight='bold')
    plt.legend(title='KPAR', loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(alpha=0.1)
    plt.tight_layout()
    plt.savefig(f"../results/kpar_times_{system}.png")
    plt.clf()