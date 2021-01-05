def add_time(start, duration, weekday=None):
    
    new_time = ""

    hours = int(start.replace(" ", ":").split(":")[0])
    minutes = int(start.replace(" ", ":").split(":")[1])
    clock_format = start.replace(" ", ":").split(":")[2]

    duration_minutes = (int(duration.split(":")[0]) * 60) + (int(duration.split(":")[1]))
    days = 0
    
    while duration_minutes > 0:
        minutes += 1

        if minutes > 59:
            hours += 1
            minutes = 0

            if hours == 12 and clock_format == "PM":
                clock_format = "AM"

            elif hours == 12 and clock_format == "AM":
                clock_format = "PM"
  
            if hours == 12 and minutes == 0 and clock_format == "AM":
                days += 1

            if hours > 12:
                hours = 1

        duration_minutes -= 1
    
    new_time += f"{hours}:{0 if minutes < 10 else ''}{minutes} {clock_format}" 

    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]

    if weekday and days == 0:
        new_time += f", {weekday}"
    
    if weekday and days == 1:
        new_time += f", {weekday_list[(weekday_list.index(weekday.lower().capitalize()) + 1)]} (next day)"

    if weekday and days > 1:
        day = weekday_list.index(weekday.lower().capitalize())
        weekday_list = (weekday_list*int(((day + days + 1) / len(weekday_list)) + ((day + days + 1) % len(weekday_list) > 0)))
        new_time += f", {weekday_list[day + days]} ({days} days later)"

    if not weekday and days == 1:
        new_time += f" (next day)"

    if not weekday and days > 1:
        new_time += f" ({days} days later)"

    return new_time


run = True

start_hours = ""
start_minutes = ""
clock_format = ""

added_hours = ""
added_minutes = ""

while run:

    while True:
        try:
            hours = int(input("Enter the start time in an hour (0 - 12): "))
            if 0 <= hours <= 12:
                start_hours = str(hours)
                break
        except ValueError:
            print("Enter correct start hour (0 - 12)!")
    
    while True:
        try:
            minutes = int(input("Enter the start time in a minutes (0 - 59): "))
            if 0 <= minutes <= 59:
                start_minutes = str(minutes)
                break
        except ValueError:
            print("Enter correct start time in minutes (0-59)!")
        
    while True:
        try:
            format = input("Enter clock format ('PM' or 'AM'): ")
            if format == "PM" or format == "AM":
                clock_format = format
                break
        except TypeError:
            print("Enter correct clock format (PM or AM)!")
        
    print()

    while True:
        try:
            add_hour = int(input("Enter added time in an hour: "))
            if 0 <= add_hour: 
                added_hours = str(add_hour)
                break
        except ValueError:
            print("Enter correct added time in hours")
        
    while True:
        try:
            add_minute = int(input("Enter added time in minutes (0 - 59): "))
            if 0 <= add_minute <= 59:
                added_minutes = str(add_minute)
                break
        except ValueError:
            print("Enter correct added time in minutes (0 - 59)!")

    print()

    while True:
        try:
            day = input("Entering the day of the week is optional (example 'Sunday'): ")
            if day.lower().capitalize() in ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]:
                weekday = day
                break
        except TypeError:
            print("Enter an existing day of the week")

    print()

    if weekday:
        
        final_time = add_time(f"{start_hours}:{start_minutes} {clock_format}", f"{added_hours}:{added_minutes}", f"{weekday}")
        print(f"Calculated time: {final_time}")
    else:
        final_time = add_time(f"{start_hours}:{start_minutes} {clock_format}", f"{added_hours}:{added_minutes}")
        print(f"Calculated time: {final_time}")

    while True:
        try:
            again = input("Do you want to calculate time again? (Y or N): ")
            if again == "Y" or again == "y":
                break
            if again == "N" or again == "n":
                run = False
        except TypeError:
            print("Enter correct letter!")

    print()

