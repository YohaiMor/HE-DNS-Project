import pymysql #NOT NEEDED

class Db_util:
    cursorClass=pymysql.cursors.DictCursor
    def __init__(self,host,user,db,charset="utf8"):
        self.con=pymysql.connect(host=host,user=user,db=db,charset=charset)
    def getIp(self,domain):
        try:
            with self.con.cursor() as cursor:
                sql="SELECT ip FROM dns WHERE domain=%s"
                cursor.execute(sql,domain)
                result=cursor.fetchone()
                print(result)
                return result
        except Exception as ex: print(ex)
    def setIp(self,domain,ip):
        try:
            with self.con.cursor() as cursor:
                sql="UPDATE dns SET ip=%s WHERE domain=%s"
                cursor.execute(sql,ip,domain)
                result=cursor.fetchone()
                print(result)
            return result
        except Exception as ex: print(ex)
    def setDomain(self,domain,ip):
        try:
            with self.con.cursor() as cursor:
                sql="UPDATE dns SET domain=%s WHERE ip=%s"
                cursor.execute(sql,domain,ip)
                result=cursor.fetchone()
                print(result)
            return result
        except Exception as ex: print(ex)


class NewDb_util:
    def __init__(self):
        self.db={
            "illegalcarrots.com":"76.211.123.2",
            "hireusednapkins.uk":"92.122.65.1",
            "notyomama.com":"76.165.22.8",
            "howtotieyourshoes.com":"42.99.132.22",
            "moonpenguins.hurrdurr":"over 9000",
            "t":"1"#for testing
        }
    def printDb(self):
        print("DB LAYOUT")
        print("---------------------------------")
        for key,val in self.db.items():
            print("%s : %s" % (key,val))
        print("---------------------------------")
    def getIp(self,domain):
        try: return self.db[domain]
        except: return "FAIL - domain \"%s\" doesnt exist" % domain
    def setIp(self,domain,ip):
        try:
            self.db[domain]=ip
            return "changed ip for domain \"%s\" to \"%s\"" % (domain,ip)
        except: return "FAIL - domain \"%s\" doesnt exist" % domain
    def setDomain(self,domain,ip):
        changed=False
        for key,val in self.db.items():
            if val==ip: 
                self.db[domain]=self.db.pop(key)
                changed=True
                break
        if changed:
            return "changed domain for ip \"%s\" to \"%s\"" %(ip,domain)
        else: return "FAIL - ip \"%s\" doesnt exist" % ip
