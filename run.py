#!/usr/local/bin/python3.7
from flask import Flask #import the framework
import threading #handles the concurrency
import server #import the server functionality
import time
# =============================================================================
# #create flask app and routes
# =============================================================================
app=Flask("dns_server")
app.debug=False
app.use_reloader=False
# =============================================================================
#  this needs to be true if tests should be run
# =============================================================================
debug=True
# =============================================================================
# #this route is for getting ip from domain, takes 1 argument, domain - only alows get requests
# =============================================================================
@app.route("/get/ip/<string:domain>",methods=["GET"])
def getIp(domain):
    return server.getIp(domain)
# =============================================================================
# this route is for setting ip, takes 2 arguments, domain and ip - only allows post request
# =============================================================================
@app.route("/change/ip/<string:domain>/<string:ip>",methods=["POST"])
def changeIp(domain,ip):
    return server.changeIp(domain,ip)
# =============================================================================
# this route is for setting domain, takes 2 arguments, domain and ip - only allows post request
# =============================================================================
@app.route("/change/domain/<string:domain>/<string:ip>",methods=["POST"])
def changeDomain(domain,ip):
    return server.changeDomain(domain,ip)
# =============================================================================
# this route is for creating new entry, takes 2 arguments, domain and ip - only allows post request
# =============================================================================
@app.route("/create/<string:domain>/<string:ip>",methods=["POST"])
def createNewEntry(domain,ip):
    return server.createNewEntry(domain,ip)
# =============================================================================
# this route is for setting domain , takes 1 arguments, domain - only allows post request
# =============================================================================
@app.route("/set/domain/<string:domain>",methods=["POST"])
def setDomain(domain):
    return server.setDomain(domain)
# =============================================================================
# this route is for setting ip , takes 1 arguments, ip - only allows post request
# =============================================================================
@app.route("/set/ip/<string:ip>",methods=["POST"])
def setIp(ip):
    return server.setIp(ip)
# =============================================================================
# if tests are to be run
# =============================================================================
if debug:
    threading.Thread(target=app.run,daemon=True).start()
    time.sleep(1)#so output doesnt mix
    print("\n\n")

flaskRunning=False
ActivateLoop = True
# =============================================================================
# loop for admin
# =============================================================================
while ActivateLoop and not debug:
# =============================================================================
# here we have a menu for the admin who response on the server
# =============================================================================
    print("\n")
    print("Server-Adminstrator Menu:")
    print("a. Set new domain and IP")
    print("b. Print DNS table")
    print("c. Activate the server - listening to requests")
    inp=input("What would you like to do? (a,b,c): ")
# =============================================================================
# create new domain + ip link
# =============================================================================
    if inp=="a":
        print(server.createNewEntry(input("New domain: "),input("Associated ip: ")))
# =============================================================================
# print database
# =============================================================================
    elif inp=="b":
        print("printing databse...")
        print(server.printDb())
# =============================================================================
# start server
# =============================================================================
    elif inp=="c":
        if not flaskRunning:
            flaskRunning=True
            #start server as a thread + daemon
            threading.Thread(target=app.run,daemon=True).start()
            time.sleep(1)#so output doesnt mix
# =============================================================================
#logging
# =============================================================================
            print("\n\n")
            print("server running")
# =============================================================================
#dont start twice
# =============================================================================
        else:
            print("server already running")
            
            
    elif inp=="exit":
         ActivateLoop=False
         
# =============================================================================
# in case cant spell correctly
# ============================================================================= 
    else:
        print("incorrect input: %s" % inp)
    time.sleep(1)
# =============================================================================
# so output doesnt mix
# =============================================================================
