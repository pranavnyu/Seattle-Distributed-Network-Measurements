'''
implementing dig command using python 
link followed : https://docs.python.org/2/library/subprocess.html#module-subprocess
'''
import subprocess
import shlex


DNSlookup = 'dig FQDN' #DNS Lookups for Fully qualified domain Name
FQDN = raw_input("enter the ip address you want to apply dig on : ")
process =subprocess.Popen(shlex.split(DNSlookup), stdout=subprocess.PIPE)
out1,err=process.communicate()
print(out1)
