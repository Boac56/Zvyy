import platform

import psutil

my_system = platform.uname()




print("Welcome to Zvyy!")





while True:
    cmd = input("$~ ")
    if cmd == "cpu":
        print(f"Processor: {my_system.processor}")
    elif cmd == "kernel":
        print(f"Kernel: {my_system.release}")
    elif cmd == "python version":
        print(f"Python Version: {platform.python_version()}")
    elif cmd == "host":
        print(f"Host: {my_system.node}")
    elif cmd == "machine":
        print(f"Machine: {my_system.machine}")
    elif cmd == "system":
        print(f"System: {my_system.system}")
    elif cmd == "cpu_times":
        print(f"CPU Times: {psutil.cpu_times()}")
    elif cmd == "virtual_memory":
        print(f"Virtual Memory: {psutil.virtual_memory()}")
    elif cmd == "swap_memory":
        print(f"Swap Memory: {psutil.swap_memory()}")
    elif cmd == "disk_partitions":
        print(f"Disk Partitions: {psutil.disk_partitions()}")
    elif cmd == "disk_usage":
        print(f"Disk Usage: {psutil.disk_usage()}")
    elif cmd == "sensors_temperatures":
        print(f"Sensors Temperatures: {psutil.sensors_temperatures()}")
    elif cmd == "users":
        print(f"Users: {psutil.users()}")
    else:
        print("Unknown Command")