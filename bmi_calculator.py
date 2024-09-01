print("Welcome to the BMI Calculator!")

# Input weight and height from the user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = round(weight / (height ** 2), 1)
status = ""
suggestion = ""

# Determine BMI category and provide suggestions
if bmi <= 18.4:
    status = "Underweight"
    suggestion = "You may need to gain weight for better health. Consider consulting with a healthcare provider or nutritionist to develop a balanced diet plan."
elif 18.5 <= bmi <= 24.9:
    status = "Normal"
    suggestion = "Great job! You're in the healthy weight range. Keep up with your current diet and exercise routine to maintain your health."
elif 25.0 <= bmi <= 29.9:
    status = "Overweight"
    suggestion = "You may benefit from losing some weight for better health. Consider a balanced diet and regular exercise. Consult a healthcare provider for personalized advice."
else:
    status = "Obese"
    suggestion = "It is advisable to lose weight to reduce the risk of health issues. Consult with a healthcare provider to create a safe and effective weight loss plan."

# Display results
print(f"\nYour BMI is: {bmi}")
print(f"Status: {status}")
print(f"Suggestion: {suggestion}")
