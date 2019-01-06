import time
from urllib.request import urlopen,Request
from urllib.parse import urlencode
import run
import server
regDError="ERROR! invalid domain format"
regIError="ERROR! invalid ip format"
createEntrySuccesfull="Entry added succesfully!"
setDSuccesfull="Hostname added succesfully!"
setDError="ERROR! domain already exist"
setIError="ERROR! ip already exist"
setISuccesfull="Ip added succesfully!"

# =============================================================================
# we have a counter for calculate how many tests we have succeed
# =============================================================================
score=0
totalScore=0


print("RUNNING TESTS - REMEMBER NOT TO HAVE SERVER RUNNING ALREADY")
print("\n")
print("\n******************************************************************************************************")
print("*****************     TEST1: create entry, via createNewEntry api function    ************************")
print("******************************************************************************************************")

inp="nana%20.com"
print("please enter a hostname: %s"%inp)

# =============================================================================
# here we use the same method as we have used in the server.py and run.py since
# we want to examine the exact actions and see if the request is succesfully made
# =============================================================================
req=Request("http://localhost:5000/create/%s/%s"%(inp,"False"),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regDError)
print("TEST1.1: %s - returned: %s | expected return: %s"%(result, asciRet, regDError))
# =============================================================================
# if and only if the return value is "True" which mean the test is succeed!:
# so we can increase the counter in 1    
# =============================================================================
if result=="True":score+=1

inp="..mako"
print("please enter a hostname: %s"%inp)
req=Request("http://localhost:5000/create/%s/%s"%(inp,"False"),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regDError)
print("TEST1.2: %s - returned: %s | expected return: %s"%( result, asciRet, regDError))
if result=="True":score+=1

inp="ads.youtube.com"
print("please enter a hostname: %s"%inp)
req=Request("http://localhost:5000/create/%s/%s"%(inp,"False"),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==createEntrySuccesfull)
print("TEST1.3: %s - returned: %s | expected return: %s"% (result, asciRet, createEntrySuccesfull))
if result=="True":score+=1
print("TEST1 DONE: result %s/3"%score)
print("******************************************************************************************************")
if score == 3:
    print("***********************************     TEST 1: SUCCEED!     *****************************************")
else:
    print("*************************************     TEST 1: FAILED!     ****************************************")
print("******************************************************************************************************\n")
   
totalScore+=score
score=0
print("\n")
print("\n******************************************************************************************************")
print("************************     TEST2: Set IP, using setIp api function    ******************************")
print("******************************************************************************************************")

inp="walla.co.il"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.1: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1

inp="45456"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.2: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1


inp="12.45.3"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.3: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1

inp="12.26"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.4: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1

inp="312.12.1.44"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.5: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1

inp="12.451.3.10"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.6: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1

inp="123.1.257.3"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==regIError)
print("TEST2.7: %s - returned: %s | expected return: %s"% (result, asciRet, regIError))
if result=="True":score+=1

