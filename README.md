data-structures
===============

##Types of data structures in this repository

    - Singly-linked list
    - Doubly-linked list
    
##Implementations of these data structures

    - Queue
    - Stack

##Miscellaneous content

    -Simple parentheses checker
        -Takes a single string as a parameter
        -Checks to see if the string is in one of three conditions: has unclosed parentheses, has at least one "broken"           paren, or contains only well-formed parentheses pairs. 
        -Returns -1 for broken, 0 for well-formed, and 1 for unclosed parentheses. 

##Weighing when to use singly- or doubly-linked lists

While most tasks probably *could* be implemented with either a single or a doubly linked list, in some cases there will be reasons to refer one over the other. In principle, anything that can be done with a doubly-linked list could presumably be accomplished with a singly-linked list, but iterating over a very large singly-linked list in reverse order could be prohibitively costly to process. On the other hand, a doubly-linked list requires more storage space than a singly-linked list, since it has double the pointers.  

Resources used include:

    http://en.wikipedia.org/wiki/Linked_list

    http://alextrle.blogspot.com/2011/05/write-linked-list-in-python.html
    
    example using "yield"
    http://stackoverflow.com/questions/280243/python-linked-list

Collaborators: Corinne, Duy, Muazzez
