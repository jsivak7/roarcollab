from roarcollab.allocation_balances import check_date,get_todays_data,plot_data,repo_update
from datetime import date
import os

allocations = [
    "sbs5563",
    "sbs5563_bc",
    "sbs5563_sc",
    "ixd4_n_bc",
    "ixd4_t_sc",
    "ixd4_s_sc",
]

datapath = "../data/alloc_balances.csv"

if check_date() == False:
    updated_alloc_df = get_todays_data(allocations, datapath)
    updated_alloc_df.to_csv(datapath, index=False)
    with open("../docs/last_alloc_collect_date", "w") as datefile:
        datefile.write(str(date.today()))

    plot_data(updated_alloc_df,allocations,"../results/")
    os.chdir('../')
    repo_update()
    print("\nSuccess!\n")
