from scipy.stats import beta, chi2
from prettytable import PrettyTable
from combining import *
from color import *
table = PrettyTable(['X', 'Observed Frequency', 'Beta Probabilities of Interval area'])
reduced_table = PrettyTable(['Observed Frequency', 'Beta Probabilities of Interval area', 'Expected Frequency'])


def goodness_fit_beta():
    # Beta
    alpha_ = float(input("Level of significance: "))
    a_ = float(input("Enter the shape parameter a: "))
    b_ = float(input("Enter the shape parameter b: "))
    mean = float(input("Enter the mean μ : "))
    std_devi = float(input("Enter the standard deviation 𝜎 : "))

    no = int(input(f"Enter the no of Categories : "))

    print(f"\n{bcolors.OKCYAN}Does the interval is a continuous one ? eg: <10 , 10 <20 etc")
    print("1. yes")
    print(f"2. no {bcolors.ENDC}")

    selection = int(input())
    print("\n")
    data = []
    if selection == 1:
        a = dict()
        a["x_h"] = int(input(f"Enter the Enter the Highest of each interval_0: "))
        a["obf"] = int(input(f"Enter the Observed Frequency for interval_0: "))
        a["probability"] = round(beta.cdf(a["x_h"], a=a_, b=b_,  loc=mean, scale=std_devi),4)
        print("\n")
        data.append(a)
        table.add_row([f'< {a["x_h"]}', a["obf"], a["probability"]])

        last_final = a["x_h"]
        for i in range(1, no-1):
            a = dict()
            a["x_l"] = last_final
            a["x_h"] = int(input(f"Enter the Enter the Highest of each interval_{i}: "))
            a["obf"] = int(input(f"Enter the Observed Frequency for interval_{i}: "))
            a["probability"] = round((beta.cdf(a["x_h"], a=a_, b=b_, loc=mean, scale=std_devi) - beta.cdf(a["x_l"], a=a_, b=b_, loc=mean, scale=std_devi)), 4)
            print("\n")
            last_final = a["x_h"]
            data.append(a)
            table.add_row([f'{a["x_l"]} < {a["x_h"]}', a["obf"], a["probability"]])

        a = dict()
        a["x_l"] = int(input(f"Enter the Lowest of Interval of_{no - 1}: "))
        a["obf"] = int(input(f"Enter the Observed Frequency for Interval of_{no - 1}: "))
        a["probability"] = round((1 - beta.cdf(a["x_l"], a=a_, b=b_,  loc=mean, scale=std_devi)), 4)
        print("\n")
        data.append(a)
        table.add_row([f'{a["x_l"]} >', a["obf"], a["probability"]])

    if selection == 2:
        for i in range(0, no):
            a = dict()
            a["x_l"] = int(input(f"Enter the Enter the Lowest of each interval_{i}: "))
            a["x_h"] = int(input(f"Enter the Enter the Highest of each interval_{i}: "))
            a["obf"] = int(input(f"Enter the Observed Frequency for interval_{i}: "))
            a["probability"] = round((beta.cdf(a["x_h"], a=a_, b=b_,  loc=mean, scale=std_devi) - beta.cdf(a["x_l"], a=a_, b=b_, loc=mean, scale=std_devi)), 4)
            print("\n")
            data.append(a)
            table.add_row([f'{a["x_l"]} < {a["x_h"]}', a["obf"], a["probability"]])

    total_obf = 0
    for each in data:
        total_obf += each["obf"]

    for each in data:
        each["exp_obf"] = each["probability"] * total_obf

    table.add_column('Expected Frequency', [each["exp_obf"] for each in data])

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
    reduced_table.add_column('Contribution to χ^2', contribution_to_chi2)

    print(f"\n{reduced_table}")

    print(f"\n{bcolors.BOLD}{bcolors.WARNING}Null hypothesis: Random variable has a Alpha distribution with a= {a_}, b= {b_}, μ = {mean} and standard deviation = {std_devi }.")
    print(f"Alternative hypothesis: Random variable does not have the Alpha distribution with a= {a_}, b= {b_}, μ = {mean} and standard deviation = {std_devi }.{bcolors.ENDC}\n")

    print("\nCalculations\n")
    print(f"Total Chi_square: {total_chi_square}\n")
    print(f"Decision")

    critical_value = (round((chi2.isf(alpha_, df=len(new_data)-1)), 4))
    print(f"The null must be rejected if χ^2 > {critical_value}\n{bcolors.FAIL}")
    if total_chi_square > critical_value:
        print(f"Since χ^2 = {total_chi_square} exceed {critical_value}, the null 'Data fit to the distribution'"
              f" must be Rejected at level of significance {alpha_} and Accept 'Data not fit to the distribution' ")
    else:
        print(f"Since χ^2 = {total_chi_square} does not exceed {critical_value}, the null hypothesis cannot be "
              f"rejected; we cannot reject that the Alpha distribution with a= {a_}, b= {b_}, μ = {mean} and standard deviation = {std_devi } provides a good fit at level "
              f"⍺ = {alpha_}.")

    print(f"{bcolors.ENDC}")

