# logic_gates_for_electronics
# source code: 

def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

def logical_xor(a, b):
    return a ^ b

def print_truth_table(gate_func, gate_name):
    print(f"Truth table for {gate_name}:")
    if gate_name == "NOT":
        print("Input A | Output")
        print("-----------------")
        for a in [False, True]:
            result = gate_func(a)
            print(f"{int(a)}       | {int(result)}")
    else:
        print("Input A | Input B | Output")
        print("---------------------------")
        for a in [False, True]:
            for b in [False, True]:
                result = gate_func(a, b)
                print(f"{int(a)}       | {int(b)}       | {int(result)}")
    print("---------------------------\n")

if __name__ == "__main__":
    print_truth_table(logical_and, "AND")
    print_truth_table(logical_or, "OR")
    print_truth_table(logical_not, "NOT")
    print_truth_table(logical_xor, "XOR")

# For the source code go to the **code ** which is side of the **preview**
