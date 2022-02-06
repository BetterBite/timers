import time

#field of constants
TIME_LIMIT = 360000 #100h time limit

class Countup:
    x = 0
    y = 0
    z = 0
    secs = 0

    def increment(self):
        self.secs += 1
        self.x += 1
        if self.x == 60:
            self.y += 1
            self.x = 0
        if self.y == 60:
            self.z += 1
            self.y = 0
        time.sleep(1)

    def print(self):
        print("%02d:%02d:%02d "+str(self.secs)+"s")

#https://youtu.be/M2dhD9zR6hk
class Countdown:
    x = 0
    y = 0
    z = 0
    secs = 0

    def __init__(self, amount, mins):
        if mins == True:
            self.x = 1
            #do something
        else:
            self.secs = amount

            self.z = self.secs//3600
            self.secs -= self.z*3600
            
            self.y = self.secs//60
            self.secs -= self.y*60

            self.x = self.secs
            self.secs = amount 


#Main, technically main, code execution starts here
while True: #two while loops permit a kind of retry should an input be invalid
    while True:
        choice = input("Select mode, 'countup' for counting up, 'countdown' for counting down")
        if choice != "countup" or choice != "countdown":
            print("Invalid input. Try again.")
            continue
        break
    if choice == "countup":
        clock = Countup()
        while clock.secs != 360000: #100 hour limit
            clock.increment()
            clock.print()
        if clock.secs == 360000:
            print("Counting finished, limit of 100h reached")
            exit(0)
        elif clock.secs != 360000:
            print("Counting finished, early termination")
            exit(0)
    if choice == "countdown":
        while True:
            amount = input("Insert time in seconds, or type 'm' to insert time in minutes.")
            if amount == 'm':
                mode = True
                while True: #in minutes
                    amount = input("Insert time in minutes.")
                    if isinstance(amount, int) == True:
                        break
                    continue
            elif isinstance(amount, int) == True: #in seconds
                break
            else:
                print("Invalid input.")
                continue
            break
        #call a class