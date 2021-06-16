#!/usr/bin/env python3
# -*- coding: utf-8 -*-

IP = "10.10.10.1"
CONFIG_COMMENT='#'
CONFIG_NEWLINE='\n'

def generate_a_config(filename_in, filename_out, host_ip):
    domain_list=[]


    with open(filename_in, 'r') as fr, open(filename_out, 'w') as fw:
        for line in fr.read().splitlines():
            line_trimed = line.strip()
            # 注释原样写回
            if len(line_trimed) == 0 or line_trimed[0] == CONFIG_COMMENT:
                fw.write(line+CONFIG_NEWLINE)
            elif line_trimed[0] == ":" and line_trimed[-1] == ":":
                # regex
                fixDomain = line_trimed[1:-1]
                line = f"{host_ip} {fixDomain}"
                fw.write(line + CONFIG_NEWLINE)
            else:
                fix_domain = line_trimed.strip(".")
                line = f"{host_ip} .*{fix_domain}$"
                fw.write(line + CONFIG_NEWLINE)

generate_a_config("domains_blocked.txt","domains_blocked.conf", IP)
