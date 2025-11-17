# point_to_point_communication_test.py
from mpi4py import MPI
from math_task import do_something  # using your existing math_task.py function

comm = MPI.COMM_WORLD
rank = comm.rank

print("my rank is:", rank)

# Process 0 sends an integer to process 4
if rank == 0:
    data = 10  # smaller number for demonstration
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("sending data %s " % data + " to process %d" % destination_process)

# Process 1 sends a string to process 8
if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data, dest=destination_process)
    print("sending data %s :" % data + " to process %d" % destination_process)

# Process 4 receives data from process 0 and uses it in math_task.py
if rank == 4:
    data = comm.recv(source=0)
    print("data received is =", data)

    results = []
    do_something(data, results)
    print(f"Process {rank}: Computed sum of cubes (with {data} iterations) = {results[0]}")

# Process 8 receives data from process 1
if rank == 8:
    data1 = comm.recv(source=1)
    print("data1 received is =", data1)
