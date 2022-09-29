
class EventRequest:

    EventType="R"

    def __init__(self,RetryCount):
        self.RetryCount=RetryCount
    

class EventStatus:

    EventType = "S"

    def __init__(self,StatusType,RetryCount):
        self.StatusType = StatusType
        self.RetryCount = RetryCount

class Event:

    event=None

    def setEventRequest(self,RetryCount):
        self.event = EventRequest(RetryCount)

    def setEventStatus(self,StatusType,RetryCount):
        self.event = EventStatus(StatusType,RetryCount)


class EventQueue:
    queue = []

    def push(self,event):

        self.queue.append(event)

    def pop(self):

        if len(self.queue)>0:

            return self.queue.pop(0)

        else:
            return None

    def isQueueEmpty(self):
        if not self.queue:
            return True
        return False

    def getElementsOfQueue(self):
        if not self.queue:
            print(f"queue is Empty")

        for i in range(len(self.queue)):
            print(self.queue[i].event)

    def getCurrentLengthOfQueue(self):
        return len(self.queue)


# Validation of events logic
def isEventValid(data):
    if len(data)>2:
        return False
    
    elif len(data)==1:
        return isRequestEventValid(data)

    elif len(data)==2:
        return isStatusEventValid(data)

    return False

# validating StatusEvent here
def isStatusEventValid(data):

    return (data[0] in ('P','M','C','T')) and (isinstance(data[1],int))

# validating RequestEvent here
def isRequestEventValid(data):

    return isinstance(data[0],int)

# This method Pushes events in queue
def getQueueWithEvents():
    queue = EventQueue()

    
    Events =[('P',0),(0,),('M',0),('P',0),('T',0),('P',0),('C',0),('M',0),('apha','df')]

    for event in Events:
        if isEventValid(event):

            if (len(event)==2):

                temp = Event()
                param1 = event[0]
                param2 = event[1]
                temp.setEventStatus(param1,param2)
                queue.push(temp)

            else:

                temp = Event()
                temp.setEventRequest(event[0])
                queue.push(temp)

    return queue



# Starting point
if __name__=="__main__":

    queue = getQueueWithEvents()
    LastValueOfStatusTypeCorT=False

    while not queue.isQueueEmpty():

        Eventt = queue.pop()

        if isinstance(Eventt.event,EventStatus):

            if (Eventt.event.StatusType in ('C','T')) and Eventt.event.RetryCount<2:
                temp = Event()
                temp.setEventStatus(Eventt.event.StatusType,Eventt.event.RetryCount+1)
                queue.push(temp)
                LastValueOfStatusTypeCorT=True

            else:
                LastValueOfStatusTypeCorT=False

            print(f"EventStatus: {Eventt.event.EventType},{Eventt.event.StatusType},{Eventt.event.RetryCount}")

        if isinstance(Eventt.event,EventRequest):

            if LastValueOfStatusTypeCorT==True:
                LastValueOfStatusTypeCorT=False


                print(f"EventRequest: {Eventt.event.EventType},{Eventt.event.RetryCount}")
            
            else:
                temp = Event()
                temp.setEventRequest(Eventt.event.RetryCount+1)
                queue.push(temp)

