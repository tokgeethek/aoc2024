from collections import Counter

with open('input.csv') as input:
    first_array, second_array, distance_array = [], [] , []
    
    for row in input:
        values = row.replace('\n','').split(" ")
        first_array.append(values[0])
        second_array.append(values[-1])

    sorted_first_array = sorted(first_array)
    sorted_second_array = sorted(second_array)

    for i in range(len(sorted_first_array)):
        distance = abs(int(sorted_first_array[i]) - int(sorted_second_array[i]))
        distance_array.append(distance)

    #Ans 1
    print(sum(distance_array))

    similarity_score_array = []
    right_list_counts = Counter(sorted_second_array)
    for location in sorted_first_array:
        try: 
            similarity_score_array.append(int(right_list_counts[location])*int(location))
        except:
            continue
    
    #Ans 2
    print(sum(similarity_score_array))
    