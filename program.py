def pack_bagpack(scores, weights, capacity): #Ranking 5th in codewars solution
    table = []
    for row in range(len(scores)+1):
        temp_rows = []
        for column in range(capacity+1):
            if row == 0:
                temp_rows.append(0)
            else:
                if weights[row-1] > column:
                    temp_rows.append(table[row-1][column])
                else:
                    value = max(table[row-1][column], scores[row-1]+table[row-1][column - weights[row-1]])
                    temp_rows.append(value)
        table.append(temp_rows)
    max_value = table[-1][-1]
    return max_value

#dude on the top
def pack_bagpack(scores, weights, capacity):
    load = [0] * (capacity + 1)
    for score, weight in zip(scores, weights):
        load = [max(l, weight <= w and load[w - weight] + score)
                for w, l in enumerate(load)]
    return load[-1]