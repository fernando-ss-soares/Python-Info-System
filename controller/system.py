import platform
import psutil

class System:
    def get_system():
        return platform.system()
    
    def get_version():
        return platform.version()
    
    def get_platform():
        return platform.platform()
    
    def get_user():
        return platform.node()
    
    def get_network():
        return psutil.net_if_addrs()
    
    def get_network_connections():
        return psutil.net_connections()
    
    def get_disks():
        return psutil.disk_partitions()