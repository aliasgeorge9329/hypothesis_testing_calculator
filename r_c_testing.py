from scipy.stats import chi
from prettytable import PrettyTable
from color import *
table = PrettyTable(['Element Name', 'Observed Frequency'])


def r_c_testing():
    r = int(input("No of rows: "))
    c = int(input("No of columns: "))
    alpha = float(input("Level of significance: "))

    data = []
    print("\n")
    for i in range(0, c):
        a = dict()
        a["no"] = 0
        print(f"Enter the column_{i+1} details")
        for j in range(0, r):
            a[f"{j}"] = int(input(f"Enter the e{j+1}{i+1}: "))
            a["no"] += a[f"{j}"]
            table.add_row([f"e{j + 1}{i + 1}", a[f"{j}"]])
        print("\n")
        data.append(a)

    total = []

    for i in range(0, r):
        total_no = 0
        for j in range(0, c):
            total_no += data[j][f"{i}"]

        total.append(total_no)

    total_num = sum(total)

    print(f"\n{bcolors.OKCYAN}Testing alternative Hypothesis both are dependent against the Null both are independent"
          f"{bcolors.ENDC}")

    total_chi_square = 0
    exp_f = []
    contribution_to_chi2 = []
    for each in data:
        for j in range(0, r):
            each[f"exp_{j}"] = each["no"] * (total[j] / total_num)
            exp_f.append(each[f"exp_{j}"])
            b = round((each[f"{j}"] - each[f"exp_{j}"]) ** 2 / (each[f"exp_{j}"]), 3)
            total_chi_square += b
            contribution_to_chi2.append(b)

    table.add_column('Expected Frequency', exp_f)
    table.add_column('Contribution to χ^2', contribution_to_chi2)

    test_statistics_value = total_chi_square

    critical_value = (round((chi.isf(alpha, df=(r-1)*(c-1))) ** 2, 4))
    print(f"The null must be rejected if χ^2>{critical_value}\n")
    print("Calculations\n")
    print(table)
    print(f"\nχ^2 = {test_statistics_value}\n")
    print(f"Decision\n{bcolors.FAIL}")
    if test_statistics_value > critical_value:
        print(f"Null both are Independent must be Rejected at level of significance {alpha} and Accept both are dependent on each other")
    else:
        print(f"Failure to reject Null both are Independent is Rejected ")

    print(f"{bcolors.ENDC}")