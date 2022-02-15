import platform
import psutil as sys
import os

invalid = True

print("~"*10, "Welcome, what information do you seek?", "~"*10)
print("[1. CPU Performance]")
print("[2. Memory Performance]")
print("[3. Disk Utilization]")
print("[4. Quit]")

while invalid: 
    try:
        answer = int(input())

        if answer == 1:
            print("~"*10, "CPU Performance", "~"*10)
            print("CPU Usage: ", sys.cpu_percent(interval=3, percpu=False), "%")
            print("CPU Uptime: ", sys.cpu_times(percpu=False))
            print("What other information do you seek? (Enter 4 to Exit)")
        elif answer == 2:
            print("~"*10, "Memory Performance", "~"*10)
            
            print("What other information do you seek? (Enter 4 to Exit)")
        elif answer == 3:
            print("~"*10, "Disk Utilization", "~"*10)
            
            print("What other information do you seek? (Enter 4 to Exit)")
        elif answer == 4:
            print("~"*10, "Shutting down...", "~"*10)
            invalid = False
        else:
            print("Enter a valid option (1-4).")
            invalid = True

    except:
        print("Enter a valid option (1-4).")
        invalid = True

