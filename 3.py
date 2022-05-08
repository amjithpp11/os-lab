#AMJITH PP 20219016


import os


def main():
    r1, w1 = os.pipe()
    r2, w2 = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r1)
        os.close(w2)
        w1 = os.fdopen(w1, "w")
        string = input("Enter the string: ")
        w1.write(string)
        w1.close()
        r2 = os.fdopen(r2)
        string = r2.read()
        print(f"Parent reads: {string}")
        r2.close()
    else:
        os.close(w1)
        os.close(r2)
        r1 = os.fdopen(r1)
        string = r1.read()
        print(f"Child reads: {string}")
        palindrome = True
        j = 0
        for i in range(len(string) - 1, 0, -1):
            if string[i] != string[j]:
                palindrome = False
                break
            j += 1
        w2 = os.fdopen(w2, 'w')
        if palindrome:
            w2.write(f"{string} is palindrome")
        else:
            w2.write(f"{string} is not palindrome")
        r1.close()
        w2.close()


if __name__ == "__main__":
    main()

#OUTPUT
"""
Enter the string: malayalam
Child reads: malayalam
Parent reads: malayalam is palindrome

Enter the string: hindi
Child reads: hindi
Parent reads: hindi is not palindrome

"""
