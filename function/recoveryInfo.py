from controller.system import System
from controller.hardware import Hardware

def recovery_info_system():
   os_system = System.get_system()
   os_platform = System.get_platform()
   os_version = System.get_version()
   os_user = System.get_user()
   os_disks = System.get_disks()
   os_network = System.get_network()
   os_result = [os_system, os_platform, os_version, os_user, os_disks, os_network]

   print(f"Recuperado informações do sistema com sucesso!")

   return os_result

def recovery_info_hardware():
   hw_cpu_info = Hardware.get_info_cpu()
   hw_cpu_arch = Hardware.get_arch()
   hw_cpu_frequency = Hardware.get_frequency_cpu()
   hw_cpu_nucleo = Hardware.get_nucleo_cpu()
   hw_memory_info = Hardware.get_memory()
   hw_result = [hw_cpu_info, hw_cpu_arch, hw_cpu_frequency, hw_cpu_nucleo, hw_memory_info]

   print(f"Recuperado informações do hardware com sucesso!")

   return hw_result