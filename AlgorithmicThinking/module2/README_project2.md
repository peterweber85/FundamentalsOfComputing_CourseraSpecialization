Project #2 Description

For the Project component of Module 2, you will first write Python code that implements breadth-first search. Then, you will use this function to compute the set of connected components (CCs) of an undirected graph as well as determine the size of its largest connected component. Finally, you will write a function that computes the resilience of a graph (measured by the size of its largest connected component) as a sequence of nodes are deleted from the graph.

You will use these functions in the Application component of Module 2 where you will analyze the resilience of a computer network, modeled by a graph. As in Module 1, graphs will be represented using dictionaries.

Breadth-first search

For this part of Project 2, you will implement the pseudo-code for BFS-Visitedfrom question 13 in Homework 2. In particular, your task is to implement the following function:

𝚋𝚏𝚜_𝚟𝚒𝚜𝚒𝚝𝚎𝚍(𝚞𝚐𝚛𝚊𝚙𝚑, 𝚜𝚝𝚊𝚛𝚝_𝚗𝚘𝚍𝚎) - Takes the undirected graph 𝚞𝚐𝚛𝚊𝚙𝚑 and the node 𝚜𝚝𝚊𝚛𝚝_𝚗𝚘𝚍𝚎 and returns the set consisting of all nodes that are visited by a breadth-first search that starts at 𝚜𝚝𝚊𝚛𝚝_𝚗𝚘𝚍𝚎.
To implement the queue used in BFS, we recommend one of two options. For desktop Python users, you may use the 𝚌𝚘𝚕𝚕𝚎𝚌𝚝𝚒𝚘𝚗𝚜.𝚍𝚎𝚚𝚞𝚎 module which supports O(1) enqueue and dequeue operations. Use the statement 𝚏𝚛𝚘𝚖 𝚌𝚘𝚕𝚕𝚎𝚌𝚝𝚒𝚘𝚗𝚜 𝚒𝚖𝚙𝚘𝚛𝚝 𝚍𝚎𝚚𝚞𝚎 to import this module for use with OwlTest. Note that using the list operations 𝚙𝚘𝚙(𝟶) and 𝚊𝚙𝚙𝚎𝚗𝚍(...) to model enqueue and dequeue will lead to a slower implementation since popping from the front of a list is O(n) in desktop Python.

For CodeSkulptor users, the list operations 𝚙𝚘𝚙(𝟶) and 𝚊𝚙𝚙𝚎𝚗𝚍(...) both have fast implementations in CodeSkulptor. As a result, you are welcome to either import the 𝚙𝚘𝚌_𝚚𝚞𝚎𝚞𝚎 module provided for "Principles of Computing" (via the statement 𝚒𝚖𝚙𝚘𝚛𝚝 𝚙𝚘𝚌_𝚚𝚞𝚎𝚞𝚎) or directly implement a queue using the list operations 𝚙𝚘𝚙(𝟶) and 𝚊𝚙𝚙𝚎𝚗𝚍(...).

Connected components

For this part of Project 2, you will implement the pseudo-code forCC-Visited from question 13 in Homework 2. In particular, your task is to implement the following two functions:

𝚌𝚌_𝚟𝚒𝚜𝚒𝚝𝚎𝚍(𝚞𝚐𝚛𝚊𝚙𝚑) - Takes the undirected graph 𝚞𝚐𝚛𝚊𝚙𝚑 and returns a list of sets, where each set consists of all the nodes (and nothing else) in a connected component, and there is exactly one set in the list for each connected component in 𝚞𝚐𝚛𝚊𝚙𝚑 and nothing else.
𝚕𝚊𝚛𝚐𝚎𝚜𝚝_𝚌𝚌_𝚜𝚒𝚣𝚎(𝚞𝚐𝚛𝚊𝚙𝚑) - Takes the undirected graph 𝚞𝚐𝚛𝚊𝚙𝚑 and returns the size (an integer) of the largest connected component in 𝚞𝚐𝚛𝚊𝚙𝚑.
To ensure an efficient implementation of 𝚌𝚌_𝚟𝚒𝚜𝚒𝚝𝚎𝚍, we recommend that you use the function 𝚋𝚏𝚜_𝚟𝚒𝚜𝚒𝚝𝚎𝚍 in implementing 𝚌𝚌_𝚟𝚒𝚜𝚒𝚝𝚎𝚍.

