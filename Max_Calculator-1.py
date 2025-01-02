# Cosmetic
bold = '\033[1m'
cyan = '\33[36m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'

# Input Values
D1 = float(input(italic + bold + "D1 = "))
D2 = float(input(italic + bold + "D2 = "))
D3 = float(input(italic + bold + "D3 = "))
Weight = float(input(italic + bold + "Weight = "))

# Condition checking if X, Y, or Z are negative
def negative_check(value): 
 return max(0,value)

Fail = 0 
Pass = 0
Results = []

# Output Values and Threshold Messages for X, Y, and Z
def value_check_1(name, value, threshold):
  global Pass, Fail
  if value == 0:
   Results.append(bold+italic+cyan+f"Recheck {name}:\nif correct, {name} = 0 and passed"+end)
  elif value > threshold:
    Fail += 1
    Results.append(bold+italic+red+f"{name} Failed:\n{name} = {value:.4f}\nThreshold = {threshold:.3f}"+end)
  else:
    Pass += 1
    Results.append(bold+italic+green+f"{name} Passed:\n{name} = {value:.4f} \nThreshold = {threshold:.3f}"+end) 

# Output Values and Threshold Messages for H only
def value_check_2(name, value, threshold):
  global Fail, Pass
  if value > threshold:
    Fail += 1
    Results.append(bold+italic+red+f"{name} Failed:\n{name} = {value:.4f}\nThreshold = {threshold:.3f}"+end)
  else:
    Pass += 1
    Results.append(bold+italic+green+f"{name} Passed:\n{name} = {value:.4f}\nThreshold = {threshold:.3f}"+end) 

# Overall Calculations
X = negative_check(D1-(Weight*0.0000155))
Y = negative_check(D2-(Weight *0.0000155))
Z = negative_check((D3*1.25)-(Weight*0.0000318))
H = Z+((X+Y)/2)

# Threshold Checks
value_check_1("X", X, 0.060)
value_check_1("Y", Y, 0.060)
value_check_1("Z", Z, 0.050)
value_check_2("H", H, 0.051)

# Summary of Results
if Pass == 4: 
 print(bold+italic+green+"All values passed"+end)
elif Fail == 4:
  print(bold+italic+red+"All values failed"+end)
else: 
  for result in Results:
    print(result)