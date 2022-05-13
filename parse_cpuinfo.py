from rich import print
from typing import List


def parse_cpuinfo(cpu_info_file: str = '/proc/cpuinfo') -> List[dict]:

    all_cores = []
    core_dict = {}

    # Open the cpu_info file.
    with open(cpu_info_file, 'r') as cpuinfo:

        core_line = cpuinfo.readlines()
        for line in core_line:
            if line != '\n':
                line_id, content = line.split(":")
                if ' ' in line_id:
                    line_id = line_id.replace(' ', '_')
                core_dict[line_id.strip()] = content.strip()

            else:
                all_cores.append(core_dict)
                core_dict = {}

    return all_cores

def parse_meminfo(mem_info_file: str = '/proc/meminfo'):
    meminfo = {}
    with open(mem_info_file, 'r') as mem_lines:
        for line in mem_lines:
            item, value = line.split(':')
            meminfo[item] = value.strip()

    return meminfo

print(parse_cpuinfo())

