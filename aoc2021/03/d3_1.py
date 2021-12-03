with open("input.txt") as x:
    reports = x.read().splitlines()

gamma = ""
epsilon = ""
rotated_rates = zip(*reports)
for i, r in enumerate(rotated_rates):
    zc = r.count("0")
    oc = r.count("1")
    gamma += "0" if zc > oc else "1"
    epsilon += "1" if zc > oc else "0"

gamma_num = int(gamma, 2)
epsilon_num = int(epsilon, 2)

print(gamma_num * epsilon_num)
