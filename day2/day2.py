def isSafe(report):
    inc = 0
    dec = 0
    for i in range(len(report)-1) :
        #increasing
        if int(report[i+1]) > int(report[i]):
            if int(report[i+1]) - int(report[i]) <= 3:
                inc += 1
            else:
                return 0
        #decreasing
        elif int(report[i+1]) < int(report[i]):
            if int(report[i]) - int(report[i+1]) <= 3:
                dec += 1
            else:
                return 0
        else:
            return 0
    if inc > 0 and dec == 0 or dec > 0 and inc == 0 :
        return 1
    else:
        return 0
        
with open('input.txt') as input:
    reports = [row.replace('\n','').split(" ") for row in input]
    print(len(reports))
    safe = 0
    for report in reports:
        safe += isSafe(report)

    print(safe)

    rereports = []
    for report in reports:
        rereport = []
        rereport.append(report)
        for level,value in enumerate(report):
            rerereport = report.copy()
            rerereport.pop(level)
            rereport.append(rerereport)
        rereports.append(rereport)

    q2safe = 0
    for x in rereports:
        safe_after_remove = []
        for y in x:
            safe_after_remove.append(isSafe(y))
        if any(safe_after_remove):
            q2safe +=1
    print(q2safe)

            