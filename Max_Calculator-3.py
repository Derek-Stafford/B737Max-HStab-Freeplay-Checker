from tabulate import tabulate
# Cosmetic
bold = '\033[1m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'
yellow ='\033[38;5;226m'

# Input Values
D1 = float(input(italic+bold+"D1 = "))
D2 = float(input(italic+bold+"D2 = "))
D3 = float(input(italic+bold+"D3 = "))
Weight = float(input(italic+bold+"Weight = "))

# Conditons for if X, Y, or Z are negative
def negative_check(value): 
	if value < 0:
			return 0
	else:
			return value

# Output Values and Threshold Messages
def individual_check(name, value, threshold):
 if value == 0:
	 return italic+bold+yellow+f"Re-Check {name}"+end
 elif value > threshold:
		return italic+bold+red+f"{name} Failed"+end
 else:
		return italic+bold+green+f"{name} Passed"+end

def overall_check(name, value, threshold):
	if value > threshold:
			return italic+bold+red+f"{name} Failed"+end
	else:
			return italic+bold+green+f"{name} Passed"+end

# Calculations
X = negative_check(D1-(Weight * 0.0000155))
Y = negative_check(D2-(Weight *  0.0000155))
Z = negative_check((D3*1.25)- (Weight * 0.0000318))
H = Z+((X + Y)/2)
equation = [
	["X = (D1-(Weight*0.0000155))", X],
	["Y = (D2-(Weight*0.0000155))", Y],
	["Z = (D3-(Weight*0.0000318))", Z],
	["H = Z+((X+Y)/2)", H]
]
head_2= ["Formula", "Result"]
print (tabulate(equation, headers =head_2, tablefmt="grid"))
# Threshold Checks
final = [
 ["X", f"{X:.4f}", 0.060, individual_check("X",X,0.060)],
 ["Y", f"{Y:.4f}", 0.060, individual_check("Y",Y,0.060)],
 ["Z", f"{Z:.4f}", 0.050, individual_check("Z", Z, 0.050)],
 ["H", f"{H:.4f}",0.051,  overall_check("H", H, 0.051)]
]
head_3 = ["Var.", "Output","Limit", "Result"]
print(tabulate(final, headers = head_3, tablefmt = "grid"))
