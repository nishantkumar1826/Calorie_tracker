# Task 1: Welcome Message
print("Welcome to Daily Calorie Tracker!")
print("This tool helps you record your meals, calculate total calories compare with your daily limit, and optionally save your session")
# Task 2: Input & Data Collection
meals = []
calories = []
num_meals = int(input("How many meals did you have today? "))
for i in range(num_meals):
    print(f"\nEnter details for meal {i + 1}:")
    meal_name = str(input("Meal name: "))
    calorie_amount = float(input("Calories (in kcal): "))
    meals.append(meal_name)
    calories.append(calorie_amount)
# Task 3: Calorie Calculation
total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))
 # Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    status_message = " You have exceeded your daily calorie limit!"
else:
    status_message = " You are within your daily calorie limit."

# Task 5: Summary Output
# -------------------------------
print("\n----------- DAILY SUMMARY REPORT -----------\n")
print("Meal Name            Calories")
print("--------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}              {calories[i]}")

print("--------------------------------------------")
print(f"Total:               {total_calories}")
print(f"Average:             {average_calories}")
print(f"Status:              {status_message}")
print("--------------------------------------------")