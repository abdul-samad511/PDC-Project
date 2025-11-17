# virtual_topology_test.py
from mpi4py import MPI
import numpy as np
from math_task import do_something  # reuse your math function

# Define direction constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0, 0, 0, 0]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    # Determine grid dimensions (closest to square)
    grid_row = int(np.floor(np.sqrt(size)))
    grid_column = size // grid_row

    # Adjust in case of mismatch
    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print(f"Building a {grid_row} x {grid_column} grid topology:\n")

    # Create the Cartesian communicator (2D virtual topology)
    cartesian_communicator = comm.Create_cart(
        (grid_row, grid_column),
        periods=(True, True),  # wrap-around (toroidal grid)
        reorder=True
    )

    # Obtain coordinates of the current process in the grid
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)

    # Identify neighbouring processes in all four directions
    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    # Display topology information for each process
    print(
        f"Process {rank} -> Row: {my_mpi_row}, Column: {my_mpi_col}\n"
        f"  Neighbour[UP]    = {neighbour_processes[UP]}\n"
        f"  Neighbour[DOWN]  = {neighbour_processes[DOWN]}\n"
        f"  Neighbour[LEFT]  = {neighbour_processes[LEFT]}\n"
        f"  Neighbour[RIGHT] = {neighbour_processes[RIGHT]}"
    )

    # Each process performs its math task
    count = rank + 2  # different work size per process
    results = []
    do_something(count, results)
    print(f"Process {rank} computed sum of cubes (count={count}): {results[0]}\n")
