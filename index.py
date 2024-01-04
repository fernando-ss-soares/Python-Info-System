import csv
from function.recoveryInfo import recovery_info_system
from function.recoveryInfo import recovery_info_hardware

print(f"Recuperando informações do sistema...")

system = recovery_info_system()
hardware = recovery_info_hardware()

print(f"Gerando relatórios...")

with open("system.csv","w",newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['os_system', 'os_platform', 'os_version', 'os_user', 'os_disks', 'os_network'])
    spamwriter.writerow([system[0], system[1], system[2], system[3], system[4], system[5]])

with open("hardware.csv","w",newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['hw_cpu_info', 'hw_cpu_arch', 'hw_cpu_frequency', 'hw_cpu_nucleo', 'hw_memory_info'])
    spamwriter.writerow([hardware[0], hardware[1], hardware[2], hardware[3], hardware[4]])