import numpy
from mpi4py import MPI
from math_task import do_something 

# Initialize communicator
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Each process performs its math task
results = []
do_something(5, results)  # each process computes sum of cubes for 5 random numbers
local_sum = results[0]

# Prepare send and receive arrays
array_size = 10
senddata = numpy.array([(rank + 1) * i for i in range(array_size)], dtype=numpy.int32)
recvdata = numpy.zeros(array_size, dtype=numpy.int32)

print(f"Process {rank} sending array: {senddata}")
print(f"Process {rank} local computation result (sum of cubes): {local_sum}")

# Perform reduction across all processes
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

# Root process displays the result of reduction
if rank == 0:
    print("\n=== After MPI Reduce (SUM) ===")
    print(f"Reduced data on root process {rank}: {recvdata}")