Graph resilience

In the Application component of this Module, we will study the connectivity of computer networks. In particular, we will subject a model of one particular network to random and targeted "attacks". These attacks correspond to disabling a sequence of servers in the network and will be simulated by removing a sequence of nodes in the graph that corresponds to these servers.

For this part of the Project, your task is to implement a function that takes an undirected graph and a list of nodes that will be attacked. You will remove these nodes (and their edges) from the graph one at a time and then measure the "resilience" of the graph at each removal by computing the size of its largest remaining connected component. In particular, your task is to implement the function:

𝚌𝚘𝚖𝚙𝚞𝚝𝚎_𝚛𝚎𝚜𝚒𝚕𝚒𝚎𝚗𝚌𝚎(𝚞𝚐𝚛𝚊𝚙𝚑, 𝚊𝚝𝚝𝚊𝚌𝚔_𝚘𝚛𝚍𝚎𝚛) - Takes the undirected graph 𝚞𝚐𝚛𝚊𝚙𝚑, a list of nodes 𝚊𝚝𝚝𝚊𝚌𝚔_𝚘𝚛𝚍𝚎𝚛 and iterates through the nodes in 𝚊𝚝𝚝𝚊𝚌𝚔_𝚘𝚛𝚍𝚎𝚛. For each node in the list, the function removes the given node and its edges from the graph and then computes the size of the largest connected component for the resulting graph. The function should return a list whose k+1th entry is the size of the largest connected component in the graph after the removal of the first k nodes in 𝚊𝚝𝚝𝚊𝚌𝚔_𝚘𝚛𝚍𝚎𝚛. The first entry (indexed by zero) is the size of the largest connected component in the original graph.
The easiest method for implementing 𝚌𝚘𝚖𝚙𝚞𝚝𝚎_𝚛𝚎𝚜𝚒𝚕𝚒𝚎𝚗𝚌𝚎 is to remove one node at a time and use 𝚕𝚊𝚛𝚐𝚎𝚜𝚝_𝚌𝚌_𝚜𝚒𝚣𝚎 to compute the size of the largest connected component in the resulting graphs. This implementation has a running time of O(n(n+m)) where n is the number of nodes and m is the number of edges in the graph.

Challenge problem: In the Application, you will compute the resilience of graphs with several thousand nodes and edges. In desktop Python, this computation will take on the order of a few seconds. In CodeSkulptor, this computation will take 3-5 minutes per graph. As a challenge, investigate other asymptotically faster approaches to implementing 𝚌𝚘𝚖𝚙𝚞𝚝𝚎_𝚛𝚎𝚜𝚒𝚕𝚒𝚎𝚗𝚌𝚎. We have implemented one approach based on a simple disjoint set algorithm that has a running time of O(nlog(n)+m). This method can perform all of the analysis in the Application part of this Module in CodeSkulptor in a few seconds.

Please note that we strongly recommend that you use 𝚕𝚊𝚛𝚐𝚎𝚜𝚝_𝚌𝚌_𝚜𝚒𝚣𝚎 in your first implementation of 𝚌𝚘𝚖𝚙𝚞𝚝𝚎_𝚛𝚎𝚜𝚒𝚕𝚒𝚎𝚗𝚌𝚎 when completing the Project and Application. If you wish to use CodeSkulptor, but would like to avoid the 3-5 minute wait times, you can compute the resiliences in IDLE and paste the resulting data back into CodeSkulptor for plotting.

Grading and coding standards

As you implement each function, remember to test that function thoroughly using test data of your creation. Once you are confident that your implementation is correct, submit your code to this Owltest page. This page will automatically test your project. The example graphs used in OwlTest are available here.

OwlTest uses Pylint to check that you have followed the coding style guidelines for this class. Deviations from these style guidelines will result in deductions from your final score. Please read the feedback from Pylint closely. If you have questions, feel free to consult this page and the class forums.

When you are ready to submit your code to be graded formally, submit your code to the CourseraTest page for this project that is linked on the main programming assignment page. Remember that submitting to OwlTest does not record a grade for the assignment.
