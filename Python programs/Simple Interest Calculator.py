def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

print("Simple Interest:", simple_interest(principal, rate, time))
