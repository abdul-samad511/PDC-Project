from mpi4py import MPI
from math_task import do_something  # use your existing math_task.py function

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Process 0 defines the variable to share
if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None

# Broadcast variable from root (rank 0) to all processes
variable_to_share = comm.bcast(variable_to_share, root=0)

# Each process uses the shared variable in its math computation
results = []
do_something(variable_to_share, results)

# Print output from each process
print(f"Process {rank} received variable = {variable_to_share}")
print(f"Process {rank} result (sum of cubes) = {results[0]}")
