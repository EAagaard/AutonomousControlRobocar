def getdistancefrontsensor():
    while gy53.value() == True:
        pass
    while gy53.value() == False:
        pass
    starttime = time.ticks_us()
    while gy53.value() == True:
        pass
    endtime = time.ticks_us()
    microsec_diff = endtime - starttime
    millimeterdistance = microsec_diff / 10
    distance = millimeterdistance / 10
    print(f"Distance to surface: {distance} cm")

    return distance

def Vdrej():
    pinFREMAD.off()
    pinHDREJ.off()
    pinVDREJ.on()

def Hdrej():
    pinFREMAD.off()
    pinVDREJ.off()
    pinHDREJ.on()

def drive():
    pinVDREJ.off()
    pinHDREJ.off()
    pinFREMAD.on()

def enginestop():
    pinFREMAD.off()
    pinVDREJ.off()
    pinHDREJ.off()

def reverse():
    pinFREMAD.off()
    pinVDREJ.off()
    pinHDREJ.off()
    pinBAGUD.on()

def getBlackWhitesensor():
    # hvid = 1
    # sort = 0

    # måske funktion for sig selv "def attack"?
    if val = 1:
        drive()
    if val = 0:
        enginestop()
        time.sleep(2)

def scan():
    enginestop()
    distance = getdistancefrontsensor()
    if distance > 200:
        Vdrej()
    else:
        Hdrej()
