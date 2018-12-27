#!/usr/local/bin/python3.7
#if i missed to remove a #debug, please do :) and REMOVE THIS :D
from flask import Flask #import the framework
from werkzeug.serving import run_simple #needed so that threading will recognize threaded as an valid option in kwargs
import threading #handles the concurrency
from sys import platform #to check what OS is running #NOT NEEDED?
from os import system #to start mysql #NOT NEEDED?
import server #import the server functionality
import atexit #used to stop mysql server, when program is finished #NOT NEEDED?
#NOT NEEDED ?
#function that will stop mysql server
def finished():
    system("SAME PATH AS ABOVE -u root shutdown")
#start mysql server - might crash if its already running?
if platform=="win32":
    #https://dev.mysql.com/doc/refman/5.7/en/windows-start-command-line.html #REMOVE THIS - intentional bug
    system("THIS NEEDS TO BE THE POSITION OF MYSQL SERVER")
atexit.register(finished) #register it - so it runs when program is finished
#END NOT NEEDED
#create flask app and routes
app=Flask("dns_server")
#this route is for getting ip from domain, takes 1 argument, domain - only alows get requests
@app.route("/get/ip/<string:domain>",methods=["GET"])
def getIp(domain):
    return server.getIp(domain)
#this route is for setting ip, takes 2 arguments, domain and ip - only allows post request
@app.route("/set/ip/<string:domain>/<string:ip>",methods=["POST"])
def setIp(domain,ip):
    return server.setIp(domain,ip)
#this route is for setting domain, takes 2 arguments, domain and ip - only allows post request
@app.route("/set/domain/<string:domain>/<string:ip>",methods=["POST"])
def setDomain(domain,ip):
    return server.setDomain(domain,ip)
#start flask app
app.run(threaded=True,port=3000)
