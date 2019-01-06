import os #check environment var for debug
import re
from db_util import NewDb_util
# =============================================================================
# #db=Db_util(host="localhost",user="root",db="dns")
# =============================================================================
db=NewDb_util()
domainReg=re.compile("^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]\.)*([A-zA-Z0-9]|[A-zA-Z0-9][A-zA-Z0-9\-]*[A-zA-Z0-9]))$")
ipReg=re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")

# =============================================================================
# #clears databaes fore testing
# =============================================================================
def clearDb():
    db.clearDb()
# =============================================================================
# #validate ip with compiled regex
# =============================================================================
def validateIp(ip):
    try: return re.match(ipReg,ip) != None #regex returns None if no match so: Match=true
    except: return False
# =============================================================================
# #validate ip with comoiled regex
# =============================================================================
def validateDomain(domain):
    try: return re.match(domainReg,domain) != None #regex returns None if no match so: Match=true
    except: return False
# =============================================================================
# #set create entry with only ip
# =============================================================================
def setDomain(domain):
    if validateDomain(domain): return db.setDomain(domain)
    else: return "ERROR! invalid domain format"
# =============================================================================
# #set create entry with only ip
# =============================================================================
def setIp(ip):
    if validateIp(ip): return db.setIp(ip)
    else: return "ERROR! invalid ip format"
# =============================================================================
# #get ip from domain
# =============================================================================
def getIp(domain):
    if validateDomain(domain):
        return db.getIp(domain)
# =============================================================================
# #crate new domain + ip link
# =============================================================================
def createNewEntry(domain,ip):
    if not validateDomain(domain):
            return "ERROR! invalid domain format"
    elif ip!="False":
        if not validateIp(ip):
                return "ERROR! invalid ip format"
    return db.createNewEntry(domain,ip)
# =============================================================================
# #Prints out the whole database
# =============================================================================
def printDb():
    return db.printDb()


try:
    if os.environ["debug"]==1:
        print("server test")
        print("testing validate ip")
        test="google.com"
        print("%s returns %s" %(test,validateDomain(test)))
        test="www.google.com"
        print("%s returns %s" %(test,validateDomain(test)))
        test="127.0.0.1"
        print("%s returns %s" %(test,validateIp(test)))
except:pass
