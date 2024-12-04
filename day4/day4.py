def xmasChecker(input,row,col):
    counts = 0
    if input[row][0][col] == "X":
        #forwards
        if col <= len(input[row][0]) -1 - 3:
            if input[row][0][col+1] == "M":
                if input[row][0][col+2] == "A":
                    if input[row][0][col+3] == "S":
                        counts += 1
        #backwards
        if col >= 3:
            if input[row][0][col-1] == "M":
                if input[row][0][col-2] == "A":
                    if input[row][0][col-3] == "S":
                        counts += 1
        #upwards
        if row >= 3:
            if input[row-1][0][col] == "M":
                if input[row-2][0][col] == "A":
                    if input[row-3][0][col] == "S":
                        counts += 1
        #downwards
        if row <= len(input) -1 - 3:
            if input[row+1][0][col] == "M":
                if input[row+2][0][col] == "A":
                    if input[row+3][0][col] == "S":
                        counts += 1
        #upleft
        if row >= 3 and col >= 3:
            if input[row-1][0][col-1] == "M":
                if input[row-2][0][col-2] == "A":
                    if input[row-3][0][col-3] == "S":
                        counts += 1
        #upright
        if row >= 3 and col <= len(input[row][0]) -1 - 3:
            if input[row-1][0][col+1] == "M":
                if input[row-2][0][col+2] == "A":
                    if input[row-3][0][col+3] == "S":
                        counts += 1
        #downleft
        if row <= len(input) -1 - 3 and col >= 3:
            if input[row+1][0][col-1] == "M":
                if input[row+2][0][col-2] == "A":
                    if input[row+3][0][col-3] == "S":
                        counts += 1
        #downright
        if row <= len(input) -1 - 3 and col <= len(input[row][0]) -1 - 3:
            if input[row+1][0][col+1] == "M":
                if input[row+2][0][col+2] == "A":
                    if input[row+3][0][col+3] == "S":
                        counts += 1
    return counts

def x_masChecker(input,row,col):
    counts = 0
    if input[row][0][col] == "A":
        if (row >= 1 and col >= 1) and (row <= len(input) -1 - 1 and col <= len(input[row][0]) -1 - 1):
            #upleft to downright
            if (input[row-1][0][col-1] == "M" and input[row+1][0][col+1] == "S") or (input[row-1][0][col-1] == "S" and input[row+1][0][col+1] == "M"):
                #downleft to upright
                if (input[row+1][0][col-1] == "M" and input[row-1][0][col+1] == "S") or (input[row+1][0][col-1] == "S" and input[row-1][0][col+1] == "M"):
                    counts += 1
    return counts

with open('input.txt') as input:
    input_array = [row.replace('\n','').split(" ") for row in input]

    q1xmas = 0
    q2xmas = 0
    for row in range(len(input_array)):
        for col in range(len(input_array[row][0])):
            xmas = xmasChecker(input_array,row,col)
            q1xmas += xmas
            x_mas = x_masChecker(input_array,row,col)
            q2xmas += x_mas

    print(q1xmas)
    print(q2xmas)
