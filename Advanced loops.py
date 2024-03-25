#!/usr/bin/env python
# coding: utf-8

# In[1]:


def board():
    row = int(input("Specify the number of boxes in the row: "))
    column = int(input("Specify the number of boxes in the columns: "))
    for r in range(1,row*2):    #need to add 2 to the initial variable
        if r%2==1:   #will run if the row is odd
            for c in range(1,(column*2)):
                if c%2==1:
                    if c!=((column*2-1)):
                        print(" ", end="")
                    else:
                        print(" ")
                else:   #will run if the column is even
                    print("|", end="")

        else:          #will run if the row number is even. Will divide the writable parts.
            print ("_"*(column*2))
    return True


# In[ ]:




