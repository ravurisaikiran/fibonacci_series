def Fibonacci(n, depth=0):
    indent = "  " * depth
    print(f"{indent}Fibonacci({n}) called")
    
    if n == 0:
        print(f"{indent}Returning 0")
        return 0
    if n == 1:
        print(f"{indent}Returning 1")
        return 1
    
    result = Fibonacci(n - 1, depth + 1) + Fibonacci(n - 2, depth + 1)
    print(f"{indent}Fibonacci({n}) returns {result}")
    return result

print("Tracing recursive call stack for Fibonacci(5):")
stack = []

def debug_Fibonacci(n, depth=0):
    indent = "  " * depth
    stack.append(f"Fibonacci({n})") 
    print(f"{indent}Fibonacci({n}) called")
    
    if n == 0:
        print(f"{indent}Returning 0")
        return 0
    if n == 1:
        print(f"{indent}Returning 1")
        return 1
    
    result = debug_Fibonacci(n - 1, depth + 1) + debug_Fibonacci(n - 2, depth + 1)
    print(f"{indent}Fibonacci({n}) returns {result}")
    
    if depth == 0:
        print("Call Stack Sequence:")
        print(" -> ".join(stack))
    
    return result

debug_Fibonacci(5)
