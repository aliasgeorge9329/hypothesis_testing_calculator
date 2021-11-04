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
print(f"\n{bcolors.BOLD}{bcolors.WARNING}Welcome to the Hypothesis Testing calculator made by ALIAS GEORGE{bcolors.ENDC}\n")
print(f"{bcolors.FAIL}Select the Calculator (type the no corresponding eg 1 for one mean Large sample){bcolors.ENDC}\n")
print("1. One Mean Large sample")
print("2. One Mean Small sample ")
print("3. Two Mean Large sample ")
print("4. Two Mean Small sample with both normal and 𝜎1 = 𝜎1 ")
print("5. One Variance Test")
print("6. Two Variance Test")
print("7. Matched Pair Test")
print("8. One Proportion Test")
print("9. Multi Proportion t-Test")
print("10. Two Proportion Difference Test")
print("11. R and C Analysis Test")
print("12. Goodness Fit Test")


selection = int(input())
print("\n")

if selection == 1:
    one_mean_large()
elif selection == 2:
    one_mean_small()
elif selection == 3:
    two_mean_large()
elif selection == 4:
    two_mean_small()
elif selection == 5:
    one_variance()
elif selection == 6:
    two_variance()
elif selection == 7:
    matched_pair_t_test()
elif selection == 8:
    one_proportion()
elif selection == 9:
    multiple_proportion()
elif selection == 10:
    two_proportion_difference()
elif selection == 11:
    r_c_testing()
elif selection == 12:
    goodness_fit()
else:
    print("Invalid selection")