# Cosmetic
bold = '\033[1m'
cyan = '\033[36m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'

# Input Values
D1 = float(input(italic+bold+"D1 = "+end))
D2 = float(input(italic+bold+"D2 = "+end))
D3 = float(input(italic+bold+"D3 = "+end))
Weight = float(input(italic+bold+"Weight = "+end))

# Condition checking if X, Y, or Z are negative
def negative_check(value):
  return max(0, value)

# Calculations
X = negative_check(D1-(Weight*0.0000155))
Y = negative_check(D2-(Weight*0.0000155))
Z = negative_check((D3*1.25)-(Weight*0.0000318))
H = Z+((X+Y)/2)

# Thresholds and Values
Thresholds = {
  "X": 0.060,
  "Y": 0.060,
  "Z": 0.050,
  "H": 0.051
}
Values = {
  "X": X,
  "Y": Y,
  "Z": Z,
  "H": H
}

# Results Storage and Counter
Pass = 0
Fail = 0
Results = []

# Check values against thresholds
for name, value in Values.items():
  if value > Thresholds[name]:
    Fail += 1
    Results.append(bold+italic+red + f"{name} failed: {value:.4f} (threshold = {Thresholds[name]})"+end)
  else:
    Pass += 1
    Results.append(bold+italic+green + f"{name} passed: {value:.4f} (threshold = {Thresholds[name]})"+end)

# Final Output
if Pass == 4:
  print(bold+italic+green+"All values passed"+end)
elif Fail == 4:
  print(bold+italic+red+"All values failed"+end)
else:
  for result in Results:
    print(result)