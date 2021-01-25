import sys
import os
letters_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                "X": 24, "Y": 25, "Z": 26, " ": 27}
dict_values = [i for i in letters_dict.values()]  # I will use these index for finding letter with number.
dict_keys = [i for i in letters_dict.keys()]
key, liste, n_square = [], [], 0
try:    # It is for opening files.
    if len(sys.argv) != 5:
        raise IndexError
    if sys.argv[2][-4:] != ".txt":
        raise IndentationError
    if sys.argv[3][-4:] != ".txt":
        raise IOError
    o_type = sys.argv[1]
    key_file = open(sys.argv[2], "r")
    plain_input_file = open(sys.argv[3], "r")
    outputfile = open(sys.argv[4], "w")
except IndexError:
    print("Parameter number error")
    exit()
except FileNotFoundError:
    if os.path.exists(sys.argv[2]):
        print("Input file not found error")
    elif os.path.exists(sys.argv[3]):
        print("Key file not found error")
    exit()
except IOError:
    print("The input file could not be read error")
    exit()
except IndentationError:
    print("Key file could not be read error")
    exit()


def determinant(liste):
    """this func will find the determinant of liste for inverse matrix"""
    if len(liste) == 2:
        return liste[0][0] * liste[1][1] - liste[0][1] * liste[1][0]  # It calculates a determinant of 2x2 matrix
    else:                                                             # It calculates a determinant of nxn matrix
        sayac, result, row = 0, 0, 0
        for satir in liste:
            column = 0
            for item in satir:
                sayac += 1
                temp1 = []
                row1 = -1
                for i in liste:
                    row1 += 1
                    temp = []
                    column1 = -1
                    for k in i:
                        column1 += 1
                        if column1 == column or row1 == row:   # I ignore the same row and column
                            continue
                        else:
                            temp.append(k)
                    if temp != []:
                        temp1.append(temp)
                column += 1
                if row == 0:                                   # There is a recursion function
                    if sayac % 2 == 0:
                        result -= (item * determinant(temp1))
                    else:
                        result += (item * determinant(temp1))
            row += 1
    return result


def minor_matrix(liste):
    """this func write item's determinant to it's location"""
    sayac, result, row, minor_matrix = 0, 0, 0, []
    for satir in liste:
        column, minor_matrixxx = 0, []
        for item in satir:
            sayac, row1, temp1 = sayac+1, -1, []
            for i in liste:
                row1, temp, column1 = row1+1, [], -1
                for k in i:
                    column1 += 1
                    if column1 == column or row1 == row:
                        continue
                    else:
                        temp.append(k)
                if temp != [] :
                    temp1.append(temp)
            column += 1
            minor_matrixxx.append(determinant(temp1))
        minor_matrix.append(minor_matrixxx)
        row += 1
    return minor_matrix


def matrix(matrix1, matrix2):
    """"this function calculate matrix"""
    text = []
    for group in matrix2:
        result = []
        for i in range(n):
            result.append([0])
        for i in range(len(matrix1)):
            for j in range(len(group[0])):
                for k in range(len(group)):
                    result[i][j] += matrix1[i][k] * group[k][j]
        message = [i[0] for i in result]
        text.extend(message)
    return text


try:
    for i in key_file:  # It is for prepare key file.
        tmp = []
        for k in i.split(","):
            n_square += 1
            tmp.append(int(k))
        key.append(tmp)
    key_file.close()
    n = int(n_square ** (1/2))
    if o_type == "dec":    # If operation type is decoding, we will work in there
        ciphertext_file = open(sys.argv[3], "r")
        ciphertext = [line.split(",") for line in ciphertext_file.readlines()][0]
        ciphertext_file.close()
        minor_mat = minor_matrix(key)   # It calls minor matrix func
        cofactor, sayacc = [], 0
        if len(key) == 2:
            inverse_key = [[key[1][1], (-1 * key[0][1])], [(-1 * key[1][0]), key[0][0]]]
        else:
            satir = 0
            for i in minor_mat:
                x, sutun = [], 0
                for k in i:     # It multiply items arbitarly with minus one and plus one there
                    x.append(((-1)**(satir+sutun))*k)
                    sayacc, sutun = sayacc+1, sutun+1
                satir += 1
                cofactor.append(x)
            adjugate = []
            for i in range(n):
                adj = []
                for k in range(n):
                    adj.append([])  # I prepare a empty adjugate list
                adjugate.append(adj)
            a = 0
            for i in cofactor:
                b= 0
                for k in i:
                    (adjugate[b])[a] = k    # I change cofactor's item's row with column.
                    b += 1
                a += 1
            deter = 0
            for i in range(n):
                deter += key[0][i] * cofactor[0][i]    # I found number of determinant
            inverse_key = []
            for row in adjugate:
                k = []
                for column in row:
                    k.append((1/deter) * column)
                inverse_key.append(k)               # We have found inverse matrix!!
        sayac, listee, tmp = 0, [], []
        for i in ciphertext:                # It makes groups with using n number
            sayac += 1
            if sayac % n == 0:
                tmp.append([int(i)])
                listee.append(tmp)
                tmp = []
            else:
                tmp.append([int(i)])
        for i in matrix(inverse_key, listee):   # It will print letters according to numbers
            print(dict_keys[dict_values.index(int(i))], end="", file=outputfile)
    elif o_type == "enc":   # If operation type is encoding, we will work in there.
        super = 1/n
        try:
            plain_input = [line for line in plain_input_file.readlines()[0]]
        except IndexError:
            print("Input file is empty error")
            exit()
        plain_input_file.close()
        num_list = [letters_dict[i.upper()] for i in plain_input]
        sayac, tmp = 0, []
        for i in num_list:       # It makes groups with using n number
            sayac += 1
            if sayac % n == 0:
                tmp.append([i])
                liste.append(tmp)
                tmp = []
            else:
                tmp.append([i])
        if tmp != []:
            tmp.extend((n-len(tmp)) * [[27]])  # if it is necessary, It appends space
            liste.append(tmp)
        print(*matrix(key, liste), sep=",", file=outputfile)
    elif o_type not in ["enc", "dec"]:
        raise LookupError  # I chose randomly
except KeyError:
    print("Invalid character in input file error")
except ZeroDivisionError:
    print("Key file is empty error")
except LookupError:
    print("Undefined parameter error")
except ValueError:
    print("Invalid character in key file error")
    exit()
except IOError:
    print("Parameter number error")
