'''class Print:
    def __init__(self):
        self.printingTasks = []
        length=len(self.printingTasks)
        # return length

    # def maxLen(self,printingTasks):
    #     return len(printingTasks) > 5    

    def addPrintTaskToSchedule(self,printTask):
        if len(self.printingTasks)<5:
            self.printingTasks.append(printTask)
            print(f"Added task : {printTask}")
        
        else:
            print("Tasks limit exceeded please try after these tasks complitation")
        

    def printingTheTask(self):
        if len(self.printingTasks) == 0:
            print("No Tasks")
            return
        else:
            if len(self.printingTasks)<=5:
                while self.printingTasks:
                    printTask = self.printingTasks.pop(0)
                    print(f"printing: {printTask}")


printScheduler = Print()

printScheduler.addPrintTaskToSchedule("kavya's resume")
printScheduler.addPrintTaskToSchedule("Krishna's wiki page for andhra tourism")
printScheduler.addPrintTaskToSchedule("chanikya's Mahesh Babu poster")
printScheduler.addPrintTaskToSchedule("kavya's resume")
printScheduler.addPrintTaskToSchedule("Krishna's wiki page for andhra tourism")
printScheduler.addPrintTaskToSchedule("kavya's resume")
printScheduler.addPrintTaskToSchedule("kavya's resume")




printScheduler.printingTheTask()'''


# task is add a lmaxLength of 5, and do the same operation like the task above.











'''class Queue:
    def __init__(self,size,count):
        self.items = []
        self.size = size
        self.count=count

    def is_empty(self):
        return len(self.items)==0
    
    def is_full(self):
        return len(self.items)==self.size

    # pushing an elemnt to queue is called enqueing
    def enqueue(self,item):
        self.count+=1
        if self.is_full():
            pass
            # print("Queue is Full, try dequing elements")
        else:
            
            self.items.append(item)

    # deleting from the front is dequeing
    def dequeue(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            self.count-=1
            return self.items.pop(0)
        
    def front(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items[0]
        
    def rear(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items[-1]
        
    def display(self):
        
        print("Queue is full, try dequing ",self.count-self.size-1,"Elements")
        return self.items
        

q = Queue(10,0)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.enqueue(5)
q.dequeue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(4)
q.enqueue(4)
q.enqueue(4)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(4)
q.enqueue(4)
q.enqueue(4)
print(q.display())
    

# suppose you are trying to enque more than the size of the queue,

# so you need to return how many times you need to deque in order to enque one elemet.'''