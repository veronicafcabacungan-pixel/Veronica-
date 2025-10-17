# Task 1: The Basic Calculator
a = 15
b = 4

print(f"a = {a}, b = {b}")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Floating-Point Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# Task 2: Order of Operations Challenge
result1 = 5 + 3 * 2 ** 2
result2 = (5 + 3) * 2 ** 2
result3 = 10 % 3 + 5 * 2

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)


# Task 3: Unit Conversion Challenge
inches = int(input("Enter the number of inches: "))
feet = inches // 12
remaining_inches = inches % 12

print(f"{inches} inches is equal to {feet} feet and {remaining_inches} inches.")


# Task 4: Movie Ticket Price Decider
age = 20
is_student = True

base_price = 12

if age <= 12:
    discount = 3
elif age >= 65:
    discount = 4
elif is_student:
    discount = 2
else:
    discount = 0

final_price = base_price - discount

print(f"Age: {age}")
print(f"Is student? {is_student}")
print(f"Your ticket price is ${final_price}.")


# Task 5: Secure System Login Simulator
correct_username = "Alice"
correct_password = "wonderland"
is_2fa_enabled = True
correct_2fa_code = "123456"

input_username = input("Enter username: ")
input_password = input("Enter password: ")
two_fa = input("Is 2FA enabled? (y/n): ").lower()
input_2fa_code = ""

if two_fa == "y":
    input_2fa_code = input("Enter 2FA code: ")

if (input_username == correct_username and
    input_password == correct_password and
    ((not is_2fa_enabled) or (input_2fa_code == correct_2fa_code))):
    print("Login successful!")
else:
    print("Login failed!")
    
    
   # Bonus Challenge: Shipping Cost Calculator with Predefined Values
# Prompt user for input (filled with exact variable values)
weight = 25
destination = "international"
membership = "premium"

# Base cost and conditions
base_cost = 10
extra_cost = 5 if weight > 20 else 0
total_cost = base_cost + extra_cost

# Apply international fee if applicable
if destination == "international" and membership != "premium":
    total_cost *= 2

# Apply premium discount if applicable
if membership == "premium":
    total_cost *= 0.8  # 20% discount

# Display detailed breakdown
print("--- Shipping Summary ---")
print(f"Weight (lbs): {weight}")
print(f"Destination (domestic/international): {destination}")
print(f"Membership (standard/premium): {membership}")
print(f"Final Shipping Cost: ${total_cost:.2f}")
print("(Details: Base $10 + Overweight $5, Premium 20% discount applied, International fee waived.)")
