#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main():
    factors = []
    myNumber = 24
    for i in range(1, 25):
        if myNumber%i==0:
            factors.append(i)
    


if __name__ == "__main__":
    main()