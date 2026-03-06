import os

from typing import List

FILE_NAME: str = "access.log"
observed_ips: List[str] = []

def get_absolute_file_path(file_name: str) -> str:

    if isinstance(file_name, str) and os.path.exists(file_name) and os.path.isfile(file_name):
        return os.path.abspath(file_name)
    
    else:
        raise Exception("Arquivo inválido! Forneça o nome de um arquivo de log válido!")


file_path: str = get_absolute_file_path(FILE_NAME)

with open(file_path, "r") as file:
    for line in file:
        if "404" in line.split(" "):
            observed_ips.append(line.split(" ")[0])


print("IPs que fixeram requições suspeitas:")

for ip in observed_ips:
    print(ip)