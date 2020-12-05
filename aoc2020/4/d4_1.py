with open("input.txt") as x:
    lines = x.read().replace("\n", "|").split("||")

valid = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in lines:
    if all(req in passport for req in fields):
        valid += 1

print(valid)
