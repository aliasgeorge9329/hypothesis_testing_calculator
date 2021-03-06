from scipy.stats import chi2
from prettytable import PrettyTable
from combining import *
from color import *
table = PrettyTable(['X', 'Observed Frequency', 'Uniform Discrete Probabilities', 'Expected Frequency'])
reduced_table = PrettyTable(['Observed Frequency', 'Uniform Discrete Probabilities', 'Expected Frequency'])


def uniform_discrete(x, a_, b_):
    return 1/(b_-a_+1)


def goodness_fit_uniform_discrete():
    # Binomial
    alpha = float(input("Level of significance: "))
    print("f(k)= 1/(b-a+1) \nk belongs to {a,........,b-1}\n")
    a_ = float(input("Enter the a: "))
    b_ = float(input("Enter the b: "))

    no = int(input(f"Enter the no of Categories: "))

    print(f"\n{bcolors.OKCYAN}Does the random variable values is in the order 0,1,3,.....,{no - 2},{no - 1}")
    print("1. yes")
    print(f"2. no {bcolors.ENDC}")

    selection = int(input())
    print("\n")

    data = []
    if selection == 1:
        for i in range(0, no):
            a = dict()
            a["x"] = i
            a["obf"] = float(input(f"Enter the Observed Frequency for {a['x']} "))
            data.append(a)

    if selection == 2:
        for i in range(0, no):
            a = dict()
            a["x"] = float(input(f"Enter the random variable value {i} "))
            a["obf"] = float(input(f"Enter the Observed Frequency for {a['x']} "))
            print("\n")
            data.append(a)

    total_obf = 0
    for each in data:
        total_obf += each["obf"]

    for each in data:
        each["probability"] = round(uniform_discrete(each["x"], a_, b_), 3)
        each["exp_obf"] = int(each["probability"] * total_obf * 10) / 10

    for each in data:
        table.add_row([each['x'], each['obf'], each['probability'], each['exp_obf']])

    print(f"\n{table}")

    new_data = combining(data, no)

    for each in new_data:
        reduced_table.add_row([each['obf'], each['probability'], each['exp_obf']])

    total_chi_square = 0
    contribution_to_chi2 = []
    for each in new_data:
        b = round((each["obf"] - each["exp_obf"]) ** 2 / each["exp_obf"], 3)
        total_chi_square += b
        contribution_to_chi2.append(b)
    reduced_table.add_column('Contribution to ??^2', contribution_to_chi2)

    print(f"\n{reduced_table}")

    print(f"\n{bcolors.BOLD}{bcolors.WARNING}Null hypothesis: Random variable has a Uniform Discrete distribution with "
          f"a = {a_} and b = {b_}")
    print(f"Alternative hypothesis: Random variable does not have the Uniform Discrete distribution with a = {a_} and "
          f"b = {b_}.{bcolors.ENDC}\n")

    print("\nCalculations\n")
    print(f"Total Chi_square: {total_chi_square}\n")
    print(f"Decision")

    critical_value = (round((chi2.isf(alpha, df=len(new_data) - 1)), 4))
    print(f"The null must be rejected if ??^2 > {critical_value}\n{bcolors.FAIL}")
    if total_chi_square > critical_value:
        print(f"Since ??^2 = {total_chi_square} exceed {critical_value}, the null 'Data fit to the distribution'"
              f" must be Rejected at level of significance {alpha} and Accept 'Data not fit to the distribution' ")
    else:
        print(f"Since ??^2 = {total_chi_square} does not exceed {critical_value}, the null hypothesis cannot be "
              f"rejected; we cannot reject that the Uniform Discrete distribution with ?? a = {a_} and b = {b_}"
              f" provides a good fit at level "
              f"??? = {alpha}.")

    print(f"{bcolors.ENDC}")

