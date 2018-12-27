from db_util import Db_util,NewDb_util
#create a connection to MySQL first - also makeing sure its online
#db=Db_util(host="localhost",user="root",db="dns")
db=NewDb_util()
db.printDb()
#NOTE: probably missunderstand what this should do or?
def getIp(domain):
    return db.getIp(domain)
def setIp(domain,ip):
    return db.setIp(domain,ip)
def setDomain(domain,ip):
    return db.setDomain(domain,ip)
