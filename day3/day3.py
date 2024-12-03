with open('input.txt') as file:
    input = file.read()
    sum = 0
    for i in range(1000):
        for j in range(1000):
            if f'mul({i},{j})' in input:
                sum += i*j

    print(sum)

    removedont = input.split("don't()")
    pt2input = [removedont[0]]
    for section in removedont[1:]:
        if "do()" in section:
            pt2input.append("".join(section.split("do()")[1:]))

    pt2sum = 0
    for do in pt2input:
        for i in range(1000):
            for j in range(1000):
                if f'mul({i},{j})' in do:
                    pt2sum += i*j
    print(pt2sum)

