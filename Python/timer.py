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
        print(str(self.z).rjust(2, '0')+":"+str(self.y).rjust(2, '0')+":"+str(self.x).rjust(2, '0')+" "+str(self.secs)+"s")

#https://youtu.be/M2dhD9zR6hk
class Countdown:
    x = 0
    y = 0
    z = 0
    secs = 1

    def __init__(self, amount, mins):
        if mins == True:
            self.x = 1
            #TO DO
        else:
            self.secs = amount
            #proper assignment of time variables
            self.z = self.secs//3600
            self.secs -= self.z*3600
            
            self.y = self.secs//60
            self.secs -= self.y*60

            self.x = self.secs
            self.secs = amount #reset to original value

    def decrement(self):
        self.secs -= 1
        self.x -= 1
        if self.x < 0:
            self.x = 59
            self.y -= 1
        if self.y < 0:
            self.y = 59
            self.z -= 1
        time.sleep(1)

    def print(self):
        print(str(self.z).rjust(2, '0')+":"+str(self.y).rjust(2, '0')+":"+str(self.x).rjust(2, '0')+" "+str(self.secs)+"s")


#Main, technically main, code execution starts here
while True: #while True: represents a block with input where upon rejection of input will prompt user to retry through continue
    choice = input("Select mode, 'countup' for counting up, 'countdown' for counting down: ")
    if choice != "countup" and choice != "countdown":
        print("Invalid input. Try again.")
        continue
    break


if choice == "countup":
    clock = Countup()
    while clock.secs != 360000: #100 hour limit
        clock.increment()
        clock.print()
    if clock.secs == 360000:
        time.sleep(1)
        print("Counting finished, limit of 100h reached")
        exit(0)
    elif clock.secs != 360000:
        time.sleep(1)
        print("Counting finished, early termination")
        exit(0)


if choice == "countdown":
    mode = False
    while True:
        amount = input("Insert time in seconds, or type 'm' to insert time in minutes. ")
        if amount == 'm':
            mode = True
            while True: #in minutes
                amount = input("Insert time in minutes. ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input.")
                    continue
                break
        try:
            amount = int(amount)
        except:
            print("Invalid input.")
            continue
        break
    clock = Countdown(amount, mode)
    while clock.secs != 0:
        clock.decrement()
        clock.print()
    if clock.secs == 0:
        time.sleep(1)
        print("Finished counting.")
    elif clock.secs != 0:
        time.sleep(1)
        print("Finished counting, early termination")
    