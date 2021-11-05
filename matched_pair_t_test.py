import math
from scipy.stats import t
import statistics
from color import *


def matched_pair_t_test():
    alpha = float(input("Level of significance: "))
    no = input(f"Enter the Raw data of Before \n")
    before_ = no.strip().split(" ")
    before = [float(x) for x in before_]

    no = input(f"Enter the Raw data of After \n")
    after_ = no.strip().split(" ")
    after = [float(x) for x in after_]

    D = [before[after.index(x)] - x for x in after]

    n = len(D)
    mean = statistics.mean(D)
    std_devi = statistics.stdev(D)
    print(f"\nMatched pair\n{D}\n")
    print(f"Mean of the Matched pair data: {mean}")
    print(f"Standard Deviation of the Matched pair data: {std_devi}\n")

    claim_mean = float(input("Mean Difference μD: "))
    test_statistics_value = (mean - claim_mean) / (std_devi / math.sqrt(n))

    print(f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null μD = {claim_mean}{bcolors.FAIL}")
    print(f"1. μD < {claim_mean} ")
    print(f"2. μD > {claim_mean} ")
    print(f"3. μD != {claim_mean}{bcolors.ENDC} ")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(t.isf(alpha, df=n-1), 4)
        print(f"The null must be rejected if t<{critical_value}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null μD = {claim_mean}  must be Rejected at level of significance {alpha} and Accept μD < {claim_mean}")
        else:
            print(f"Failure to reject Null μD = {claim_mean} ")

    if selection == 2:
        critical_value = round(t.isf(alpha, df=n-1), 4)
        print(f"The null must be rejected if t>{critical_value}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null μD = {claim_mean} must be Rejected at level of significance {alpha} and Accept μD > {claim_mean}")
        else:
            print(f"Failure to reject Null μD = {claim_mean}  ")

    if selection == 3:
        critical_value_lower = -1*round(t.isf(alpha / 2, df=n-1), 4)
        critical_value_upper = round(t.isf(alpha / 2, df=n-1), 4)
        print(f" The null must be rejected if t<{critical_value_lower} or t>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null μD = {claim_mean} must be Rejected at level of significance {alpha} and Accept μD != {claim_mean}")
        else:
            print(f"Failure to reject Null μD = {claim_mean} ")
