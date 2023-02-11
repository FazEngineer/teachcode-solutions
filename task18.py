# A Module is a file consisting of Python code. A module can define functions, 
# classes and variables. A module can also include runnable code.
# Most commonly used modules are: math, time, os. 
# In order to use their functions, we can import them like: import module_name 
# and use the functions defined inside the module by modulename.func_name()

import time

local_time = time.asctime(time.localtime(time.time()))
print(local_time)