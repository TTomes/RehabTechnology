# Gait Detection - Rehab Engineering
# Circular Buffer for ananlyzing real-time gait cycle data. 
# Written by: Travis Tomer

class CircularBuffer:

    def __init__(self, cirBufferSize):
        self.queue = list([0] * cirBufferSize)
        self.maxSize = cirBufferSize
        self.head = 0
        self.tail = 0

    #Adding elements to the queue
    def enqueue(self, data):
        # Check if queue is full before appending
        if self.size() == self.maxSize - 1:
            print("BUFFER FULL")
            return False

        # Add new data at the tail index
        self.queue[self.tail] = (data)
        # Update tail position
        self.tail = (self.tail + 1) % self.maxSize
        # End funtion 
        return True 

    # Removing old elements 
    def dequeue(self):
        # Check if queue is empty 
        if self.size() == 0:
            print("BUFFER EMPTY")
            return False # Queue is empty
        data = self.queue[self.head]
        # Update head positon
        self.head = (self.head + 1) % self.maxSize
        # End funtion by returning updated data 
        return data


    # Check if data in buffer is ascending
    def isAscending(self):
        # Check if queue is empty
        if self.size() == 0:
            print("Size is zero")
            return False
        else:
            # CASE 1: If the tail index is less than the head index
            if self.tail <= self.head:
                for i in range(self.head , self.maxSize - 1): # Loop to run from head index to end of array
                    if (self.queue[i] > self.queue[i+1]): # if the data is not ascending return false
                        return False
                 
                if (self.queue[0] < self.queue[self.maxSize - 1]): # Checks the value at index 0 versus the end index (at maxSize - 1) 
                    return False

                for j in range(0, self.tail - 1): # Loop to run from 0 to tail index (only if the data from head to end is ascending)
                    if (self.queue[j] > self.queue[j+1]): # if the data is not ascending return false
                        return False
            # CASE 2: If the tail index is greater than the head index
            else:
                for i in range(self.head, self.tail - 1):
                    if (self.queue[i] > self.queue[i+1]):
                        return False
        # If the previous loops don't return False then the data is ascending (return True)
        return True
        

    # Check if data in buffer is descending
    def isDescending(self):
        # Check if queue is empty
        if self.size() == 0:
            return False
        else:
            # CASE 1: If the tail index is less than the head index
            if self.tail <= self.head:
                #print("CASE 1:")
                for i in range(self.head , self.maxSize - 1): # Loop to run from head index to end of array
                    if (self.queue[i] < self.queue[i+1]): # if the data is not descending return false
                        return False
                
                if (self.queue[0] > self.queue[self.maxSize - 1]): # Checks the value at index 0 versus the end index (at maxSize - 1) 
                    return False

                for j in range(0, self.tail - 1): # Loop to run from 0 to tail index (only if the data from head to end is descending)
                    if (self.queue[j] < self.queue[j+1]): # if the data is not descending return false
                        return False
            # CASE 2: If the tail index is greater than the head index
            else:
                #print("CASE 2:")
                for i in range(self.head, self.tail):
                    if (self.queue[i] < self.queue[i+1]):
                        return False
        # If the previous loops don't return False then the data is descending (return True)
        return True


    # Get average value of data in the buffer
    def avgValue(self):
        if self.size() != 0:
            if self.tail <= self.head: # Case 1: when the tail index is less than the head index
                return (sum(self.queue[self.head:self.maxSize]) + sum(self.queue[0:self.tail])) / self.size()

            else: # Case 2: when tail index is greater than head index
                return sum(self.queue[self.head:self.tail]) / self.size()
        else:
            return 0

    # Checks to see if the data in the buffer contains a zero cross
    def didCrossZero(self):
        # Check if queue is empty
        if self.size() == 0:
            return False

        if self.tail <= self.head: # tail index less than head index
            for i in range(self.head , self.maxSize - 1):
                if self.queue[i] * self.queue[i+1] < 0:
                    return True

            if (self.queue[0] * self.queue[self.maxSize - 1] < 0): # Checks the value at index 0 versus the end index (at maxSize - 1) 
                return True
            
            for j in range(0,self.tail):
                if self.queue[j] * self.queue[j+1] < 0:
                    return True 
        else: # Case 2: tail index greater than head index
            for i in range(self.head, self.tail - 1):
                if (self.queue[i] * self.queue[i+1] < 0):
                    return True
        return False

    # Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        else:
            return (self.maxSize - (self.head - self.tail))
    