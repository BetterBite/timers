import time
def timeprinter(p): #ensures proper 24 hour format
    if p < 10:
        o = '0'+str(p) #makes it 0x instead of just x
        return(o)
    else:
        o = str(p) #if it already is 2 digit then no change is made except casting as string
        return(o)


while True:
    x=0 #seconds
    y=0 #minutes
    z=0 #hours
    sec=0 #time in second format
    choice = input("Type '1' to count up time. Type '2' to count down time. ")
    if choice == '1': #count up timer
        input("You have chosen to count up time. Press enter to continue. ")
        while True:
            sec=sec+1
            x=x+1
            if x == 60: #converts upon overflow
                y=y+1
                x=0
            if y == 60:
                z=z+1
                y=0

            x2 = timeprinter(x)
            y2 = timeprinter(y)
            z2 = timeprinter(z)

            print(z2+':'+y2+':'+x2+' '+str(sec)+'s')
            time.sleep(1)
    elif choice == '2': #Count down timer
        input("You have chosen to count down time. Press enter to continue ")
        settime = input("Please input desired time in seconds. If you would like to input in minutes, type 'm'. ")
        if settime == 'm':
            minutes = True
            settime = input("Please input desired time in minutes. ")
            try:
                settime = int(settime) #settime may be depreciated as it could become redundant
                x = settime*60
                sec = x
                y = settime
                z = y//60
                x = x%60
                if sec != 0 and x == 0: #to ensure that on the first time it does not remove a minute
                    x=60
                    y=y-1
                while sec != 0:
                    sec=sec-1
                    if sec != 0: #ensures it avoids a -1
                        x=x-1
                        if x == 0: #Overflower but for the negatives
                            y=y-1
                            x=59
                        if sec > 59: #ensures it avoids a -1 in the minutes
                            if y == 0:
                                z=z-1
                                y=59
                    else:
                        x=x-1 #ensures it finishes on x=0

                    x2 = timeprinter(x)
                    y2 = timeprinter(y)
                    z2 = timeprinter(z)

                    print(z2+':'+y2+':'+x2+' '+str(sec)+'s')
                    time.sleep(1) #the actual point of the timer
            except:
                print("You have chosen something other than a number. Idiot.")
        else:
            try:
                settime = int(settime)
                minutes = False
                sec = settime
                x=sec%60 #0h 0m 2s 3602
                y=sec//60 #0h 60m 2s 3602
                z=y//60 #1h 60m 2s 3602
                y -=60 #1h 0m 2s 3602
                if sec != 0 and x == 0: #This can probably be merged into 1 function by using 'choice' to determine whether it adds or subtracts
                    x=59
                    y=y-1
                while sec != 0:
                    if sec != 0 and x == 0: #This can probably be merged into 1 function by using 'choice' to determine whether it adds or subtracts
                        x=60
                        y=y-1 
                    sec=sec-1 #1h 0m 2s 3601
                    if sec != 0:
                        x=x-1 #1h 0m 1s 3601
                        ##if x == 0 and y != 0 and (sec%60) != 0:
                            ##y = y-1 
                            ##x = 59 
                        if sec > 60:
                            if y == 0 and x != 0 and z != 0:
                                z=z-1 
                                y=59
                    else:
                        x=x-1
                   
                    x2 = timeprinter(x)
                    y2 = timeprinter(y)
                    z2 = timeprinter(z)

                    print(z2+':'+y2+':'+x2+' '+str(sec)+'s')
                    time.sleep(1)
            except:
                print("You have chosen something other than a number or the letter 'm'. Idiot.")

    else:
        print("You have chosen something other than 1 and 2. Idiot. Try again.")