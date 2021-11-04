# _no = input(f"Enter the Raw data of \n")
# a = _no.strip().split(" ")
# data_ = [float(x) for x in a]
# no_ = len(data_)
# print(data_)

# 3 15 47 76 68 74 46 39 15 9 5 2 0 1
# 4 5 10 13 18 16 9 9 4 2
# 1 1 1 1 1 5 5 5


def slicing_(data, no):
    slicing = []
    shift = 0

    for i in range(0, no):
        shift = shift
        i = shift
        if i == no - 1 and data[i] < 5:
            slicing.append((no - 2, no - 1))
            break
        if i == no-1:
            break
        if data[i] < 5:
            initial = i
            final = 0
            sum_ = data[i]
            if i != no - 1:
                for j in range(i + 1, no):
                    sum_ += data[j]
                    if sum_ < 5:
                        final = j
                        if j != no-1:
                            continue
                        else:
                            initial = initial - 1
                    else:
                        final = j
                        break

                slicing.append((initial, final))
                shift = final + 1

            if final == no - 1:
                break
        else:
            shift = i+1

    # print(f"\nCombined categories (initial,final) {slicing}")
    return slicing


# slicing_(data_, no_)
