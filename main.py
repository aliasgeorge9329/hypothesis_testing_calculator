from one_mean_large import *
from one_mean_small import *
from two_mean_large import *
from two_mean_small import *
from one_variance import *
from two_variance import *
from matched_pair_t_test import *
from one_proportion import *
from multiple_proportion import *
from two_proportion_difference import *
from r_c_testing import *
from Goodness_fit import *
from color import *

print(f"\n{bcolors.BOLD}{bcolors.WARNING}Welcome to the Hypothesis Testing calculator made by ALIAS GEORGE{bcolors.ENDC}\n")
print(f"{bcolors.FAIL}Select the Calculator (type the no corresponding eg 1 for one mean Large sample){bcolors.ENDC}\n")
print("1. One Mean Large sample n > 30")
print("2. One Mean Small sample (𝝈 unknown)")
print("3. Two Mean Large sample n1 , n2 > 30")
print("4. Two Mean Small sample with both normal and 𝜎1 = 𝜎1 ")
print("5. Matched Pair t-Test")
print("6. One Variance Test")
print("7. Two Variance Test")
print("8. One Proportion Test")
print("9. Multi Proportion Test")
print("10. Two Proportion Difference Test")
print("11. R and C Analysis Test (Dependence Test)")
print("12. Goodness Fit Test")


selection = int(input())
print(f"\n{bcolors.OKCYAN}")

if selection == 1:
    print("1. One Mean Large sample n > 30")
    print(f"\n{bcolors.ENDC}")
    one_mean_large()
elif selection == 2:
    print("2. One Mean Small sample (𝝈 unknown)")
    print(f"\n{bcolors.ENDC}")
    one_mean_small()
elif selection == 3:
    print("3. Two Mean Large sample n1 , n2 > 30")
    print(f"\n{bcolors.ENDC}")
    two_mean_large()
elif selection == 4:
    print("4. Two Mean Small sample with both normal and 𝜎1 = 𝜎1 ")
    print(f"\n{bcolors.ENDC}")
    two_mean_small()
elif selection == 5:
    print("5. Matched Pair t-Test")
    print(f"\n{bcolors.ENDC}")
    matched_pair_t_test()
elif selection == 6:
    print("6. One Variance Test")
    print(f"\n{bcolors.ENDC}")
    one_variance()
elif selection == 7:
    print("7. Two Variance Test")
    print(f"\n{bcolors.ENDC}")
    two_variance()
elif selection == 8:
    print("8. One Proportion Test")
    print(f"\n{bcolors.ENDC}")
    one_proportion()
elif selection == 9:
    print("9. Multi Proportion Test")
    print(f"\n{bcolors.ENDC}")
    multiple_proportion()
elif selection == 10:
    print("10. Two Proportion Difference Test")
    print(f"\n{bcolors.ENDC}")
    two_proportion_difference()
elif selection == 11:
    print("11. R and C Analysis Test (Dependence Test)")
    print(f"\n{bcolors.ENDC}")
    r_c_testing()
elif selection == 12:
    print("12. Goodness Fit Test")
    print(f"\n{bcolors.ENDC}")
    goodness_fit()
else:
    print("Invalid selection")