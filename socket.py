'''
implementing dig command using python 
link followed : https://docs.python.org/2/library/subprocess.html#module-subprocess
'''
import subprocess
import shlex

NAME_SERVER_IP ="@8.8.8.8" #it is the server to be queried by default

DNSlookup = 'dig NAME_SERVER_IP FQDN' #DNS Lookups for Fully qualified domain Name
FQDN = raw_input("enter the ip address you want to apply dig on : ")
# cmd='dig @ns1.netnames.net www.rac.co.uk CNAME'
process =subprocess.Popen(shlex.split(DNSlookup), stdout=subprocess.PIPE)
out1,err=process.communicate()
print(out1)

'''
DNSconfig = 'dig NAMESERVER FQDN'
NAMESERVER = raw_input("enter the nameserver : ")
process =subprocess.Popen(shlex.split(DNSconfig), stdout=subprocess.PIPE)
out2,err=process.communicate()
print(out2)
'''