from scipy.stats import chi2
from color import *


def one_variance():
    alpha = float(input("Level of significance: "))

    print("Is the data in Variance: ")
    print("1. yes")
    print("2. no")
    selection = int(input())

    if selection == 1:
        n = float(input("No of samples: "))
        variance = float(input("Variance of sample 𝜎^2: "))
        claim_variance = float(input("Claim Variance 𝜎^2_0: "))
        print(
            f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null 𝜎^2_0 = {claim_variance}{bcolors.FAIL}")
        print(f"1. 𝜎^2 < {claim_variance} ")
        print(f"2. 𝜎^2 > {claim_variance} ")
        print(f"3. 𝜎^2 != {claim_variance} {bcolors.ENDC}")
        test_statistics_value = ((n - 1) * variance) / claim_variance
        selection = int(input())

        if selection == 1:
            critical_value = -1 * (round((chi2.isf(1 - alpha, df=n - 1)), 4))
            print(f"The null must be rejected if χ^2<{critical_value}\n")
            print("Calculations\n")
            print(f"χ^2 = {test_statistics_value}\n")
            print("Decision\n")
            if test_statistics_value < critical_value:
                print(
                    f"Null 𝜎^2 = {claim_variance} must be Rejected at level of significance {alpha} and Accept 𝜎^2 < {claim_variance}")
            else:
                print(f"Failure to reject Null 𝜎^2 = {claim_variance} ")

        if selection == 2:
            critical_value = (round((chi2.isf(alpha, df=n - 1)), 4))
            print(f"The null must be rejected if χ^2>{critical_value}\n")
            print("Calculations\n")
            print(f"χ^2 = {test_statistics_value}\n")
            print("Decision\n")
            if test_statistics_value > critical_value:
                print(
                    f"Null 𝜎^2 = {claim_variance} must be Rejected at level of significance {alpha} and Accept 𝜎^2 > {claim_variance}")
            else:
                print(f"Failure to reject Null 𝜎^2 = {claim_variance}  ")

        if selection == 3:
            critical_value_lower = -1 * (round((chi2.isf(1 - alpha / 2, df=n - 1)), 4))
            critical_value_upper = (round((chi2.isf(alpha / 2, df=n - 1)), 4))
            print(f" The null must be rejected if χ^2<{critical_value_lower} or χ^2>{critical_value_upper}\n")
            print("Calculations\n")
            print(f"χ^2 = {test_statistics_value}\n")
            print("Decision\n")
            if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
                print(
                    f"Null 𝜎^2 = {claim_variance} must be Rejected at level of significance {alpha} and Accept 𝜎^2 != {claim_variance}")
            else:
                print(f"Failure to reject Null 𝜎^2 = {claim_variance} ")

    if selection == 2:
        n = float(input("No of samples: "))
        variance = float(input("Standard deviation of sample 𝜎: "))**2
        claim_std_deviation = float(input("Claim Standard deviation 𝜎_0: "))
        print(
            f"\n{bcolors.OKCYAN}Select the alternative Hypothesis to test with null 𝜎_0 = {claim_std_deviation}{bcolors.FAIL}")
        print(f"1. 𝜎 < {claim_std_deviation} ")
        print(f"2. 𝜎 > {claim_std_deviation} ")
        print(f"3. 𝜎 != {claim_std_deviation} {bcolors.ENDC}")
        test_statistics_value = ((n - 1) * variance) / claim_std_deviation**2
        selection = int(input())

        if selection == 1:
            critical_value = -1 * (round((chi2.isf(1 - alpha, df=n - 1)), 4))
            print(f"The null must be rejected if χ^2<{critical_value}\n")
            print("Calculations\n")
            print(f"χ^2 = {test_statistics_value}\n")
            print("Decision\n")
            if test_statistics_value < critical_value:
                print(
                    f"Null 𝜎 = {claim_std_deviation} must be Rejected at level of significance {alpha} and Accept 𝜎 < {claim_std_deviation}")
            else:
                print(f"Failure to reject Null 𝜎 = {claim_std_deviation} ")

        if selection == 2:
            critical_value = (round((chi2.isf(alpha, df=n - 1)), 4))
            print(f"The null must be rejected if χ^2>{critical_value}\n")
            print("Calculations\n")
            print(f"χ^2 = {test_statistics_value}\n")
            print("Decision\n")
            if test_statistics_value > critical_value:
                print(
                    f"Null 𝜎 = {claim_std_deviation} must be Rejected at level of significance {alpha} and Accept 𝜎 > {claim_std_deviation}")
            else:
                print(f"Failure to reject Null 𝜎 = {claim_std_deviation}  ")

        if selection == 3:
            critical_value_lower = -1 * (round((chi2.isf(1 - alpha / 2, df=n - 1)), 4))
            critical_value_upper = (round((chi2.isf(alpha / 2, df=n - 1)), 4))
            print(f" The null must be rejected if χ^2<{critical_value_lower} or χ^2>{critical_value_upper}\n")
            print("Calculations\n")
            print(f"χ^2 = {test_statistics_value}\n")
            print("Decision\n")
            if test_statistics_value > critical_value_upper or test_statistics_value < critical_value_lower:
                print(
                    f"Null 𝜎 = {claim_std_deviation} must be Rejected at level of significance {alpha} and Accept 𝜎 != {claim_std_deviation}")
            else:
                print(f"Failure to reject Null 𝜎 = {claim_std_deviation} ")




