map = input("Please enter feeding map as a list:")
direction = input("Please enter direction of movements as a list: ")
print("Your board is:")
score , number_of_line = 0 , 0
board,location = [],[]
for j in map.split("],"):
    k = 0
    for i in j:
        if i in ["W","A","C","P","*","X","M"]:  # I want to clear something like--> , ' [ ]
            board.append(i)
            print(i, end=" ")  # it is for printing 2D
            k += 1
        if i == "*":
            location = [(map.split("],")).index(j)] # I have found location of * . location is a list which has 2 index
            location.append(k)
    print()
    number_of_line += 1  # I have found how many line
number_of_column = int(len(board) / number_of_line)  # I have found how many clomn
superman = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
board.extend(superman)

def feeding(destination):  # this function for collect points
    global score
    if destination == "C":
        score += 10
    elif destination == "A":
        score += 5
    elif destination == "M":
        score -= 5
    return score

for move in direction:
    if move == "R":
        right = board[(location[0] * number_of_column) + location[1]]
        if location[1] != number_of_column and right != "W":       # "right" is the char which to the right of the star
            feeding(right)
            if right == "P":
                location[1] = location[1] + 1
                break
            location[1] = location[1] + 1
    elif move == "L":
        left = board[(location[0] * number_of_column) + location[1] - 2]
        if location[1] != 1 and left != "W":     # "left" is the char which to the left of the star
            feeding(left)
            if left == "P":
                location[1] = location[1] - 1
                break
            location[1] = location[1] - 1
    elif move == "U":
        up = board[(location[0] - 1) * number_of_column + location[1] - 1]
        if location[0] != 0 and up != "W":         # "up" is the char which to the above of the star
            feeding(up)
            if up == "P":
                location[0] = location[0] - 1
                break
            location[0] = location[0] - 1
    elif move == "D":
        down = board[(location[0] + 1) * number_of_column + location[1] - 1]
        if location[0] != (number_of_line - 1) and down != "W":  #"down" is the char which to the down of the star
            feeding(down)
            if down == "P":
                location[0] = location[0] + 1
                break
            location[0] = location[0] + 1
print("Your output should be like this: ")
board[board.index("*")] = "X"                              # I put a "X" instead of star
board[location[0] * number_of_column + location[1] - 1] = "*"  # I have changed the location of star.
a = 1
for x in board:
    if x != " ":
        print(x, end=" ")
        if a % number_of_column == 0:  # I wanted to push enter when x should be end of line
            print()
    a += 1
print("Your score:", score)