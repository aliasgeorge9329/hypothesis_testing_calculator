from scipy.stats import poisson, chi2
from prettytable import PrettyTable
from combining import *
from color import *
table = PrettyTable(['X', 'Observed Frequency', 'Poisson Probabilities', 'Expected Frequency'])
reduced_table = PrettyTable(['Observed Frequency', 'Poisson Probabilities', 'Expected Frequency'])


def goodness_fit_poisson():
    # Poisson
    alpha = float(input("Level of significance: "))
    mean = float(input("Enter the λ: "))

    no = int(input(f"Enter the no of Categories: "))

    print(f"\n{bcolors.OKCYAN}Does the random variable values is in the order 0,1,3,.....,{no - 2},{no - 1}")
    print("1. yes")
    print(f"2. no {bcolors.ENDC}")

    selection = int(input())
    print("\n")

    print(f"\n{bcolors.OKBLUE}Does the random variable values at last category is ")
    print(f"1. last no")
    print(f"2. last no{bcolors.ENDC} >")
    sel = int(input())
    print("\n")

    data = []
    if selection == 1:
        for i in range(0, no):
            a = dict()
            a["x"] = i
            a["obf"] = int(input(f"Enter the Observed Frequency for {a['x']} "))
            data.append(a)

    if selection == 2:
        for i in range(0, no):
            a = dict()
            a["x"] = int(input(f"Enter the random variable value {i}"))
            a["obf"] = int(input(f"Enter the Observed Frequency for {a['x']} "))
            print("\n")
            data.append(a)

    total_obf = 0
    for each in data:
        total_obf += each["obf"]

    if sel == 1:
        for each in data:
            each["probability"] = round(poisson.pmf(each["x"], mean), 3)
            each["exp_obf"] = int(each["probability"] * total_obf * 10) / 10
            table.add_row([each['x'], each['obf'], each['probability'], each['exp_obf']])

    elif sel == 2:
        for each in data[0:len(data)-1]:
            each["probability"] = round(poisson.pmf(each["x"], mean), 3)
            each["exp_obf"] = int(each["probability"] * total_obf * 10) / 10
            table.add_row([each['x'], each['obf'], each['probability'], each['exp_obf']])

        data[len(data)-1]["probability"] = poisson.sf(data[len(data)-1]["x"], mean) + poisson.pmf(data[len(data)-1]["x"], mean)
        data[len(data)-1]["exp_obf"] = int(data[len(data)-1]["probability"] * total_obf * 10) / 10
        table.add_row([f"{data[len(data)-1]['x']} >", data[len(data)-1]['obf'], data[len(data)-1]["probability"], data[len(data)-1]["exp_obf"]])

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

    print(f"\n{bcolors.BOLD}{bcolors.WARNING}Null hypothesis: Random variable has a Poison distribution with λ = {mean}.")
    print(f"Alternative hypothesis: Random variable does not have the Poison distribution with λ = {mean}.{bcolors.ENDC}\n")

    print("\nCalculations\n")
    print(f"Total Chi_square: {total_chi_square}\n")
    print(f"Decision")

    critical_value = (round((chi2.isf(alpha, df=len(new_data) - 1)), 4))
    print(f"The null must be rejected if χ^2 > {critical_value}\n{bcolors.FAIL}")
    if total_chi_square > critical_value:
        print(f"Since χ^2 = {total_chi_square} exceed {critical_value}, the null 'Data fit to the distribution'"
              f" must be Rejected at level of significance {alpha} and Accept 'Data not fit to the distribution' ")
    else:
        print(f"Since χ^2 = {total_chi_square} does not exceed {critical_value}, the null hypothesis cannot be "
              f"rejected; we cannot reject that the Poisson distribution with λ = {mean} provides a good fit at level "
              f"⍺ = {alpha}.")

    print(f"{bcolors.ENDC}")

