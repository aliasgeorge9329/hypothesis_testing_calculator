from slicing import *


def combining(data, no):
    # Reduction
    slicing = []
    for each in data:
        slicing.append(each["obf"])
    slicing = slicing_(slicing, no)

    print(f"\nCombined categories (initial,final) {slicing}")

    new_data = []

    if len(slicing) != 0:
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

            if final == no - 1 or slicing.index(each) == len(slicing) - 1:
                break

            else:
                new_initial = slicing[slicing.index(each) + 1][0]
                for i in range(final + 1, new_initial):
                    a = dict()
                    a["obf"] = data[i]["obf"]
                    a["probability"] = data[i]["probability"]
                    a["exp_obf"] = data[i]["exp_obf"]
                    new_data.append(a)

        if slicing[len(slicing) - 1][1] != no - 1:
            for i in range(slicing[len(slicing) - 1][1] + 1, no):
                a = dict()
                a["obf"] = data[i]["obf"]
                a["probability"] = data[i]["probability"]
                a["exp_obf"] = data[i]["exp_obf"]
                new_data.append(a)

    else:
        for i in range(0, no):
            a = dict()
            a["obf"] = data[i]["obf"]
            a["probability"] = data[i]["probability"]
            a["exp_obf"] = data[i]["exp_obf"]
            new_data.append(a)

    return new_data
