import psutil as sys
import platform as plat
import time

valid = True

print("~"*15, "Welcome to TaskManagerCLI. What information do you want?", "~"*15)

while valid:
    try:
        print("[1. CPU Performance]")
        print("[2. Memory Performance]")
        print("[3. Disk Utilization]")
        print("[4. Quit]")
        answer = int(input())

        if answer == 1:
            print("~"*15, "CPU Performance", "~"*15)

            cpu = plat.processor()
            print("CPU:", cpu)

            physicalCount = sys.cpu_count(logical = False)
            logicalCount = sys.cpu_count(logical = True)
            print("CPU Core Count: Physical - ", physicalCount, "cores | Logical -", logicalCount, "cores")
            
            totalLoad = sys.cpu_percent(interval = 0.1, percpu = False)
            print("CPU Usage:", totalLoad, end="")
            print("%")

            ctxS = sys.cpu_stats().ctx_switches
            ints = sys.cpu_stats().interrupts
            sInts = sys.cpu_stats().soft_interrupts
            calls = sys.cpu_stats().syscalls
            print("CPU Stats: Context Switches -", ctxS, "| Interrupts -", ints, "| Software Interrupts -", sInts, "| System Calls -", calls)

            userLoad = round((sys.cpu_times(percpu = False).user / 60), 2)
            systemLoad = round((sys.cpu_times(percpu = False).system / 60), 2)
            idleLoad = round((sys.cpu_times(percpu = False).idle / 60), 2)
            print("CPU Uptime: User -", userLoad, "minutes | System -", systemLoad, "minutes | Idle -", idleLoad, "minutes")

            time.sleep(3)
            print("="*10, "What other information do you want? (Enter 4 to Quit)", "="*10)

        elif answer == 2:
            print("~"*15, "Memory Performance", "~"*15)

            memTotal = round((sys.virtual_memory().total / 1048576), 2)
            memAvail = round((sys.virtual_memory().available / 1048576), 2)
            memUsed = round((sys.virtual_memory().used / 1048576), 2)
            memFree = round((sys.virtual_memory().free / 1048576), 2)
            print("Memory: Total -", memTotal, "MB | Available -", memAvail, "MB | Used -", memUsed, "MB | Free -", memFree, "MB")

            swapTotal = round((sys.swap_memory().total / 1048576), 2)
            swapUsed = round((sys.swap_memory().used / 1048576), 2)
            swapFree = round((sys.swap_memory().free / 1048576), 2)
            print("Swap Memory: Total -", swapTotal, "MB | Used -", swapUsed, "MB | Free -", swapFree, "MB")

            time.sleep(3)
            print("="*10, "What other information do you want? (Enter 4 to Quit)", "="*10)

        elif answer == 3:
            print("~"*15, "Disk Utilization", "~"*15)

            diskTotal = round((sys.disk_usage("/").total / 1048576), 2)
            diskUsed = round((sys.disk_usage("/").used / 1048576), 2)
            diskFree = round((sys.disk_usage("/").free / 1048576), 2)
            print("Disk: Total -", diskTotal, "MB | Used -", diskUsed, "MB | Free -", diskFree, "MB")

            time.sleep(3)
            print("="*10, "What other information do you want? (Enter 4 to Quit)", "="*10)
        elif answer == 4:
            print("~"*15, "Shutting down...", "~"*15)
            valid = False
    except:
        print("[Enter a valid response (1-4).]")
        valid = True

