y = 20 # Global variable

def access_global():
    print(y) # Can access global variable

access_global() # Output: 20

def modify_global():
    global y
    y = 30 # Now modifying the global variable

modify_global()
print(y) # Output: 30

#this was all done by ehtisham on sohaib laptop because ehtisham was teaching him