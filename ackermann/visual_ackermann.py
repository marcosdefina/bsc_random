import time

def ackermann(i, j, depth=0):
    print(" " * depth * 4 + f"|-> ackermann({i}, {j})")
    time.sleep(DELAY)

    if i == 0:
        result = j + 1
        print(" " * depth * 4 + f"|   Result: {result}")
        return result
    elif j == 0:
        result = ackermann(i - 1, 1, depth + 1)
        print(" " * depth * 4 + f"|   Returning: {result}")
        return result
    else:
        inner_result = ackermann(i, j - 1, depth + 1)
        result = ackermann(i - 1, inner_result, depth + 1)
        print(" " * depth * 4 + f"|   Returning: {result}")
        return result


def visual_ackermann(i, j):
    print(f"Starting Ackermann function with i={i}, j={j}")
    result = ackermann(i, j)
    print(f"Final Result: {result}")


if __name__ == "__main__":
    #Recommended i = 3, j = 4 - it's mesmerizing
    i = 2
    j = 5
    DELAY = 0.1  # delay in seconds for visual effect
    visual_ackermann(i, j)