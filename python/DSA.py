#List
a=[10,20,"GFG",True]
print(a)

#Searching Algorithms
import bisect
A=[2,4,6,8,10]

#linear search using 'in'
print(6 in a)

#Linear search using 'count'
print(a.count(7)>0)

#Binary search using bisect
pos = bisect.bisect_left(A,0)
print("Food at index:",pos)

#Sorting Algorithms
nums=[5,3,8,1]

#In-place sort
nums.sort()
print(nums)

#New sorted list(desending)
print(sorted(nums, reverse=True))

#String
s="Hello Geeks"
print(s)

#Set
a={10,20,20,"GFG",True,True}
print(a)

#Creating a Dictionary
d = {10: "hello",20 : "geek","hello": "world", 2.0:55}
print(d)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))

#Recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

#Stack
stack=[]
#append() function to push element in the stack
stack.append('g')
stack.append('f')
stack.append('g')

print("Initial stack")
print(stack)

#LIFO ordwe
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())

print("nStack after elements are popped:")
print(stack)

#Queue
queue=[]
#Adding elements to the queue
queue.append("g")
queue.append("f")
queue.append("g")

print("Initial queue")
print(queue)

#removing elements
print("Elements dequeued from the queue")
print(queue.pop(0))

print("Queue after removing")
print(queue)

# Linked List
# Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    # Create nodes and link them
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    # Traverse and print linked list
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
#Tree

class Node :
    def __init__(self,v):
        self.data = v
        self.left = None
        self.right = None

def printInorder(root):
    if(root == None):
        return 
    printInorder(root.left)
    print(root.data,end = "")
    printInorder(root.right)

if __name__ == "__main__":
   root = Node(1)
   root.left = Node(2)
   root.right = Node(3)

   printInorder(root)

#Heap

import heapq
a = [5,7,9,1,3]

heapq.heapify(a)
print("The created heap is:",a)

heapq.heappush(a,4)
print("The modified heap after push is:",a)

print("The smallest element is:",heapq.heappop(a))

#Graphs
def addEdge(adj, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))

def displayAdjList(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
    print()

def main():

    V = 3
    adj = [[] for _ in range(V)]

    addEdge(adj, 1, 0, 4)
    addEdge(adj, 1, 2, 3)
    addEdge(adj, 2, 0, 1)

    print("Adjacency List Representation:")
    displayAdjList(adj)

if __name__ == "__main__":
    main()