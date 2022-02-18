import platform as pl
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

            cpu = pl.processor()
            print("CPU: ", cpu)

            physicalCount = sys.cpu_count(logical=False)
            logicalCount = sys.cpu_count(logical=True)

            print("CPU Core Count: Physical -", physicalCount, "cores | Logical -", logicalCount, "cores")

            totalLoad = sys.cpu_percent(interval=0.1, percpu=False)
            
            print("CPU Usage:", totalLoad, end="")
            print("%")

            ctxS = sys.cpu_stats().ctx_switches
            ints = sys.cpu_stats().interrupts
            sInts = sys.cpu_stats().soft_interrupts
            calls = sys.cpu_stats().syscalls

            print("CPU Stats: Context Switches -", ctxS, "| Interrupts -", ints, "| Software Interrupts -", sInts, "| System Calls -", calls)

            userLoad = sys.cpu_times(percpu=False).user
            systemLoad = sys.cpu_times(percpu=False).system
            idleLoad = sys.cpu_times(percpu=False).idle

            print("CPU Uptime: User -", userLoad, "seconds | System -", systemLoad, "seconds | Idle -", idleLoad, "seconds")

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
