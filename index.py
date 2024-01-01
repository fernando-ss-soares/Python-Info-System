import platform
import psutil

print(f"Sistema Operacional: {platform.system()}")
print(f"Plataforma: {platform.platform()}")
print(f"Maquina: {platform.machine()}")
print(f"Arquitetura: {platform.architecture()}")
print(f"Processor: {platform.processor()}")
print(f"Frequência do Processador: {psutil.cpu_freq()}")
print(f"Quantidade de Núcleos: {psutil.cpu_count()}")
