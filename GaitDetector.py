# Gait Detector - Rehab Engineering
# Gait detection algorithm for ananlyzing real-time gait cycle data using a Circular Buffer. 
# Written by: Travis Tomer

from Buffer import CircularBuffer as cb
import numpy as np


# INITIALIZE FLAGS
BUFFER_FULL = False # Used to fill buffer before calculations are made
HC_FLAG = False     # Used for determining if a Heel Contact event is coming
TO_FLAG = False     # Used for determining if a Toe Off event is coming
LAST_EVENT = 1      # 1: Heel Contact, 4: Toe Off


# Set threshold for gait detection algorithm [rad/s] ***MAY NEED CHANGED ON PERSON TO PERSON BASIS***
THRESHOLD = 1 # rad/s


# Useful Functions
def getSamplingFrequency(dtime):
    return (1 / dtime)



#######################################################################################################################
# READING DATA FILES #

# Import healthy foot data from csv
healthyFootGyroFile = "./Data/Test01_GyroXHealthyFoot.csv"
data = np.loadtxt(open(healthyFootGyroFile, "rb"), dtype=float, delimiter=",", skiprows=1)
#Extract time
time = data[:,0]
# Extract healthy foot gryo data (x-axis) - ****In my case it is the x-axis but you want to get the gryo for dorsi/plantar felxion of the ankle****
gyro = data[:,1]

# Calculate sampling frequency
fs = int(getSamplingFrequency(time[1]))
print("Sampling frequency = " + str(fs) + "Hz")

# END OF READING DATA FILES #
#######################################################################################################################



# Create Buffers (Buf1: For healthy foot, Buf2: For affected foot)
# BufferSize = 1/5 of the sampling frequency
healthyBuf = cb(int((1/15) * fs))
print("Buffer size = " + str(int((1/15) * fs)))
print(healthyBuf.maxSize)


# Simulate live data
for i in range(0,len(time)):
    # Enqueue (add) data until buffer is full.  enqueue funciton returns false if the buffer is full.
    # Buffer is full when tail = head - 1
    if BUFFER_FULL == False:
        if (healthyBuf.size() < healthyBuf.maxSize - 1):
            
            healthyBuf.enqueue(gyro[i]) # Fill buffer with latest gyro data

        else:
            BUFFER_FULL = True
    else: # Begin calculations once buffer is full

        # Delete oldest data point
        healthyBuf.dequeue()
        # Update the buffer with most recent data point
        healthyBuf.enqueue(gyro[i])

        # Toe Off Detection
        if TO_FLAG == False:
            if healthyBuf.avgValue() > THRESHOLD and healthyBuf.isAscending():
                TO_FLAG = True
        elif TO_FLAG == True: 
            if healthyBuf.isDescending():
                if LAST_EVENT == 1:
                    print("TOE OFF AT: " + str(time[i]) + "     Index: " + str(i))
                    LAST_EVENT = 4
                TO_FLAG = False        





# Test case (right before toe off event.  Toe off occurs at index 2530/2531)
#data = gyro[2505:2531]
#buf = cb(26)
#for i in range(0,25):
#    buf.enqueue(data[25 - i])


#print(buf.isAscending())