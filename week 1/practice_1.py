# Simple Interest
def simple_interest(P, R, T):
    return P * (1 + (R / 100) * T)

# Compound Interest
def compound_interest(P, R, n, t):
    return P * (1 + R / (100 * n)) ** (n * t)

# Annuity Plan
def annuity_plan(PMT, R, n, t):
    r = R / (100 * n)
    return PMT * ((1 + r) ** (n * t) - 1) / r

# Get user input
P = float(input("Enter Principal: "))
R = float(input("Enter Interest Rate (%): "))
T = float(input("Enter Time (years): "))
n = int(input("Enter Compounding Periods per Year: "))
PMT = float(input("Enter Annuity Payment: "))

# Display results
print("\nSimple Interest:", simple_interest(P, R, T))
print("Compound Interest:", compound_interest(P, R, n, T))
print("Annuity Plan:", annuity_plan(PMT, R, n, T))
