from scipy.stats import chi
from color import *


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
    for each in data:
        for j in range(0, r):
            each[f"exp_{j}"] = each["no"] * (total[j] / total_num)
            total_chi_square += (each[f"{j}"] - each[f"exp_{j}"]) ** 2 / (each[f"exp_{j}"])

    test_statistics_value = total_chi_square

    critical_value = (round((chi.isf(alpha, df=(r-1)*(c-1))) ** 2, 4))
    print(f"The null must be rejected if χ^2>{critical_value}\n")
    print("Calculations\n")
    print(f"χ^2 = {test_statistics_value}\n")
    print("Decision\n")
    if test_statistics_value > critical_value:
        print(f"Null both are Independent must be Rejected at level of significance {alpha} and Accept both are dependent on each other")
    else:
        print(f"Failure to reject Null both are Independent is Rejected ")
