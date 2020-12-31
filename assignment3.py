import sys
inputfile = open(sys.argv[1], "r")
commands = [line.split() for line in inputfile.readlines()]
inputfile.close()
board = ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "p1", "p2", "p3", "p4", "p5", "p6","p7", "p8", "r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
map = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a6", "b6", "c6","d6", "e6", "f6", "g6", "h6", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a4", "b4", "c4", "d4", "e4", "f4","g4", "h4", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "a1","b1", "c1", "d1", "e1", "f1", "g1", "h1"]
board1 = board.copy()
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
def color_of_rack(rack):
    color = True
    if rack[0] in ["P", "R", "B", "Q", "K", "N"]:
        color = True
    elif rack[0] in ["p", "r", "b", "q", "k", "n"]:
        color = False
    return color
def showmovess(rack):
    chance = []
    if rack in ["ki", "KI"]:
        chance.extend(king_showmoves(rack))
    elif rack in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
        chance.extend(Pawn_showmoves(rack))
    elif rack in ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]:
        chance.extend(pawn_showmoves(rack))
    elif rack in ["R1", "R2", "r1", "r2"]:
        chance.extend(rook_showmoves(rack))
    elif rack in ["b1", "b2"]:
        chance.extend(bishop_showmoves(rack))
    elif rack in ["B1", "B2"]:
        chance.extend(Bishop_showmoves(rack))
    elif rack in ["qu", "QU"]:
        chance.extend(queen_showmoves(rack))
    elif rack in ["n1", "n2", "N1", "N2"]:
        chance.extend(knight_showmoves(rack))
    return chance
def king_possibility(king):
    king_possib = []
    if map[board.index(king)][0] != "a":
        king_possib.append(map[board.index(king) - 1])
    if map[board.index(king)][0] != "h":
        king_possib.append(map[board.index(king) + 1])
    if map[board.index(king)][1] != "8":
        king_possib.append(map[board.index(king) - 8])
    if map[board.index(king)][1] != "1":
        king_possib.append(map[board.index(king) + 8])
    if map[board.index(king)][0] != "a" and map[board.index(king)][1] != "8":
        king_possib.append(map[board.index(king) - 9])
    if map[board.index(king)][0] != "h" and map[board.index(king)][1] != "8":
        king_possib.append(map[board.index(king) - 7])
    if map[board.index(king)][0] != "a" and map[board.index(king)][1] != "1":
        king_possib.append(map[board.index(king) + 7])
    if map[board.index(king)][0] != "h" and map[board.index(king)][1] != "1":
        king_possib.append(map[board.index(king) + 9])
    return king_possib
def king_showmoves(king):
    king_moves = []
    for aim in king_possibility(king):
        if board[map.index(aim)] == "  ":
            king_moves.append(aim)
        elif color_of_rack(board[map.index(aim)]) != color_of_rack(king) and board[map.index(aim)] not in ["ki", "KI"]:
            king_moves.append(aim)
    return king_moves
def rook_possibility(rook):
    rook_possib = []
    x, y = map[board.index(rook)][0], map[board.index(rook)][1]
    rook_possib.extend([x + "1", x + "2", x + "3", x + "4", x + "5", x + "6", x + "7", x + "8", "|", "a" + y, "b" + y, "c" + y,"d" + y, "e" + y, "f" + y, "g" + y, "h" + y])
    return [rook_possib]
def rook_showmoves(rook):
    rook_moves = []
    x = rook_possibility(rook)[0][:]
    a = x[:x.index(map[board.index(rook)])]
    b = x[x.index(map[board.index(rook)]) + 1:x.index("|")]
    e = x[x.index("|"):]
    c = e[1:e.index(map[board.index(rook)])]
    d = e[e.index(map[board.index(rook)]) + 1:]
    for k in [a[::-1], b, c[::-1], d]:
        for i in k:
            if board[map.index(i)] == "  ":
                rook_moves.append(i)
            elif color_of_rack(board[map.index(i)]) != color_of_rack(rook) and board[map.index(i)] not in ["ki", "KI"]:
                rook_moves.append(i)
                break
            else:
                break
    return rook_moves
