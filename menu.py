from urllib.request import urlopen,Request 
# =============================================================================
# used by the menu to interact with dns server
# =============================================================================
# =============================================================================
# start infinite loop to serve user
# =============================================================================
while 1:
    print(str(urlopen("http://localhost:5000/get/ip/%s"%input("What hostname do you wish to translate: ")).read().decode("ascii")))
