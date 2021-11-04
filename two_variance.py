import math
from scipy.stats import f
from color import *


def two_variance():
    alpha = float(input("Level of significance: "))

    print("Is the data in Variance: ")
    print("1. yes")
    print("2. no")
    selection = int(input())

    n_1 = 0
    std_deviation_1 = 0

    n_2 = 0
    std_deviation_2 = 0

    if selection == 1:
        n_1 = float(input("No of samples 1: "))
        std_deviation_1 = math.sqrt(float(input("Variance of sample 1 𝜎^2_1: ")))
        n_2 = float(input("No of samples 2: "))
        std_deviation_2 = math.sqrt(float(input("Variance of sample 2 𝜎^2_2: ")))

    if selection == 2:
        n_1 = float(input("No of samples 1: "))
        std_deviation_1 = float(input("Standard deviation of sample 1 𝜎_1: "))
        n_2 = float(input("No of samples 2: "))
        std_deviation_2 = float(input("Standard deviation of sample 2 𝜎_2: "))

    if std_deviation_1 > std_deviation_2:
        test_statistics_value = std_deviation_1**2/std_deviation_2**2
    else:
        test_statistics_value = std_deviation_2**2/std_deviation_1**2

    print(f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null 𝜎^2_1 = 𝜎^2_2 {bcolors.FAIL}")
    print(f"1. 𝜎^2_1 < 𝜎^2_2 ")
    print(f"2. 𝜎^2_1 > 𝜎^2_2 ")
    print(f"3. 𝜎^2_1 != 𝜎^2_2 {bcolors.ENDC}")

    selection = int(input())

    if selection == 1:
        critical_value = round(f.isf(alpha, dfn=n_2-1, dfd=n_1-1), 4)
        print(f"The null must be rejected if F>{critical_value}\n")
        print("Calculations\n")
        print(f"F = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null 𝜎^2_1 = 𝜎^2_2 must be Rejected at level of significance {alpha} and Accept 𝜎^2_1 < 𝜎^2_2")
        else:
            print(f"Failure to reject Null 𝜎^2_1 = 𝜎^2_2")

    if selection == 2:
        critical_value = round(f.isf(alpha, dfn=n_2-1, dfd=n_1-1), 4)
        print(f"The null must be rejected if F>{critical_value}\n")
        print("Calculations\n")
        print(f"F = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null 𝜎^2_1 = 𝜎^2_2  must be Rejected at level of significance {alpha} and Accept 𝜎^2_1 > 𝜎^2_2")
        else:
            print(f"Failure to reject Null 𝜎^2_1 = 𝜎^2_2")

    if selection == 3:
        critical_value = round(f.isf(alpha/2, dfn=n_2-1, dfd=n_1-1), 4)
        print(f" The null must be rejected if F>{critical_value}\n")
        print("Calculations\n")
        print(f"F = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null 𝜎^2_1 = 𝜎^2_2 must be Rejected at level of significance {alpha} and Accept 𝜎^2_1 != 𝜎^2_2")
        else:
            print(f"Failure to reject Null 𝜎^2_1 = 𝜎^2_2")


