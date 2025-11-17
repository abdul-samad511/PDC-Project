from mpi4py import MPI
from math_task import do_something  

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Process 0 defines the array to scatter
if rank == 0:
    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
else:
    array_to_share = None

# Scatter one element of the array to each process
recvbuf = comm.scatter(array_to_share, root=0)

print(f"Process {rank} received value: {recvbuf}")

# Each process performs its math task using the received value
results = []
do_something(recvbuf, results)

print(f"Process {rank} computed sum of cubes (with count={recvbuf}): {results[0]}")
