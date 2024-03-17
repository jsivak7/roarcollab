def repo_update():
    """Commits and pushes updates - meant for allocation balancess"""
    import os
    from datetime import date

    print("\nCommitting and pushing updated allocation balances...")
    os.system("git commit -a -m '{}'".format(date.today()))
    os.system("git push")


def plot_data(dataframe, allocations, resultspath):
    """
    Plots updated allocation balances

    Args:
        dataframe (pandas DataFrame): with dates and allocation balances
        allocations (str): all slurm allocations
        resultspath (str): realtive path to results
    """
    from datetime import date
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['figure.dpi'] = 400
    plt.rcParams['figure.figsize'] = [8, 4]
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.linewidth'] = 1.25

    print("\nPlotting updated allocation balances...")

    for allocation in allocations:
        plt.plot(np.arange(len(dataframe['date'])), dataframe[allocation], label=allocation)
        plt.xticks([])
        plt.grid(visible=True, alpha = 0.25, axis='y')
        plt.ticklabel_format(style='plain', axis='y')
        
        plt.title(f"Allocation Balances (as of {date.today().strftime('%b %d, %Y')})", weight='bold')
        plt.xlabel("Time")
        plt.ylabel('CPU Hours')
        plt.tight_layout()
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tick_params(width=1.25)

        plt.savefig(f'{resultspath}/alloc_balances.png')


def get_todays_data(allocations, datapath):
    """
    Gets current date's balance for all allocations

    Args:
        allocations (list): list of strings for all allocations
        datapath (str): relative path to data

    Returns:
        pandas DataFrame: updated dataframe object for all allocations
    """
    from datetime import date
    import pandas as pd

    print(f"\nCollecting allocation balances for today ({date.today()})...\n")
    new_alloc_data = {'date': date.today()}
    alloc_df = pd.read_csv(datapath)

    for allocation in allocations:
        balance = _get_alloc_data(allocation)
        print(f"{allocation} \t-> {balance} cpu hours")
        new_alloc_data[allocation] = [balance]

    new_alloc_df = pd.concat([alloc_df, pd.DataFrame(new_alloc_data)])
    return new_alloc_df


def _get_alloc_data(alloc):
    """
    Gets allocation data on slurm system for a given allocation/account..

    Args:
        alloc (str): name of slurm allocation/account to get balance for

    Returns:
        float: Balance hours for allocation given
    """
    import os
    
    os.system("mybalance > all_alloc_balances")
    with open("all_alloc_balances") as oldfile, open("alloc_balance", "w") as newfile:
        found = False
        for line in oldfile:
            if alloc in line and found == False:
                newfile.write(line)
                found = True # to only get first instance since may only differ by trailing characters
    balance = open("alloc_balance").readline().split()[3]
    os.system("rm all_alloc_balances alloc_balance")
    return balance


def check_date():
    """
    For checking if allocation data has already been collected for today on slurm.
    Compares current date to 'last_alloc_collect_date' file in my home dir on Roar Collab

    Returns:
        True if has already been collected for the day. False otherwise.
    """
    from datetime import date
    
    today = str(date.today())
    with open("../docs/last_alloc_collect_date") as f:
        last_extract_date = f.readline()
        if today == last_extract_date:
            print(f"\nAllocation data has already been extracted for today ({today})...\n")
            return True
        else:
            return False