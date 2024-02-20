# Day 6
# February 13, 2024
# Assignment 2

def move_block(blocks, from_position, to_position):
    if blocks[from_position]:
        block = blocks[from_position].pop()
        blocks[to_position].append(block)

def solve_blocks(initial_blocks, final_blocks):
    steps = []
    for final_stack in final_blocks:
        for block in final_stack:
            if block not in [b for stack in initial_blocks for b in stack]:
                print(f"Block {block} is not present in the initial configuration.")
                return None

    for final_stack in final_blocks:
        for block in final_stack:
            for i, stack in enumerate(initial_blocks):
                if block in stack and initial_blocks[i] != final_stack:
                    move_block(initial_blocks, i, [idx for idx, st in enumerate(final_blocks) if block in st][0])
                    steps.append((block, i, [idx for idx, st in enumerate(final_blocks) if block in st][0]))
    return steps

# Example usage:
initial_blocks = [['A'], ['B'], ['C']]
final_blocks = [['C', 'A'], [], ['B']]
solution_steps = solve_blocks(initial_blocks, final_blocks)

if solution_steps is not None:
    print("Initial blocks configuration:")
    for stack in initial_blocks:
        print(stack)

    print("\nFinal blocks configuration:")
    for stack in final_blocks:
        print(stack)

    print("\nSolution steps:")
    for step in solution_steps:
        print(f"Move block {step[0]} from stack {step[1]} to stack {step[2]}")
