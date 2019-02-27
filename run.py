#!/usr/local/bin/python3.7
from flask import Flask #import the framework
from flask import Response
import threading #handles the concurrency
import server #import the server functionality
import time
# =============================================================================
# create flask app and routes
# 
# 1. Open an app using flask framework
# 2. just tell the Flask app we are not in debug mode
# 3. app.debug = False - like a bootApp: once you make changes you don't need to restart the app
#    so now some functions in Flask frame work won't be able to work
# =============================================================================
app=Flask("dns_server")
app.debug=False
app.use_reloader=False
# =============================================================================
#  this needs to be true if tests should be run
# =============================================================================
debug=False

# =============================================================================
# @app.route above class or function which mean a registeration functions in our Flask App
# and attach it with http route
# =============================================================================

# =============================================================================
# #this route is for getting ip from domain, takes 1 argument, domain - only alows get requests
# =============================================================================
@app.route("/get/ip/<string:domain>",methods=["GET"])
def getIp(domain):
    [rc, ipData] = server.getIp(domain)
    print ("status   =   " +str(rc))
    print ("ipData = " +str(ipData))
    print ("domain = " +str(domain))
    jsonResponse = '[{"text" : "' + domain +'","url": "http://' +ipData +'"}]'
    return Response(jsonResponse, status = rc, mimetype = 'application/json')
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
# =============================================================================
# Our code divide to 2 parts: Test Part with debug = TRUE and Server Part with debug = FALSE
# But since we need to run the tests we need to eun it with a thread but without the server!!
# so we create only one thread for the tests!  
# =============================================================================
if debug:
    threading.Thread(target=app.run,daemon=True).start()
    time.sleep(1)#so output doesnt mix
    print("\n\n")

flaskRunning=False
stopped=False
# =============================================================================
# loop for admin
# =============================================================================
while not stopped and not debug:
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
# start server - multithreading option
# =============================================================================
    elif inp=="c":
        if not flaskRunning:
            flaskRunning=True
            #start server as a thread + daemon
            threading.Thread(target=app.run("0.0.0.0"),daemon=True).start()
            time.sleep(1)#so output doesnt mix
# =============================================================================
#logging
# =============================================================================
            print("\n\n")
            print("server running")
            
        else:
            print("server already running") 


    
    elif inp=="exit":
        stopped=True
# =============================================================================
#dont start twice
# =============================================================================

# =============================================================================
# in case cant spell correctly
# =============================================================================
    else:
        print("incorrect input: %s" % inp)
    time.sleep(1)
# =============================================================================
# so output doesnt mix
# =============================================================================
