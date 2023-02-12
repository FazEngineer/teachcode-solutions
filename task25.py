# Exception Handling
#  When an error occurs, or exception as we call it, 
# Python will normally stop and generate an error message. 
# These exceptions can be handled using the try statement. Eg
# try: 
#    print(i) 
# except: 
#    print('An Exception Occured') 
# When the try block raises an error, the except block statement gets executed. 
# Without this try-except block, the program may crash. 

try:
    print(1/0)
except:
    print('Zero Division not possible')
