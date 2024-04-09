# Take float user input in Python

# ✅ Take user input float value
user_input = float(input('Enter a float: '))
print(user_input)

# ------------------------------------------------

# ✅ Take user input float value with validation
try:
    user_input = float(input('Enter a float: '))
    print(user_input)
except ValueError:
    print('Enter a valid float')