import os #check environment var for debug
# =============================================================================
# #This is a default DNS-table
# =============================================================================
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
        self.undefiendCounter=0
   
# =============================================================================
# #once we print the table we want to check if the table either empty or not    
# =============================================================================
    def printDb(self):
        if self.db != {}:
            returnedDbString="DB ENTRIES\n___________________________________\n"
            for key,val in self.db.items(): returnedDbString+="%s : %s\n"%(key,val)
            returnedDbString+="---------------------------------"
            return returnedDbString
        else: return "Table is empty!"
    def clearDb(self):
        self.db.clear()
# =============================================================================
# #to create any entity combained domain and IP
# =============================================================================
    def createNewEntry(self,domain,ip):
        try:
            print(self.db[domain])
        except:
            print("couldnt print domain ip")
        try: self.db[domain]
        except:
            if ip!=False: self.db[domain]=ip
            else: self.db[domain]="[NOIP]"
            return "Entry added succesfully!"
        #when no error occurs it alreadt exists
        return "ERROR! Hostname already exist"
    #creates a new entry with only an IP in value spot of map
    def setIp(self,ip):
        found=False
        for k,v in self.db.items():
            #look for ip in values
            if v==ip:
                found=True
                print("IP FOUND %s"%v)
                break
        #only add if not found
        if not found:
            while 1:
                #cant create domain ip value due to map structure, so set domain to something uninportant
                try:
                    self.db["[NODOMAIN%s]"%str(self.undefiendCounter)]=ip
                    break
                except:self.undefiendCounter+=1
            return "Ip added succesfully!"
        else: return "ERROR! ip already exists"
    def setDomain(self,domain):
        #excepts if it already exists
        try: self.db[domain]
        #create new entry
        except:
            self.db[domain]="[NOIP]"
            #inform
            return "Hostname added succesfully!"
        #inform user
        return "ERROR! domain already exist"
    def getIp(self,domain):
        try: return self.db[domain]
        except: return "ERROR! hostname not found"
    #changes the ip on an already existing entry
    def changeIp(self,domain,ip):
        try: 
            if self.db[domain]: self.db[domain]=ip
        #excepts if domain doesnt exist
        except:
            return "ERROR! Hostname doesn't exist"
    #changes the domain on an already entry, via ip value
    def changeDomain(self,domain,ip):
        changed=False
        for key,val in self.db.items():
            if val==ip: 
                self.db[domain]=self.db.pop(key)
                changed=True
                break
        if changed:
            return "changed domain for ip \"%s\" to \"%s\"" %(ip,domain)
        else: return "FAIL - ip \"%s\" doesnt exist" % ip

#DEBUG TEST
try:
    if os.environ["debug"]==1:
        db=NewDb_util()
        db.printDb()
        print()
        print("creating new entry")
        print(db.createNewEntry("hej.com","test"))
        db.printDb()
        print("getting hej.com, directly thro db class")
        print(db.getIp("hej.com"))
        print("creating new entry")
        print(db.createNewEntry("bananas.com","test2"))
        print("getting bananas.com, directly thro db class")
        print(db.getIp("bananas.com"))
        print("TEST END")
except: pass
#END DEBUG