def bishop_possibility(bishop):
    a, b = [], []
    x, y, sayac, sayac1, sayac2 = map[board.index(bishop)][0], map[board.index(bishop)][1], 0, 0, 0
    for column in letters:
        sayac += 1
        if column == x:
            for i in letters[sayac:]:
                sayac1 += 1
                if int(y) + sayac1 > 8:
                    break
                a.append(i + str(int(y) + sayac1))
            for k in letters[:sayac - 1][::-1]:
                sayac2 += 1
                if int(y) + sayac2 > 8:
                    break
                b.append(k + str(int(y) + sayac2))
    return [a, b]
def bishop_showmoves(bishop):
    bishop_moves = []
    for i in bishop_possibility(bishop)[0]:
        if board[map.index(i)] == "  ":
            bishop_moves.append(i)
        elif (color_of_rack(board[map.index(i)]) == True) and board[map.index(i)] not in ["ki", "KI"]:
            bishop_moves.append(i)
            break
        else:
            break
    for i in bishop_possibility(bishop)[1]:
        if board[map.index(i)] == "  ":
            bishop_moves.append(i)
        elif (color_of_rack(board[map.index(i)]) == True) and board[map.index(i)] not in ["ki", "KI"]:
            bishop_moves.append(i)
            break
        else:
            break
    return bishop_moves
def Bishop_possibility(bishop):
    a, b = [], []
    x, y, sayac, sayac1, sayac2 = map[board.index(bishop)][0], map[board.index(bishop)][1], 0, 0, 0
    for column in letters:
        sayac += 1
        if column == x:
            for i in letters[sayac:]:
                sayac1 += 1
                if int(y) - sayac1 < 1:
                    break
                a.append(i + str(int(y) - sayac1))
            for k in letters[:sayac - 1][::-1]:
                sayac2 += 1
                if int(y) - sayac2 < 1:
                    break
                b.append(k + str(int(y) - sayac2))
    return [a, b]
def Bishop_showmoves(bishop):
    Bishop_moves = []
    a, b = Bishop_possibility(bishop)
    for i in a:
        if board[map.index(i)] == "  ":
            Bishop_moves.append(i)
        elif color_of_rack(board[map.index(i)]) == False and board[map.index(i)] not in ["ki", "KI"]:
            Bishop_moves.append(i)
            break
        else:
            break
    for i in b:
        if board[map.index(i)] == "  ":
            Bishop_moves.append(i)
        elif color_of_rack(board[map.index(i)]) == False and board[map.index(i)] not in ["ki", "KI"]:
            Bishop_moves.append(i)
            break
        else:
            break
    return Bishop_moves
def queen_possibilty(queen):
    liste1 = [Bishop_possibility(queen) + bishop_possibility(queen)]
    return [liste1, rook_possibility(queen)]
def queen_showmoves(queen):
    queen_moves = []
    for k in queen_possibilty(queen)[0]:
        for m in k:
            for i in m:
                if board[map.index(i)] == "  ":
                    queen_moves.append(i)
                elif color_of_rack(board[map.index(i)]) != color_of_rack(queen) and board[map.index(i)] not in ["ki","KI"]:
                    queen_moves.append(i)
                    break
                else:
                    break
    x = queen_possibilty(queen)[1][0]
    a = x[:x.index(map[board.index(queen)])]
    b = x[x.index(map[board.index(queen)]) + 1:x.index("|")]
    e = x[x.index("|"):]
    c = e[1:e.index(map[board.index(queen)])]
    d = e[e.index(map[board.index(queen)]) + 1:]
    for k in [a[::-1], b, c[::-1], d]:
        for i in k:
            if board[map.index(i)] == "  ":
                queen_moves.append(i)
            elif color_of_rack(board[map.index(i)]) != color_of_rack(queen) and board[map.index(i)] not in ["ki", "KI"]:
                queen_moves.append(i)
                break
            else:
                break
    return queen_moves
def pawn_possibility(pawn):
    pawn_possib = []
    if map[board.index(pawn)][1] != "8":
        pawn_possib.append(map[board.index(pawn) - 8])
    return pawn_possib
def pawn_showmoves(pawn):
    pawn_moves = []
    for aim in pawn_possibility(pawn):
        if board[map.index(aim)] == "  ":
            pawn_moves.append(aim)
        elif color_of_rack(board[map.index(aim)]) == True and board[map.index(aim)] not in ["ki", "KI"]:
            pawn_moves.append(aim)
    return pawn_moves
