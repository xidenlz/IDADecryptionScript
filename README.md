# Installation:
- Copy the provided Python script (decompile.py) into your IDA Pro's Python directory.

# Usage:
1. Import the idaapi module in your Python script.
2. Use the decompile_func function provided in the script to decompile a specific function.
3. Pass the effective address (EA) of the function you want to decompile as an argument to the decompile_func function.
4. The function returns the decompiled code of the specified function.

# Example 
```py
import idaapi
from decompile import decompile_func

# Example effective address of the function to decompile
ea = 0x12345678

# Attempt to decompile the function at the specified effective address
decompiled_code = decompile_func(ea)

# Print the decompiled code
print("Decompiled Code:")
print(decompiled_code)
```
