def left(i):
  return 2*i+1  

def right(i): 
  return 2*i+2 

def max_heapify(arr,node):
  if(node in range(0,len(arr))):
    largest = node
    #print(node)
    #print(left(node))
    #print(right(node))
    #print("--")
    if(left(node)<=len(arr)-1):
      if(arr[largest]<arr[left(node)]):
        largest = left(node)
    if(right(node)<=len(arr)-1):
      if(arr[largest]<arr[right(node)]):
        largest = right(node)
    arr[node],arr[largest] = arr[largest],arr[node]
    if(largest!=node):
      max_heapify(arr,largest)
    
def heapify(arr):
  for j in range(int(len(arr)-1),-1,-1):
    #print("j: "+str(j))
    max_heapify(arr,j)

def heap_sort(arr):
  i = 0
  return i

  
arr = []
raw = input().split()
for i in raw:
  arr.append(int(i))
heapify(arr)
print(arr)

  
