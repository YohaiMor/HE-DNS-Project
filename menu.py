from urllib.request import urlopen,Request #used by the menu to interact with dns server
#start infinite loop to serve user
while 1:
    #handle user input
    inp=input("what to use method? expected answer g/s:")
    #for input "g"
    if inp=="g":
        inp=input("type domain to get ip for: ")
        res=urlopen("http://localhost:3000/get/ip/%s"%inp)
        print("response: %s" % str(res.read().decode("ascii")))
    #for input "s"
    elif inp=="s":
        inp=input("set domain or ip? expected answer d/i: ")
        if inp=="d":
            ip=input("ip to set domain on: ")
            domain=input("new domain: ")
            res=urlopen(Request(url="http://localhost:3000/set/domain/%s/%s"%(domain,ip),method="POST"))
            print("response: %s" % str(res.read().decode("ascii")))
        elif inp=="i":
            domain=input("domain to set ip on: ")
            ip=input("new ip: ")
            res=urlopen(Request(url="http://localhost:3000/set/ip/%s/%s"%(domain,ip),method="POST"))
            print("response: %s" % str(res.read().decode("ascii")))
        else:
            print("program doesn't understand input: %s. try again." % inp)
        #in case you can't spell correctly hah :)
    else: 
        print("program doesn't understand input: %s. try again." % inp)
    print("\n")
