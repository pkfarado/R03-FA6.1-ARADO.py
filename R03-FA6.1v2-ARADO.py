# Version 2: Added String Formatting

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
event_year = input("Enter event year (YYYY): ")
event_month = input("Enter event month (1-12): ")
event_day = input("Enter event day (1-31): ")

clean_first = first_name.strip().title()
clean_last = last_name.strip().title()
full_name = f"{clean_first} {clean_last}"
name_code = full_name.upper()
clean_section = section.strip().upper()
clean_event = event_name.strip().title()

print("\nStudent Event Registration Summary")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {clean_section}")
print(f"Event: {clean_event}")
print(f"Event Date: {event_month.strip()}/{event_day.strip()}/{event_year.strip()}")
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Registration record created successfully.")