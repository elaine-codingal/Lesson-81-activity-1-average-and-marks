# Import the necessary library for data visualization
import matplotlib.pyplot as plt  # Matplotlib for plotting graphs

# Define a list of student names
students_names = ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]

# Define corresponding marks obtained by students out of 50
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

# Initialize an empty list to store percentage values
marks_perc = []

# Calculate percentage for each student (marks obtained out of 50)
for x in students_marks:
    res = (x / 50) * 100  # Convert marks to percentage
    marks_perc.append(res)  # Append the result to the list

# Print the calculated percentage values
print(marks_perc)

# Function to plot a line chart of students' marks
def line_chart_of_students_and_marks():
    plt.plot(students_names, students_marks, marker='o', linestyle='-')  # Plot a line graph with markers
    plt.title("Students Marks Graph")  # Set title of the graph
    plt.xlabel("Students Names")  # Label for x-axis
    plt.ylabel("Students Marks")  # Label for y-axis
    plt.grid(True)  # Enable grid for better visualization
    plt.show()  # Display the plot

# Call the function to display the line chart
line_chart_of_students_and_marks()

# Function to plot a bar chart of students' percentages
def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='skyblue')  # Create a bar chart with a specific color
    plt.title("Students' Percentage Graph")  # Set title of the graph
    plt.xlabel("Student Names")  # Label for x-axis
    plt.ylabel("Student Percentage")  # Label for y-axis
    plt.ylim(0, 100)  # Set y-axis limit to 0-100 for percentage scale
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add a grid for better readability
    plt.show()  # Display the plot

# Call the function to display the bar chart
percentage_bar_chart()
