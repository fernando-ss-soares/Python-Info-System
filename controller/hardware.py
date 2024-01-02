import platform
import psutil

class Hardware:
    def get_info_cpu():
        return platform.processor()

    def get_nucleo_cpu():
        return psutil.cpu_count()

    def get_frequency_cpu():
        return psutil.cpu_freq(percpu=True)
    
    def get_arch():
        return platform.architecture()
    
    def get_memory():
        return psutil.virtual_memory()