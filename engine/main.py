import numpy as np


## Identifiera strömmarna



## Definiera in-stream and out-stream
## Define System Boundaries

## Mixer, Separator, Total

# Core math:
## in - out + generated - consumed = 0

# Unknowns

A = np.array([[1, 0, 0, 0, 0], 
              [0, 1, 0, 0, 0], 
              [1, 1, 1, -1, 0], 
              [0, 0, -1, 0.3, 0], 
              [0, 0, 0, 0.7, -1]])

b = np.array([5,2,0,0,0])

print("Answer is", np.linalg.solve(A, b.T))

def textInput():
    answer = 0 
    if input == "":
        print("try again")
    else:
        answer = input()

    return answer

def splitter():
    # out = 0.7
    # back in = 0.3
    return 0

def main():
    return 0


if __name__ == "__main__":
    main()

