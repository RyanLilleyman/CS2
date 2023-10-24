import numpy as np

def unique():
    print("Problem 1")
    arr1 = np.array([10,10,20,20,30,30])
    arr2 = np.array([[1,1],[2,3]])
    print(f"""
    Array 1: 
    {arr1}

    Unique: {np.unique(arr1)}

    Array 2: 
    {arr2}

    Unique: {np.unique(arr2)}

    """)

def another_shape():
    print()
    print("Problem 2")
    print(arr := np.array([1,2,3,4,5,6]),end = "\n")
    print(arr.reshape(3,2),end = "\n")
    print(arr.reshape(2,3),end = "\n")
    
def one_diagonals():
    print()
    print("Problem 3")
    print(np.eye(3),end = "\n")

def diagonals():
    print()
    print("Problem 4")
    print(np.diag([4,5,6,7]),end = "\n")

def main():
    unique()
    another_shape()
    one_diagonals()
    diagonals()
    




if __name__ == "__main__":
    main()