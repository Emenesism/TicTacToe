import numpy as np
import random


rows = int(input("Enter your Abaad: "))
cols = rows
size = rows*cols
mat = np.array([0]*size).reshape(rows, cols)


def karbar():
    radif, soton = int(input("Radif: ")), int(input("Soton: "))
    try:
        if mat[radif][soton] == 0:
            mat[radif][soton] = 1
            return mat
        else:
            print("Already chosen!")
            return karbar()
    except IndexError:
        print("Entekhab shoma kharej az Mahdoode Ast")
        return karbar()

    except:
        print("Yek chizi eshtebah pish raft")
        return karbar()



def pc():
    radifpc = random.randint(0, rows-1)
    sotonpc = random.randint(0, rows-1)
    if mat[radifpc][sotonpc] == 0:
        mat[radifpc][sotonpc] = -1
        return mat
    else:
        print("Tavasot Karbar entekhab shode!!")
        return pc()


def karbarcheck(a: list):
    jam1 = 0
    jamg = 0
    jamf = 0
    finish = False
    for i in a:
        if sum(i) == len(a):
            finish = True
        else:
            break
    for i in range(0, (len(a))):
        for j in range(0, (len(a))):

            jam1 += a[j][i]
            if jam1 == len(a):
                finish = True
            elif j == (len(a)) - 1:
                jam1 = 0
            elif j != (len(a)):
                continue

    for i in range(0, (len(a))):
        for j in range(0, (len(a))):
            while i == j:
                jamg += a[i][j]
                if jamg == len(a):
                    finish = True
                else:
                    break

    for i in range(0, (len(a))):
        for j in range(0, (len(a))):

            while i + j == (len(a)) - 1:
                jamf += a[i][j]
                if jamf == len(a):
                    finish = True
                break

    if finish == True:
        print("Karbar Wins")
        return True


def checkpc(b: list):
    finish = False
    jam1 = 0
    jam2 = 0
    jam3 = 0

    for i in b:
        if sum(i) == -1 * (len(b)):
            finish = True
        else:
            continue
    for i in range(0, (len(b))):
        for j in range(0, (len(b))):
            jam1 += b[j][i]
            if jam1 == -1 * (len(b)):
                finish = True
            elif j == len(b) - 1:
                jam1 = 0
            else:
                continue
    for i in range(0, (len(b))):
        for j in range(0, (len(b))):
            while i == j:
                jam2 += b[i][j]
                if jam2 == -1 * (len(b)):
                    finish = True
                else:
                    break

    for i in range(0, (len(b))):
        for j in range(0, (len(b))):
            while i + j == (len(b)) + 1:
                jam3 += b[i][j]
                if jam3 == -1 * (len(b)):
                    finish = True
                else:
                    break
    if finish == True:
        print("Pc Wins")
        return True


def main():
    while True:

        karbar()
        for i in range(2):
            print("  ")
        print(mat)
        if karbarcheck(mat):
            break

        pc()
        print(mat)
        if checkpc(mat):
            break


main()
