#AMJITH PP 20219016

import os


def main():
    n = int(input(
        "Enter the number of numbers to be sent from parent process to child process: "))
    r, w = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r)
        w = os.fdopen(w, "w")
        for i in range(n):
            num = input(f"Enter number: ")
            w.write(num)
        w.close()
    else:
        os.close(w)
        r = os.fdopen(r)
        number = r.read()
        print("Child Process Reads: ", number)
        r.close()


if __name__ == "__main__":
    main()
    
#OUTPUT
"""Enter the number of numbers to be sent from parent process to child process: 5
Enter number: 40
Enter number: 60
Enter number: 20
Enter number: 10
Enter number: 15
Child Process Reads:  4060201015
"""
