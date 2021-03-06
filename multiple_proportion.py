from scipy.stats import chi
from color import *
from prettytable import PrettyTable
table = PrettyTable(['Observed Frequency', 'Expected Observed Frequency', 'Contribution to χ^2'])


def multiple_proportion():
    k = int(input("No of proportions: "))
    alpha = float(input("Level of significance: "))

    data = []
    print("\n")
    print("Data Format")
    print("1. Total_no and Success")
    print("2. Success and Failures")
    selection = int(input())
    if selection == 1:
        for i in range(0, k):
            a = dict()
            a["no"] = int(input(f"Total No of p{i + 1}: "))
            a["success"] = int(input(f"No of success of p{i + 1}: "))
            print("\n")
            a["failures"] = a["no"] - a["success"]
            data.append(a)

    elif selection == 2:
        for i in range(0, k):
            a = dict()
            a["success"] = int(input(f"No of success of p{i + 1}: "))
            a["failures"] = int(input(f"No of failures of p{i + 1}: "))
            print("\n")
            a["no"] = a["success"] + a["failures"]
            data.append(a)
    else:
        print("Invalid")
        exit(0)

    total_success = 0
    total_failures = 0
    for each in data:
        total_success += each["success"]
        total_failures += each["failures"]

    total_no = total_success + total_failures

    print(f"\n{bcolors.OKCYAN}Testing Alternative Hypothesis p1!=p2!=p3.....!=pk against Null Hypothesis "
          f"p1=p2=p3.....=pk  {bcolors.ENDC}")

    total_chi_square = 0
    for each in data:
        each["exp_success"] = each["no"]*(total_success/total_no)
        each["exp_failures"] = each["no"] * (total_failures / total_no)
        total_chi_square += (each["success"]-each["exp_success"])**2/(each["exp_success"]) +\
                            (each["failures"] - each["exp_failures"]) ** 2 / (each["exp_failures"])

        table.add_row([each["success"], each["exp_success"], (each["success"]-each["exp_success"])**2/(each["exp_success"])])
        table.add_row([each["failures"], each["exp_failures"],
                      (each["failures"] - each["exp_failures"]) ** 2 / (each["exp_failures"])])

    print(f"\n{table}\n")
    test_statistics_value = total_chi_square

    critical_value = (round((chi.isf(alpha, df=k - 1)) ** 2, 4))
    print(f"The null must be rejected if χ^2>{critical_value}\n")
    print("Calculations\n")
    print(f"χ^2 = {test_statistics_value}\n")
    print("Decision\n")

    if test_statistics_value > critical_value:
        print(f"Null p1=p2=p3.....=pk  must be Rejected at level of significance {alpha} and Accept p1!=p2!=p3.....!=pk")
    else:
        print(f"Failure to reject Null p1=p2=p3.....=pk ")
