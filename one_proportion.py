import math
from scipy.stats import norm
from color import *


def one_proportion():
    alpha = float(input("Level of significance: "))
    n = float(input("No of samples: "))
    no_success = float(input("No of Success: "))
    claim_proportion = float(input("Claim Proportion p0: "))
    test_statistics_value = (no_success - n * claim_proportion) / (math.sqrt((n * claim_proportion * (1 - claim_proportion))))

    print(f"{bcolors.OKCYAN}Select the alternative Hypothesis to test with null p0 = {claim_proportion}{bcolors.FAIL}")
    print(f"1. p < {claim_proportion} ")
    print(f"2. p > {claim_proportion} ")
    print(f"3. p ≠ {claim_proportion} {bcolors.ENDC}")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(norm.isf(alpha, loc=0, scale=1), 4)
        print(f"The null must be rejected if Z<{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null p = {claim_proportion} must be Rejected at level of significance {alpha} and Accept p < {claim_proportion}")
        else:
            print(f"Failure to reject Null p = {claim_proportion} ")

    if selection == 2:
        critical_value = round(norm.isf(alpha, loc=0, scale=1), 4)
        print(f"The null must be rejected if Z>{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null p = {claim_proportion} must be Rejected at level of significance {alpha} and Accept p > {claim_proportion}")
        else:
            print(f"Failure to reject Null p = {claim_proportion}  ")

    if selection == 3:
        critical_value_lower = -1*round(norm.isf(alpha / 2, loc=0, scale=1), 4)
        critical_value_upper = round(norm.isf(alpha / 2, loc=0, scale=1), 4)
        print(f" The null must be rejected if Z<{critical_value_lower} or Z>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null p = {claim_proportion} must be Rejected at level of significance {alpha} and Accept p ≠ {claim_proportion}")
        else:
            print(f"Failure to reject Null p = {claim_proportion} ")


