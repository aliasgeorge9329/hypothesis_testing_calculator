from goodness_fit_poisson import *
from goodness_fit_binomial import *
from goodness_fit_geometric import *
from goodness_fit_hyper_geometric import *
from goodness_fit_uniform_discrete import *
from goodness_fit_normal import *
from goodness_fit_log_normal import *
from goodness_fit_alpha import *
from goodness_fit_beta import *
from goodness_fit_gamma import *
from goodness_fit_weibull import *
from goodness_fit_exponential import *
from goodness_fit_uniform_continous import *
from color import *


def goodness_fit():
    print("\nSelect the Calculator\n")
    print(f"{bcolors.FAIL}Discrete Distribution{bcolors.ENDC}")
    print("1. Goodness Fit for Poisson Test")
    print("2. Goodness Fit for Binomial Test")
    print("3. Goodness Fit for Geometric Test")
    print("4. Goodness Fit for Hyper Geometric Test")
    print("5. Goodness Fit for Uniform Discrete Test\n")
    print(f"{bcolors.FAIL}Continuous Distribution{bcolors.ENDC}")
    print("6. Goodness Fit for Normal Test")
    print("7. Goodness Fit for Log Normal Test")
    print("8. Goodness Fit for Alpha Test")
    print("9. Goodness Fit for Beta Test")
    print("10. Goodness Fit for Gamma Test")
    print("11. Goodness Fit for Weibull Test")
    print("12. Goodness Fit for Exponential Test")
    print("13. Goodness Fit for Uniform Continuous Test")

    selection = int(input())
    print("\n")
    if selection == 1:
        goodness_fit_poisson()
    elif selection == 2:
        goodness_fit_binomial()
    elif selection == 3:
        goodness_fit_geometric()
    elif selection == 4:
        goodness_fit_hyper_geometric()
    elif selection == 5:
        goodness_fit_uniform_discrete()
    elif selection == 6:
        goodness_fit_normal()
    elif selection == 7:
        goodness_fit_log_normal()
    elif selection == 8:
        goodness_fit_alpha()
    elif selection == 9:
        goodness_fit_beta()
    elif selection == 10:
        goodness_fit_gamma()
    elif selection == 11:
        goodness_fit_weibull()
    elif selection == 12:
        goodness_fit_exponential()
    elif selection == 13:
        goodness_fit_uniform_continuous()
    else:
        print("Invalid selection")



