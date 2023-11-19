import speedtest

def testSpeed():
    intSpd = speedtest.Speedtest()
    print("Download Speed: ")
    downloadSpeed = intSpd.download()/1000000 #using this to convert into mbps
    print(f"{downloadSpeed:.2f}")    
    print("Upload Speed: ")         
    uploadSpeed = intSpd.upload()/1000000 
    print(f"{uploadSpeed:.2f}")
    if(downloadSpeed > 100.00):
        print("Excellent Internet")
    elif(downloadSpeed > 25.00):
        print("Good Internet")
    else:
        print("Poor Internet")
        
testSpeed()


# ping best >20 good >50 poor <150