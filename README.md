data-structures
===============

##Types of data structures in this repository

    - Singly-linked list
        The singly-linked list is implemented without using the native Python list construction. There are two classes:
        a Node class and a List class. Each Node has a single pointer to the Node that follows it. The List has functions
        including `insert`, `remove`, and `pop`. 
    - Doubly-linked list
        The doubly-linked list is implemented without using the native Python list construction. There are also two 
        classes: a Node class and a List class. Each Node has two pointers: one pointing to the Node that follows and one
        pointing to the Node that precedes it. The List has functions including `insert`, `append`, `pop`, `shift`, and
        `remove`. 
    - Binary Heap
        The binary heap can be initialized as either a "min heap" (where the smallest value is always the head of the 
        heap), or a "max heap" (where the largest value is the head). 
    
##Implementations of these data structures

    - Queue
    - Stack
    - Priority Queue
        The priority queue is implemented with an underlying binary heap data structure. The queue supports the following
        methods: `push`, `pop`, and `peek`. Nodes are initialized with a "data" value and a manually set "priority" 
        value which must be an integer. Each Node is initialized with a unique order. Nodes are sorted first according to
        priority (where the maximum value is the highest priority), and second according to order (where the lowest
        "order", i.e. priority of initialization, is the highest priority. 
        
        
##Miscellaneous content

    -Simple parentheses checker
        -Takes a single string as a parameter
        -Checks to see if the string is in one of three conditions: has unclosed parentheses, has at least one "broken" 
        paren, or contains only well-formed parentheses pairs. 
        -Returns -1 for broken, 0 for well-formed, and 1 for unclosed parentheses. 

##Weighing when to use singly- or doubly-linked lists

While most tasks probably *could* be implemented with either a single or a doubly linked list, in some cases there will be reasons to refer one over the other. In principle, anything that can be done with a doubly-linked list could presumably be accomplished with a singly-linked list, but iterating over a very large singly-linked list in reverse order could be prohibitively costly to process. On the other hand, a doubly-linked list requires more storage space than a singly-linked list, since it has double the pointers.  

Resources used include:

    http://en.wikipedia.org/wiki/Linked_list

    http://alextrle.blogspot.com/2011/05/write-linked-list-in-python.html
    
    example using "yield"
    http://stackoverflow.com/questions/280243/python-linked-list

Collaborators: Corinne, Duy, Muazzez
