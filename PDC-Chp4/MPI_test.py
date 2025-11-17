
from mpi4py import MPI
import numpy as np
from math_task import do_something  

# Initialize MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process performs the math task
results = []
do_something((rank + 1) * 5, results)
result = results[0]  # get the computed sum

# Prepare data to send to every process
senddata = np.array([(rank + 1) * (i + 1) + result for i in range(size)], dtype=int)
recvdata = np.empty(size, dtype=int)

# Alltoall communication
comm.Alltoall(senddata, recvdata)

# Display process info
print(f"Process {rank}: sum_of_cubes={result}")
print(f"Process {rank} sending: {senddata}")
print(f"Process {rank} received: {recvdata}\n")
