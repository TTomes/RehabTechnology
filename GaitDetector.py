# Gait Detector - Rehab Engineering
# Gait detection algorithm for ananlyzing real-time gait cycle data using a Circular Buffer. 
# Written by: Travis Tomer

from Buffer import CircularBuffer as cb
import numpy as np

# Functions
def getSamplingFrequency(dtime):
    return (1 / dtime)


# Define variables
BUFFER_FULL = False


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

# Create Buffers (Buf1: For healthy foot, Buf2: For affected foot)
# BufferSize = 1/5 of the sampling frequency
healthyBuf = cb(int((1/10) * fs))
print("Buffer size = " + str(int((1/10) * fs)))
print(healthyBuf.maxSize)

# Count used for debugging
#count = 0

# Loop through the data
for i in range(0,len(time)):
    # Enqueue's (adds) data until buffer is full.  enqueue funciton returns false if the buffer is full.
    # Buffer is full when tail = head - 1
    if BUFFER_FULL == False :
        if (healthyBuf.size() < healthyBuf.maxSize - 1):
            # Fill buffer with latest gyro data
            healthyBuf.enqueue(gyro[i])

            #Debugging
            #count = count + 1
            #print("Filling buf: Gryo = " + str(gyro[i]))
        else:
            BUFFER_FULL = True
    else:
        # Begin calculations once buffer is full
        print("Buffer Full. Beginning calculations!")

        # Begin TO and HC calculations
        

        break


# Debugging 
#print(count)
#print(healthyBuf.queue)


