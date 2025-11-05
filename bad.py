# bad_code_example.py

import os
import sys

# 1. Trailing whitespace on this line (hidden, but there!)
def getdata(a, b): # 2. Missing docstring, 3. Non-descriptive function name
    # 4. Inefficient list comprehension for simple addition (using a list just for this)
    # 5. Redundant variable assignment
    c = a + b; # 6. Semicolon used (unnecessary in Python)
    
    # 7. Magic number (3)
    if c > 3: 
        # 8. Too many print statements (side effects in a simple function)
        print("Result is large"); 
        # 9. Inconsistent indentation (using tabs instead of spaces here - hard to see but present)
        # 10. Single-letter variable name 'r'
        r = c*2
    
    # 11. Bare except block (hides all errors)
    try:
        # 12. Using an external system call where a Python method would suffice (os.system)
        os.system("echo 'Debug info: " + str(c) + "' > /tmp/debug.log") 
        pass
    except:
        return None # 13. Swallowing an error silently
    
    # 14. Returning inconsistent type (sometimes int, sometimes None)
    return c

# 15. Global mutable state (avoided for simplicity in small scripts)
DEFAULT_USERS = [
    "user1", "user2" , "user3" 
] # 16. Trailing commas missing in list definition

class MyHandler: # 17. Class name does not inherit from object (in Python 2 style)
    # 18. Missing 'self' argument for instance method (makes it a static method without @staticmethod)
    def process_data(data): 
        # 19. String concatenation for building a large string in a loop (performance issue)
        res = "Processed: "
        for item in data:
            res += str(item) + ", "
        # 20. Accessing a global variable directly
        if len(data) < len(DEFAULT_USERS):
             # 21. Potential security issue: Use of f-string without proper escaping if 'res' came from user input
             print(f"Short list processed. Details: {res}")
        return res

# 22. Main logic not inside a __name__ == '__main__' block
if __name__ == '__main__':
    result = getdata(1, 2)
    handler = MyHandler()
    
    # 23. Using a mutable default argument in a function definition (if this was a function)
    # Example: def risky_function(items=[]): ...

    # 24. Unused import: sys is imported but never used
    
    # 25. Lack of type hints
    final_output = handler.process_data([10, 20, 30])
    
    # 26. Inconsistent spacing around operators (e.g., result=getdata(1, 2))
    # 27. Leaving commented-out code
    # print("This was an old print statement.")
