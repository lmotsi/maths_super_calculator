def mode(data_list):
    pairs = dict()
    for i in data_list:
        if i not in pairs.keys():
            pairs[i] = 1;
        else:
            pairs[i] = pairs[i] + 1
    
    high = data_list[0]
    for i in pairs.keys():
        if pairs[i] > pairs[high]:
            high = i
            
    return high

def mean(data_list):
    sum = 0;
    count = 0;
    for i in data_list:
        sum += i
        count += 1
    return sum/count

def median(data_list):
    half = len(data_list)/2
    return data_list[half]
      