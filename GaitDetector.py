# Gait Detector - Rehab Engineering
# Gait detection algorithm for ananlyzing real-time gait cycle data using a Circular Buffer. 
# Written by: Travis Tomer

from Buffer import CircularBuffer as cb
import numpy as np

# Functions
def getSamplingFrequency(dtime):
    return (1 / dtime)

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
healthyBuf = cb(int((1/5) * fs))
print("Buffer size = " + str(int((1/5) * fs)))
print(healthyBuf.maxSize)

# Count used for debugging
count = 0
# Initially put a 0 as the first element in the buffer
healthyBuf.enqueue(0)

# Loop through the data
for i in range(0,len(time)):
    if (healthyBuf.tail != healthyBuf.head):
        # Fill buffer with latest gyro data
        healthyBuf.enqueue(gyro[i])
        count = count + 1
        #print("Filling buf: Gryo = " + str(gyro[i]))
    else:
        # Begin calculations once buffer is full
        print("Buffer Full. Beginning calculations!")
        break

print(count)
print(healthyBuf.queue)




