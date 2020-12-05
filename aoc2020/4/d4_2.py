from re import match

with open("input.txt") as x:
    lines = x.read().strip().split("\n\n")
lines = [line.replace("\n", " ") for line in lines]

valid = 0

fields = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: match(r"^#[a-f0-9]{6}$", x), # match only matches from beginning of string
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: x.isnumeric() and len(x) == 9
        }

for passport in lines:
    pd = dict(tuple(i.split(":")) for i in passport.split())
    if all((field in pd.keys() and fields[field](pd[field])) for field in fields):
        valid += 1

print(valid)
