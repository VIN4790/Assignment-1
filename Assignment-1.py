#!/usr/bin/env python
# coding: utf-8

# 1.TWO SUM PROBLEM
def chekpair(A,size,x):
    for i in range(0,size-1):
        for j in range(1,size):
           if A[i]+A[j]==x:
                return([i,j])
            
A=[1,3,15,6,5]
size=len(A)
x=7
print(chekpair(A,size,x))

# In[ ]:
class RemoveElement:
    def removeElement(self,nums, val):
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not val
                nums[count] = nums[i]
                count += 1
        return count
r = RemoveElement()
print(r.removeElement([2, 3, 3, 2], 3))



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




