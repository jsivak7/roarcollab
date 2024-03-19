def add_legend():
    plt.plot([], [], linestyle='', marker='^', color='blue', alpha=0.8, label = '# nodes')
    plt.plot([], [], linestyle='', marker='o', color='red', alpha=0.8, label='default (1)')
    plt.plot([], [], linestyle='-', color='black', alpha=0.8, label = '64 atoms (6 kpts)')
    plt.plot([], [], linestyle='--', color='black', alpha=0.8, label = '128 atoms (8 kpts)')
    plt.plot([], [], linestyle=':', color='black', alpha=0.8, label = '256 atoms (6 kpts)')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='KPAR')

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 200
plt.rcParams['figure.figsize'] = [6, 3]
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.25

hardware_types = ["bc_sapphirerapids", "sc_icelake", "sc_cascadelake"]
systems = ["NiOconv2x2x2", "NiOconv4x2x2", "NiOconv4x4x2"]

linestyles = {
    "NiOconv2x2x2": "-",
    "NiOconv4x2x2": "--",
    "NiOconv4x4x2": ":"
}

for hardware_type in hardware_types:
    for system in systems:

        data = pd.read_csv(f"../data/{system}/kpar_multinode/{hardware_type}.csv")
        print(data)
        
        plt.plot(data.num_nodes, data.kpar1[0]/data.kparnodes, marker='^', color='blue', alpha=0.8, linestyle=linestyles[system])
        plt.plot(data.num_nodes, data.kpar1[0]/data.kpar1, marker='o', color='red', alpha=0.8, linestyle=linestyles[system])
    plt.plot([0, 10], [0, 10], color='black', linestyle='-', alpha=0.25, zorder=0)
    plt.xlim(0, 8.5)
    plt.ylim(0, 6.5)
    plt.xticks([0, 2, 4, 6, 8])
    plt.yticks([0, 2, 4, 6])
    plt.xlabel("# nodes")
    plt.ylabel("speedup")
    plt.title(f"{hardware_type}", weight='bold')
    plt.legend(title='KPAR', loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(alpha=0.1)
    add_legend()
    plt.tight_layout()
    plt.savefig(f"../results/kpar_speedup_{hardware_type}.png")
    plt.clf()
