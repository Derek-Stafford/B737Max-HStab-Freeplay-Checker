# Cosmetic
bold = '\033[1m'
cyan = '\33[36m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'
# Input values
D1 = float(input(bold+italic+"D1 = "+end))
D2 = float(input(bold+italic+"D2 = "+end))
D3 = float(input(bold+italic+"D3 = "+end))
Weight = float(input(bold+italic+"Weight = "+end))
# creates table
print(f"{'Variable': <10} {'Value': <10} {'Threshold': <10} {'Result': <10}")
print("-"*40)

# Sets X, Y, and Z to either 0 if it's negative or keeps it's value if positive
def negative_check (value):
  return max(0,value)

# Used specifically for X, Y, and Z
def value_check_1 (value,threshold):
  global Pass, Fail
  if value == 0:
    return bold+italic+cyan+"Recheck but Passed"+end
  elif value > threshold:
    return bold+italic+red+"Failed"+end
  else:
    return bold+italic+green+"Passed"+end

# Used specifically for H
def value_check_2 (value,threshold):
  if value > threshold:
   return bold+italic+red+"Failed"+end
  else:
   return bold+italic+green+"Passed"+end
    
# Calculations
X = negative_check(D1-(Weight*0.0000155))
Y = negative_check(D2-(Weight*0.0000155))
Z = negative_check((D3*1.25)-(Weight*0.0000318))
H = Z+((X+Y)/2)

# Structured representstion for each value. The structure is (Name, Value, Threshold, Reault)
rows = [
  ("X", f"{X:.4f}", "0.060", value_check_1(X, 0.060)),
  ("Y", f"{Y:.4f}", "0.060", value_check_1(D2, 0.060)),
  ("Z", f"{Z:.4f}", "0.050", value_check_1(D3, 0.050)),
  ("H", f"{H:.4f}", "0.051", value_check_2(H, 0.051)),
]

# Used to print the table
for var, value, limit, result in rows:
  print(f"{var:<10} {value:<10} {limit:<10} {result:<10}")