# Dinner Outing Total Calculator

food_charge = float(input("Enter the total food charge: ($):"))

tip = food_charge * 0.18
sales_tax = food_charge * 0.07
total_amount = food_charge + tip + sales_tax

# Display results with proper formatting
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")

