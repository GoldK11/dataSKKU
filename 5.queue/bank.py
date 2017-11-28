from queuee import *


import random

class Teller:
    def __init__(self):
        self.currentCustomer = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentCustomer != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentCustomer = None

    def busy(self):
        if self.currentCustomer != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentCustomer = newtask
        self.timeRemaining = newtask.getServiceTime()

class Customer:
    def __init__(self, time, cid, stime):
        self.id = cid
        self.timestamp = time
        self.stime = stime

    def getStamp(self):
        return self.timestamp

    def getServiceTime(self):
        return self.stime 

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds):

    tellers = [Teller()]

    customerQueue = Queue()
    waitingtimes = []
    cid = 0
    
    for currentSecond in range(1,numSeconds):
        print('time = ', currentSecond)

        if newPrintTask():
             cid += 1
             customer = Customer(currentSecond, cid, random.randrange(1,11))
             print('Customer %d enters. service time = %d.' %(customer.id, customer.getServiceTime()))
             customerQueue.enqueue(customer)


        for i in tellers:                 
            if (not i.busy()) and (not customerQueue.isEmpty()):
                nextcustomer = customerQueue.dequeue()
                waitingtimes.append( nextcustomer.waitTime(currentSecond))
                i.startNext(nextcustomer)

            i.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Number of customers who entered = ", cid)
    print("Number of served customers = ", len(waitingtimes))
    print("Average Waiting time per customer = ", averageWait)
    print("Number of customers waiting = ",customerQueue.size())
    print("DEBUG: waitingtimes:",waitingtimes)
 
def newPrintTask():
    num = random.randrange(1,3)
    if num == 1:
        return True
    else:
        return False

for i in range(1):
    simulation(11)


