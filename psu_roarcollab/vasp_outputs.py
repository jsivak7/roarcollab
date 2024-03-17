def get_total_cpu_time(outcarpath):
    """
    Uses pymatgen to get total CPU time of VASP calculation

    Args:
        outcarpath (str): relative path to OUTCAR file

    Returns:
        time (float): in seconds
    """

    from pymatgen.io.vasp import Outcar

    o = Outcar(outcarpath)
    time = o.run_stats['Total CPU time used (sec)']
    return time