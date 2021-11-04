import math
from scipy.stats import norm
from color import *


def one_mean_large():
    alpha = float(input("Level of significance: "))
    n = float(input("No of samples: "))
    sample_mean = float(input("Mean of sample: "))
    std_deviation = float(input("Standard deviation of sample/Population: "))
    claim_mean = float(input("Claim Mean: "))
    test_statistics_value = (sample_mean-claim_mean)/(std_deviation/math.sqrt(n))

    print(f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null μ = {claim_mean}{bcolors.FAIL}")
    print(f"1. μ < {claim_mean} ")
    print(f"2. μ > {claim_mean} ")
    print(f"3. μ ≠ {claim_mean} {bcolors.ENDC}")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(norm.isf(alpha, loc=0, scale=1), 4)
        print(f"\nThe null must be rejected if Z<{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null μ = {claim_mean} must be Rejected at level of significance {alpha} and Accept μ < {claim_mean}")
        else:
            print(f"Failure to reject Null μ = {claim_mean} ")

    if selection == 2:
        critical_value = round(norm.isf(alpha, loc=0, scale=1), 4)
        print(f"The null must be rejected if Z>{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null μ = {claim_mean} must be Rejected at level of significance {alpha} and Accept μ > {claim_mean}")
        else:
            print(f"Failure to reject Null μ = {claim_mean}  ")

    if selection == 3:
        critical_value_lower = -1*round(norm.isf(alpha / 2, loc=0, scale=1), 4)
        critical_value_upper = round(norm.isf(alpha / 2, loc=0, scale=1), 4)
        print(f" The null must be rejected if Z<{critical_value_lower} or Z>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null μ = {claim_mean} must be Rejected at level of significance {alpha} and Accept μ ≠ {claim_mean}")
        else:
            print(f"Failure to reject Null μ = {claim_mean} ")


