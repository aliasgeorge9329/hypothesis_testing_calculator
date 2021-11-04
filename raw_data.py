import statistics
from color import *


def enter_raw(data):
    no = input(f"Enter the Raw data of {data} \n")
    a = no.strip().split(" ")
    floats = [float(x) for x in a]
    mean = statistics.mean(floats)
    n = len(floats)
    std_devi = statistics.stdev(floats)
    print(f"\n{bcolors.OKBLUE}No of Sample data {n}")
    print(f"Mean of the sample data {mean}")
    print(f"Standard Deviation of the sample data {std_devi}{bcolors.ENDC}\n")

    return n, mean, std_devi

