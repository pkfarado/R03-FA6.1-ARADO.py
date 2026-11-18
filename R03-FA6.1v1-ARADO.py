# Version 1: Basic Input and Output

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
event_year = input("Enter event year (YYYY): ")
event_month = input("Enter event month (1-12): ")
event_day = input("Enter event day (1-31): ")

print("\nStudent Event Registration Summary")
print("Name:", first_name, last_name)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_month + "/" + event_day + "/" + event_year)
print("Language Used: Python")
print("Registration record created successfully.")