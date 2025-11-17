from mpi4py import MPI
from math_task import do_something 

comm = MPI.COMM_WORLD
rank = comm.rank

print(f"My rank is {rank}")

# Process 1 and Process 5 will communicate with each other
if rank == 1:
    data_send = "a"
    destination_process = 5
    source_process = 5

    # Receive data from process 5 first
    data_received = comm.recv(source=source_process)

    # Then send data to process 5
    comm.send(data_send, dest=destination_process)

    print(f"Sending data '{data_send}' to process {destination_process}")
    print(f"Data received is = '{data_received}'")

    # Perform math task
    results = []
    do_something(5, results)
    print(f"Process {rank} sum of cubes = {results[0]}")


elif rank == 5:
    data_send = "b"
    destination_process = 1
    source_process = 1

    # Send data to process 1 first
    comm.send(data_send, dest=destination_process)

    # Then receive data from process 1
    data_received = comm.recv(source=source_process)

    print(f"Sending data '{data_send}' to process {destination_process}")
    print(f"Data received is = '{data_received}'")

    # Perform math task
    results = []
    do_something(10, results)
    print(f"Process {rank} sum of cubes = {results[0]}")
