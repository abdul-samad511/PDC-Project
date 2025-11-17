Parallel and Distributed Computing – Chapter 4
Message Passing using MPI (mpi4py)

Chapter 4: Message Passing Interface (MPI)

Objective:
The objective of this chapter is to understand interprocess communication using MPI in Python with the mpi4py library. Each example demonstrates various communication mechanisms such as broadcast, scatter, point-to-point communication, reduction operations, and the concept of virtual topologies.

Tools & Technologies:
- Language: Python 3
- Library: mpi4py
- IDE: Visual Studio Code
- Execution Environment: mpiexec / mpirun

Folder Structure:
PDC-Chapter4/
│
├── broadcast_test.py
├── deadlock_prob_test.py
├── math_task.py
├── MPI_test.py
├── point_to_point_communication_test.py
├── reduction_test.py
├── scatter_test.py
├── virtual_topology_test.py
└── README.md

1. broadcast_test.py
Objective:
To demonstrate broadcasting of data from one process (root) to all other processes.

Theory:
Broadcast is a collective operation in MPI where one process shares the same data with all other processes in the communicator.

Code Explanation:
- The root process initializes a variable.
- comm.bcast() is used to send the value to all other processes.
- Each process prints the received data.

Expected Output:
All processes display the same broadcasted value from the root.

Conclusion:
Broadcast enables efficient one-to-all communication in MPI programs.

2. deadlock_prob_test.py
Objective:
To illustrate the concept of deadlock in point-to-point communication.

Theory:
Deadlocks occur when processes wait indefinitely for messages from each other, blocking progress.

Code Explanation:
- Each process sends and receives messages in a circular manner.
- Incorrect ordering of send/recv calls leads to a deadlock scenario.

Expected Output:
The program may hang due to both processes waiting for each other.

Conclusion:
Proper ordering or use of non-blocking communication avoids deadlocks in MPI programs.

3. math_task.py
Objective:
To perform mathematical operations collectively using MPI.

Theory:
This script demonstrates basic parallel numerical tasks and can serve as a base for implementing different MPI operations like Scatter, Gather, and Reduce.

Code Explanation:
- Initializes MPI communicator and ranks.
- Distributes mathematical computations across processes.
- Can be modified to test various communication patterns.

Expected Output:
Each process contributes to the computation and prints partial results.

Conclusion:
MPI allows efficient parallel computation and data distribution for numeric tasks.

4. MPI_test.py
Objective:
To verify MPI environment setup and basic communication between processes.

Theory:
Before implementing complex communication, it’s essential to confirm that mpi4py is installed and MPI is functioning.

Code Explanation:
- Initializes MPI and prints process rank and total size.
- Used as a basic test script for environment validation.

Expected Output:
Displays each process rank and total number of processes.

Conclusion:
Confirms successful MPI environment setup and interprocess communication.

5. point_to_point_communication_test.py
Objective:
To demonstrate direct communication between two MPI processes.

Theory:
Point-to-point communication involves send and receive operations between specific processes.

Code Explanation:
- Each process sends data to another process using comm.send() and comm.recv().
- Demonstrates explicit data transfer between ranks.

Expected Output:
Processes print the data sent and received from their partner ranks.

Conclusion:
Point-to-point communication forms the basis of all MPI interactions and is useful for fine-grained control.

6. reduction_test.py
Objective:
To perform collective data reduction using MPI Reduce.

Theory:
Reduce combines data from all processes using a specified operation (sum, max, min, etc.) and stores the result on the root process.

Code Explanation:
- Each process prepares a numeric array.
- comm.Reduce() is used with the MPI.SUM operation.
- Root process prints the final reduced result.

Expected Output:
Root process displays the sum of all arrays from each rank.

Conclusion:
Reduction operations efficiently combine distributed data across processes.

7. scatter_test.py
Objective:
To demonstrate distribution of array elements to multiple processes using Scatter.

Theory:
Scatter is a collective communication operation that divides data from the root process and sends individual parts to each process.

Code Explanation:
- Root process creates an array.
- comm.scatter() distributes one element to each process.
- Each process prints the received value.

Expected Output:
Each process receives a unique value from the root array.

Conclusion:
Scatter allows efficient one-to-many data distribution among processes.

8. virtual_topology_test.py
Objective:
To illustrate the concept of virtual process topology in MPI.

Theory:
Virtual topologies map logical communication patterns (like grid or ring structures) onto physical processes to simplify communication.

Code Explanation:
- Creates a Cartesian topology using Create_cart().
- Displays coordinates and neighbors for each process.

Expected Output:
Each process prints its position and neighbor ranks within the virtual grid.

Conclusion:
Virtual topologies improve communication efficiency and structure in complex MPI applications.

Overall Conclusion:
This collection of MPI programs demonstrates both point-to-point and collective communication in Python using mpi4py. Understanding these primitives forms the foundation for scalable distributed systems and parallel computation.

How to Run:
Use the mpiexec or mpirun command to run MPI programs.

Example:
mpiexec -n 4 python broadcast_test.py
mpirun -n 4 python scatter_test.py
