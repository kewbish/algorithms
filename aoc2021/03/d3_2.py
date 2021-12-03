with open("input.txt") as x:
    reports = x.read().splitlines()


def find_rate(reports, condition) -> int:
    rates = reports
    i = 0
    while len(rates) != 1:
        rotated_rates = list(zip(*rates))
        zc = rotated_rates[i].count("0")
        oc = rotated_rates[i].count("1")
        rates = list(filter(lambda rate: rate[i] == condition(zc, oc), rates))
        i += 1
    rate = int(rates[0], 2)
    return rate


oxy = find_rate(reports, lambda zc, oc: "0" if zc > oc else "1")
co2 = find_rate(reports, lambda zc, oc: "0" if zc <= oc else "1")
print(oxy * co2)
