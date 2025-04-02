#Import library
import matplotlib.pyplot as plt

# Occupations and corresponding wages
occupations = ["Software Engineer", "Nurse", "Electrician", "CEO"]
wages = [90000, 55000, 60000, 200000]  

# Calculate percentage of the max wage 
wages_percentage = []
max_wage = max(wages)
for wage in wages:
    res = (wage / max_wage) * 100
    wages_percentage.append(res)
print(wages_percentage)

# Line chart for wages
def wages_line_chart():
    plt.plot(occupations, wages, marker='o')
    plt.title("Occupation Wages Line Chart")
    plt.xlabel("Occupations")
    plt.ylabel("Wages (USD)")
    plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability
    plt.show()

wages_line_chart()

# Bar chart for wages percentage
def percentage_bar_chart():
    plt.bar(occupations, wages_percentage, color='green')
    plt.title("Occupation Wages Percentage Graph")
    plt.xlabel("Occupations")
    plt.ylabel("Wage Percentage")
    plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability
    plt.show()

percentage_bar_chart()
