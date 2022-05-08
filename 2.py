#AMJITH PP 20219016


import os


def main():
    n = int(input("Enter the number of numbers: "))

    r1, w1 = os.pipe()
    r2, w2 = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r1)
        os.close(w2)
        w1 = os.fdopen(w1, "w")
        for i in range(n):
            number = input(f"Enter number {i+1}: ")
            w1.write(f"{number},")
        w1.close()
        r2 = os.fdopen(r2)
        string = r2.read()
        print(f"Parent reads: {string}")
        r2.close()
    else:
        os.close(w1)
        os.close(r2)
        r1 = os.fdopen(r1)
        number_string = r1.read()
        print(f"Child reads: {number_string}")
        prime = []
        is_prime = True
        numbers = number_string.split(",")
        numbers.pop()  # Remove the last empty string from the list of numbers
        for i in numbers:
            is_prime = True
            for j in range(2, int(i)):
                if int(i) % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime.append(i)
        r1.close()
        w2 = os.fdopen(w2, 'w')
        w2.write(",".join(prime))
        w2.close()


if __name__ == "__main__":
    main()
#OUTPUT
"""
Enter the number of numbers: 5
Enter number 1: 2
Enter number 2: 3
Enter number 3: 4
Enter number 4: 5
Enter number 5: 6
Child reads: 2,3,4,5,6,
Parent reads: 2,3,5
"""
