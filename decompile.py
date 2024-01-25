import idaapi

def decompile_func(ea):
    # Check if the Hex-Rays plugin is initialized successfully
    if not init_hexrays_plugin():
        return False

    # Get the function object from the effective address
    func = idaapi.get_func(ea)
    if func is None:
        return False

    # Attempt to decompile the function
    cfunc = decompile(func)
    if cfunc is None:
        return False

    # Retrieve the pseudocode lines from the decompiled function
    pseudocode_lines = [idaapi.tag_remove(line.line) for line in cfunc.get_pseudocode()]

    # Join the lines and return the decompiled function code
    return "\n".join(pseudocode_lines)
