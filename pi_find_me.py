try:
    from sympy.mpmath import mp
except ImportError:
    from mpmath import mp

mp.dps = 100000
pi_value = str(mp.pi)

my_b_day = input("Enter your birthday in this format DayMonthYear: ")

position = pi_value.find(my_b_day)

digits_before_b_day = position

print(f"The number of digits before {my_b_day} in the value {pi_value} is: {digits_before_b_day}")

if "5389" in pi_value:
    print("It is your birthday")
else:
    print("It's not in here")

