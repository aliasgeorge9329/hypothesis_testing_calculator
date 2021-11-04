import math
from raw_data import enter_raw
from scipy.stats import t
from color import *


def one_mean_small():
    alpha = float(input("Level of significance: "))
    print("Is the data given in raw format: ")
    print("1. yes")
    print("2. no")
    selection = int(input())

    n = 0
    sample_mean = 0
    std_deviation = 0

    if selection == 1:
        data_1 = enter_raw(1)
        (n, sample_mean, std_deviation) = data_1

    if selection == 2:

        n = float(input("No of samples: "))
        sample_mean = float(input("Mean of sample: "))
        std_deviation = float(input("Standard deviation of sample: "))

    claim_mean = float(input("Claim Mean: "))
    test_statistics_value = (sample_mean - claim_mean) / (std_deviation / math.sqrt(n))

    print(f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null μ = {claim_mean}{bcolors.FAIL}")
    print(f"1. μ < {claim_mean} ")
    print(f"2. μ > {claim_mean} ")
    print(f"3. μ ≠ {claim_mean} {bcolors.ENDC}")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(t.isf(alpha, df=n-1), 4)
        print(f"The null must be rejected if t<{critical_value}\n")
        print("Calculations\n")
        print(f"Sample mean = {sample_mean}")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null μ = {claim_mean} must be Rejected at level of significance {alpha} and Accept μ < {claim_mean}")
        else:
            print(f"Failure to reject Null μ = {claim_mean} ")

    if selection == 2:
        critical_value = round(t.isf(alpha, df=n-1), 4)
        print(f"The null must be rejected if t>{critical_value}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null μ = {claim_mean} must be Rejected at level of significance {alpha} and Accept μ > {claim_mean}")
        else:
            print(f"Failure to reject Null μ = {claim_mean}  ")

    if selection == 3:
        critical_value_lower = -1*round(t.isf(alpha / 2, df=n-1), 4)
        critical_value_upper = round(t.isf(alpha / 2, df=n-1), 4)
        print(f" The null must be rejected if t<{critical_value_lower} or t>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null μ = {claim_mean} must be Rejected at level of significance {alpha} and Accept μ != {claim_mean}")
        else:
            print(f"Failure to reject Null μ = {claim_mean} ")


