def getdistance():
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

def move_forward():
    pinDREJ.off()
    pinFREMAD.on()

def move_sideways():
    pinFREMAD.off()
    pinDREJ.on()

def enginestop():
    pinFREMAD.off()
    pinDREJ.off()

def follow_wall():
    pinFREMAD.on()
    distance = getdistance()
    if distance <= 5:
        move_sideways()
    if distance > 5:
        move_forward()
    if DISTANCETOFRONTSENSOR => 10
        enginestop()

