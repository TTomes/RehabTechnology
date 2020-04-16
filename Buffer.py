# Gait Detection - Rehab Engineering
# Circular Buffer for ananlyzing real-time gait cycle data. 
# Written by: Travis Tomer

class CircularBuffer:

    def __init__(self, cirBufferSize):
        self.queue = list()
        self.maxSize = cirBufferSize
        self.head = 0
        self.tail = 0

    #Adding elements to the queue
    def enqueue(self, data):
        # Check if queue is full before appending
        if self.size() == self.maxSize - 1:
            return False

        # Add new data
        self.queue.append(data)
        # Update tail position
        self.tail = (self.tail + 1) % self.maxSize
        # End funtion 
        return True 

    # Removing old elements 
    def dequeue(self):
        # Check if queue is empty 
        if self.size() == 0:
            return -1 # Queue is empty
        data = self.queue[self.head]
        self.queue.pop(self.head)
        # Update head positon
        self.head = (self.head + 1) % self.maxSize
        # End funtion by returning updated data 
        return data


    # Check if data in buffer is ascending
    def isAscending(self):
        # Check if queue is empty
        if self.size() == 0:
            return False
        else:
            for i in range(self.head, self.tail - 1):
                if (self.queue[i] > self.queue[i+1]):
                    return False
        return True
        

    # Check if data in buffer is descending
    def isDescending(self):
        # Check if queue is empty
        if self.size() == 0:
            return False
        else:
            for i in range(self.head, self.tail - 1):
                if (self.queue[i] < self.queue[i+1]):
                    return False
        return True


    # Get average value of data in the buffer
    def avgValue(self):
        if self.size() != 0:
            return sum(self.queue[self.head:self.tail]) / self.size()
        else:
            return 0

    # Checks to see if the data in the buffer contains a zero cross
    def didCrossZero(self):
        # Check if queue is empty
        if self.size() == 0:
            return False
        for i in range(self.head, self.tail - 1):
            if (self.queue[i] * self.queue[i+1] < 0):
                return True
        return False

    #Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        else:
            return (self.maxSize - (self.head - self.tail))




#buf = CircularBuffer(4)
#print("Max Size: " + str(buf.maxSize))
#buf.enqueue(0)
#rint("Head: " + str(buf.head) + ", Tail: " + str(buf.tail))
#buf.enqueue(1)
#print("Head: " + str(buf.head) + ", Tail: " + str(buf.tail))
#buf.enqueue(2)
#print("Head: " + str(buf.head) + ", Tail: " + str(buf.tail))
#print(buf.queue)
#buf.enqueue(3)
#print("Head: " + str(buf.head) + ", Tail: " + str(buf.tail))
#print(buf.queue)
#buf.enqueue(4)
#print("Head: " + str(buf.head) + ", Tail: " + str(buf.tail))