def Pawn_possibility(pawn):
    Pawn_possib = []
    if map[board.index(pawn)][1] != "1":
        Pawn_possib.append(map[board.index(pawn) + 8])
    return Pawn_possib
def Pawn_showmoves(pawn):
    Pawn_moves = []
    for aim in Pawn_possibility(pawn):
        if board[map.index(aim)] == "  ":
            Pawn_moves.append(aim)
        elif color_of_rack(board[map.index(aim)]) == False and board[map.index(aim)] not in ["ki", "KI"]:
            Pawn_moves.append(aim)
    return Pawn_moves
def knight_possibility(knight):
    liste1, liste2, x, y = [], [], map[board.index(knight)][0], map[board.index(knight)][1]
    for i in letters:
        if (letters.index(i) - letters.index(x) < 3 and letters.index(i) - letters.index(x) >= 0) or (letters.index(x) - letters.index(i) < 3 and letters.index(x) - letters.index(i) >= 0):
            for k in range(1, 9):
                if (k - int(y) < 3 and k - int(y) >= 0) or (int(y) - k < 3 and int(y) - k >= 0):
                    liste1.append(i + str(k))
    liste1.remove(x + y)
    liste = Bishop_possibility(knight)
    liste.extend(bishop_possibility(knight))
    liste.extend(rook_possibility(knight))
    for b in liste:
        for c in b:
            if c in liste1:
                liste1.remove(c)
    if map[board.index(knight)][0] != "a" and map[board.index(knight)][1] != "8":
        liste2.append(map[board.index(knight) - 9])
    if map[board.index(knight)][0] != "h" and map[board.index(knight)][1] != "8":
        liste2.append(map[board.index(knight) - 7])
    if map[board.index(knight)][0] != "a" and map[board.index(knight)][1] != "1":
        liste2.append(map[board.index(knight) + 7])
    if map[board.index(knight)][0] != "h" and map[board.index(knight)][1] != "1":
        liste2.append(map[board.index(knight) + 9])
    return [liste1, liste2]
def knight_showmoves(knight):
    knight_moves = []
    for i in knight_possibility(knight)[0]:
        if board[map.index(i)] == "  ":
            knight_moves.append(i)
        elif color_of_rack(board[map.index(i)]) != color_of_rack(knight) and board[map.index(i)] not in ["ki", "KI"]:
            knight_moves.append(i)
    for i in knight_possibility(knight)[1]:
        if board[map.index(i)] == "  " and board[map.index(i)] not in ["ki", "KI"]:
            knight_moves.append(i)
    return knight_moves
for command in commands:
    print(">", end=" ")
    print(*command)
    if command[0] == "initialize":
        print("-" * 23)
        a = 1
        for i in board1:
            print(i, end=" ")
            if a % 8 == 0:
                print()
            a += 1
        print("-" * 23)
        board = board1
    elif command[0] == "print":
        b = 1
        print("-" * 23)
        for i in board:
            print(i, end=" ")
            if b % 8 == 0:
                print()
            b += 1
        print("-" * 23)
    elif command[0] == "exit":
        exit()
    elif command[0] == "showmoves":
        if command[1] in ["KI", "ki"]:
            if king_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*sorted(king_showmoves(command[1])))
        elif command[1] in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
            if Pawn_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*Pawn_showmoves(command[1]))
        elif command[1] in ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]:
            if pawn_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*pawn_showmoves(command[1]))
        elif command[1] in ["R1", "R2", "r1", "r2"]:
            if rook_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*sorted(rook_showmoves(command[1])))
        elif command[1] in ["b1", "b2"]:
            if bishop_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*sorted(bishop_showmoves(command[1])))
        elif command[1] in ["B1", "B2"]:
            if Bishop_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*sorted(Bishop_showmoves(command[1])))
        elif command[1] in ["qu", "QU"]:
            if queen_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*sorted(queen_showmoves(command[1])))
        elif command[1] in ["n1", "n2", "N1", "N2"]:
            if knight_showmoves(command[1]) == []:
                print("FAILED")
            else:
                print(*sorted(knight_showmoves(command[1])))
    elif command[0] == "move":
        if command[2] in showmovess(command[1]):
            print("OK")
            board[board.index(command[1])] = "  "
            board[map.index(command[2])] = command[1]
        else:
            print("FAILED")