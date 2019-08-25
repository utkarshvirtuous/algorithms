def insertion_sort(arr):
  for j in range(1,len(arr)):
    i = j-1
    key = arr[j]
    while(arr[i]>key and i>=0):
      arr[i+1] = arr[i]
      i = i-1
    arr[i+1] = key
  return arr

def merge(arr,start,mid,end):
  #print(arr[start:end+1])
  left = []
  right = []
  left = arr[start:mid+1]
  right = arr[mid+1:end+1]
  j = 0
  k = 0
  i = start
  while(i<=end):
    if(j>=len(left)):
      break
    if(k>=len(right)):
      break
    if(left[j]<right[k]):
      arr[i] = left[j]
      j = j+1
    elif(left[j]>=right[k]):
      arr[i] = right[k]
      k = k+1
    i = i + 1
  while(j<=len(left)-1):
    arr[i] = left[j]
    i = i+1
    j = j+1
  while(k<=len(right)-1):
    arr[i] = right[k]
    i = i+1
    k = k+1
  #print(arr[start:end+1])
  return



def merge_sort(arr,start,end):
  mid = int((end+start)/2)
  if(start<end):
    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    merge(arr,start,mid,end)
  elif(start==end):
    return 
  else:
    print("error ocurred")
    return

arr = []
raw = input().split()
for i in raw:
  arr.append(int(i))
#print(insertion_sort(arr))
#mid = int((len(arr)-1)/2)
merge_sort(arr,0,(len(arr)-1))
print(arr)
