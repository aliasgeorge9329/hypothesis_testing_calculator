import math
from scipy.stats import norm
from color import *


def two_proportion_difference():
    alpha = float(input("Level of significance: "))
    n_1 = float(input("No of samples 1: "))
    no_success_1 = float(input("No of Success 1: "))

    n_2 = float(input("No of samples 2: "))
    no_success_2 = float(input("No of Success 2: "))
    p_ = (no_success_1+no_success_2)/(n_1+n_2)

    test_statistics_value = (no_success_1/n_1 - no_success_2/n_2)/math.sqrt((p_*(1-p_))*(1/n_1+1/n_2))

    print(f"{bcolors.OKCYAN}Select the alternative Hypothesis to test with null p1 = p2 {bcolors.FAIL}")
    print(f"1. p1 < p2 ")
    print(f"2. p1 > p2 ")
    print(f"3. p1 != p2 {bcolors.ENDC}")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(norm.isf(alpha, loc=0, scale=1), 4)
        print(f"The null must be rejected if Z<{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null p1 = p2  must be Rejected at level of significance {alpha} and Accept p1 < p2")
        else:
            print(f"Failure to reject Null p1 = p2 ")

    if selection == 2:
        critical_value = round(norm.isf(alpha, loc=0, scale=1), 4)
        print(f"The null must be rejected if Z>{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null p1 = p2 must be Rejected at level of significance {alpha} and Accept p1 > p2")
        else:
            print(f"Failure to reject Null p1 = p2")

    if selection == 3:
        critical_value_lower = -1*round(norm.isf(alpha / 2, loc=0, scale=1), 4)
        critical_value_upper = round(norm.isf(alpha / 2, loc=0, scale=1), 4)
        print(f" The null must be rejected if Z<{critical_value_lower} or Z>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null p1 = p2 must be Rejected at level of significance {alpha} and Accept p1 != p2")
        else:
            print(f"Failure to reject Null p1 = p2 ")


