import math
from raw_data import enter_raw
from scipy.stats import t
from color import *


def two_mean_small():
    # For both normal population and 𝝈1 = 𝝈2
    alpha = float(input("Level of significance: "))
    print("Is the data given in raw format: ")
    print("1. yes")
    print("2. no")
    selection = int(input())

    n_1 = 0
    sample_mean_1 = 0
    std_deviation_1 = 0

    n_2 = 0
    sample_mean_2 = 0
    std_deviation_2 = 0

    if selection == 1:
        data_1 = enter_raw(1)
        data_2 = enter_raw(2)
        (n_1, sample_mean_1, std_deviation_1) = data_1
        (n_2, sample_mean_2, std_deviation_2) = data_2

    if selection == 2:

        n_1 = float(input("No of samples 1: "))
        sample_mean_1 = float(input("Mean of sample 1: "))
        std_deviation_1 = float(input("Standard deviation of sample/Population 1: "))
        n_2 = float(input("No of samples 2: "))
        sample_mean_2 = float(input("Mean of sample 2: "))
        std_deviation_2 = float(input("Standard deviation of sample/Population 2: "))

    delta_0 = float(input("μ1 - μ2 : "))

    pooled_estimator_sp = math.sqrt(((n_1 - 1)*(std_deviation_1**2)+(n_2 - 1)*(std_deviation_2**2))/(n_1+n_2-2))

    test_statistics_value = (sample_mean_1-sample_mean_2 - delta_0) / \
                            (pooled_estimator_sp * math.sqrt((1 / n_1) + (1 / n_2)))

    d_f = n_1+n_2-2

    print(f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null μ1 - μ2 = {delta_0}{bcolors.FAIL}")
    print(f"1. μ1 - μ2 < {delta_0} ")
    print(f"2. μ1 - μ2 > {delta_0} ")
    print(f"3. μ1 - μ2 != {delta_0}{bcolors.ENDC} ")

    selection = int(input())

    if selection == 1:
        critical_value = -1*round(t.isf(alpha, df=d_f), 4)
        print(f"The null must be rejected if t<{critical_value}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value < critical_value:
            print(f"Null μ1 - μ2 = {delta_0} must be Rejected at level of significance {alpha} and Accept μ1 - μ2 < {delta_0}")
        else:
            print(f"Failure to reject Null μ1 - μ2 = {delta_0} ")

    if selection == 2:
        critical_value = round(t.isf(alpha, df=d_f), 4)
        print(f"The null must be rejected if t>{critical_value}\n")
        print("Calculations\n")
        print(f"Z = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value:
            print(f"Null μ1 - μ2 = {delta_0} must be Rejected at level of significance {alpha} and Accept μ1 - μ2 > {delta_0}")
        else:
            print(f"Failure to reject Null μ1 - μ2 = {delta_0} ")

    if selection == 3:
        critical_value_lower = -1*round(t.isf(alpha / 2, df=d_f), 4)
        critical_value_upper = round(t.isf(alpha / 2, df=d_f), 4)
        print(f" The null must be rejected if t<{critical_value_lower} or t>{critical_value_upper}\n")
        print("Calculations\n")
        print(f"t = {test_statistics_value}\n")
        print("Decision\n")
        if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
            print(f"Null μ1 - μ2 = {delta_0} must be Rejected at level of significance {alpha} and Accept μ1 - μ2 != {delta_0}")
        else:
            print(f"Failure to reject Null μ1 - μ2 = {delta_0} ")


