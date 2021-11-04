from scipy.stats import geom, chi2
from prettytable import PrettyTable
from slicing import *
from color import *
table = PrettyTable(['X', 'Observed Frequency', 'Geometric Probabilities', 'Expected Frequency'])
reduced_table = PrettyTable(['Observed Frequency', 'Geometric Probabilities', 'Expected Frequency'])


def goodness_fit_geometric():
    # geometric
    alpha = float(input("Level of significance: "))
    p_ = float(input("Enter the p: "))

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

    for each in data:
        each["probability"] = round(geom.pmf(each["x"], p_), 3)
        each["exp_obf"] = int(each["probability"] * total_obf * 10) / 10

    for each in data:
        table.add_row([each['x'], each['obf'], each['probability'], each['exp_obf']])

    print(f"\n{table}")

    # Reduction

    slicing = []
    for each in data:
        slicing.append(each["obf"])
    slicing = slicing_(slicing, no)

    print(f"\nCombined categories (initial,final) {slicing}")

    new_data = []
    if slicing[0][0] != 0:
        for i in range(0, slicing[0][0]):
            a = dict()
            a["obf"] = data[i]["obf"]
            a["probability"] = data[i]["probability"]
            a["exp_obf"] = data[i]["exp_obf"]
            new_data.append(a)

    for each in slicing:
        initial = each[0]
        final = each[1]
        a = dict()
        a["obf"] = 0
        a["probability"] = 0
        a["exp_obf"] = 0

        for i in range(initial, final + 1):
            a["obf"] += data[i]["obf"]
            a["probability"] += data[i]["probability"]
            a["exp_obf"] += data[i]["exp_obf"]

        new_data.append(a)

        if final == no - 1:
            break

        else:
            new_initial = slicing[slicing.index(each) + 1][0]
            for i in range(final + 1, new_initial):
                a = dict()
                a["obf"] = data[i]["obf"]
                a["probability"] = data[i]["probability"]
                a["exp_obf"] = data[i]["exp_obf"]
                new_data.append(a)

    for each in new_data:
        reduced_table.add_row([each['obf'], each['probability'], each['exp_obf']])

    print(f"\n{reduced_table}")

    total_chi_square = 0
    for each in new_data:
        total_chi_square += (each["obf"] - each["exp_obf"]) ** 2 / each["exp_obf"]

    print("\nCalculations\n")
    print(f"Total Chi_square: {total_chi_square}\n")
    print(f"Decision")

    critical_value = (round((chi2.isf(alpha, df=len(new_data) - 1)), 4))
    print(f"The null must be rejected if χ^2 < {critical_value}\n{bcolors.FAIL}")
    if total_chi_square > critical_value:
        print(f"Null 'Data fit to the distribution'  is Rejected and so Accept 'Data not fit to the distribution' ")
    else:
        print(f"Failure to reject Null 'Data fit to the distribution'  ")

    print(f"{bcolors.ENDC}")


