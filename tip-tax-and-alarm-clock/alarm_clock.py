# 24 HR Alarm Clock Calculator

current_hour = int(input("Enter the current time (0-23): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

alarm_hour = (current_hour + wait_hours) % 24

# Display result
print(f"The alarm will go off at {alarm_hour}:00")