inp="10.43.20.21"
print("please enter a ip: %s"%inp)
req=Request("http://localhost:5000/set/ip/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==setISuccesfull)
print("TEST2.8: %s - returned: %s | expected return: %s"% (result, asciRet, setISuccesfull))
if result=="True":score+=1

print("TEST2 DONE: result %s/8"%score)
print("******************************************************************************************************")
if score == 8:
    print("***********************************     TEST 2: SUCCEED!     *****************************************")
else:
    print("*************************************     TEST 2: FAILED!     ****************************************")
print("******************************************************************************************************\n")
print("\n")




totalScore+=score
score=0


print("\n******************************************************************************************************")
print("***************    TEST3: CREATE\CHECK existance domain via setDomain API function   *****************")
print("******************************************************************************************************")


inp="google.co.il"
print("Please enter a hostname: %s"%inp)
req=Request("http://localhost:5000/set/domain/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==setDSuccesfull)
print("TEST3.1: %s - returned: %s | expected return: %s"% (result, asciRet, setDSuccesfull))
if result=="True":score+=1

inp="google.co.il"
print("Please enter a hostname: %s"%inp)
req=Request("http://localhost:5000/set/domain/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==setDError)
print("TEST3.2: %s - returned: %s | expected return: %s"% (result, asciRet, setDError))
if result=="True":score+=1

inp="walla.co.il"
print("Please enter a hostname: %s"%inp)
req=Request("http://localhost:5000/set/domain/%s"%(inp),method="POST")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet==setDSuccesfull)
print("TEST3.3: %s - returned: %s | expected return: %s"% (result, asciRet, setDSuccesfull))
if result=="True":score+=1
print("TEST3 DONE: result %s/3"%score)



print("******************************************************************************************************")
if score == 3:
    print("***********************************     TEST 3: SUCCEED!     *****************************************")
else:
    print("*************************************     TEST 3: FAILED!     ****************************************")
print("******************************************************************************************************\n")
print("\n")

totalScore+=score
score=0
print("\n******************************************************************************************************")
print("**********************************    TEST4: printing DNS table   ************************************")
print("******************************************************************************************************")


time.sleep(1)
server.clearDb()#to show result from clear db
time.sleep(1)
inp="b"
print("Choose char: %s"%inp)
asciRet=server.printDb()
result=str(asciRet=="Table is empty!")
print("TEST4.1: %s - returned: %s | expected return: %s"% (result, asciRet, "Table is empty!"))
if result=="True":score+=1

inp="a"
print("Chooce char: %s"%inp)
print("please enter a hostname: walla.co.il\nplease enter a ip: 10.43.121.3")
req=Request("http://localhost:5000/create/%s/%s"%("walla.co.il","10.43.121.3"),method="POST")
asciRet=urlopen(req).read().decode("ascii")
print(asciRet)
print(createEntrySuccesfull)
result=str(asciRet==createEntrySuccesfull)
if result=="True":
    print("Domain & IP added successfully!")
    print("Chooce char: b \n")
    time.sleep(1)
    ret=server.printDb()
    print(ret)
    if ret!="Table is empty!":score+=1
    tmp="Table is empty!" if ret=="Table is empty!" else "An not empty table"
    print("TEST4.2: %s - returned %s | expected return %s"%(ret!="Table is empty!",tmp,"An not empty table"))
else: print("Couldnt create new entry and continue with this test")

print("TEST4 DONE: result %s/2"%score)

print("******************************************************************************************************")
if score == 2:
    print("***********************************     TEST 4: SUCCEED!     *****************************************")
else:
    print("*************************************     TEST 4: FAILED!     ****************************************")
print("******************************************************************************************************\n")
print("\n")


totalScore+=score
score=0


print("\n******************************************************************************************************")
print("***************************    TEST5: get ip for non-existing domain   *******************************")
print("******************************************************************************************************")

print("TEST5.1")
inp="google.co.il"
print("What domain would you like to translate: %s"%inp)
req=Request("http://localhost:5000/get/ip/%s"%(inp),method="GET")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet=="ERROR! hostname not found")
if result=="True": score+=1
print("TEST5 DONE: result %s/1"%score)
print("******************************************************************************************************")
if score == 1:
    print("***********************************     TEST 5: SUCCEED!     *****************************************")
else:
    print("*************************************     TEST 5: FAILED!     ****************************************")
print("******************************************************************************************************\n")
print("\n")


totalScore+=score
score=0

print("\n******************************************************************************************************")
print("*****************************    TEST6: get ip from existing domain   ********************************")
print("******************************************************************************************************")

print("TEST6.1")
inp="walla.co.il"
print("What domain would you like to translate: %s"%inp)
req=Request("http://localhost:5000/get/ip/%s"%(inp),method="GET")
asciRet=urlopen(req).read().decode("ascii")
result=str(asciRet!="ERROR! hostname not found")
print("return value: %s"%asciRet)
if result=="True": score+=1
print("TEST6 DONE: result %s/1"%score)
totalScore+=score
print("******************************************************************************************************")
if score == 1:
    print("***********************************     TEST 6: SUCCEED!     *****************************************")
else:
    print("*************************************     TEST 6: FAILED!     ****************************************")
print("******************************************************************************************************\n")
print("\n")

print("TOTAL [%s] TEST RESULT= %s/18"%(totalScore==18,totalScore))
