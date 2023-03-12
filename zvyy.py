import platform
import sys
import psutil
my_system = platform.uname()
print("Welcome to Zvyy!")
print("Note: made for fun.")
print("Type 'cmds' to see a list of commands")
while True:
    cmd = input("$~ ")
    if cmd == "cpu":
        print(f"Processor: {my_system.processor}")
    elif cmd == "cmds":
        print('Command List: exit, kernel, python_version, host, machine, system, cpu_times, virtual_memory, swap_memory, disk_partitions, disk_usage, sensors_temperatures, users')
    elif cmd == "kernel":
        print(f"Kernel: {my_system.release}")
    elif cmd == "python_version":
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
    elif cmd == "exit":
        print(sys.exit())
    else: print("Unknown Command")
