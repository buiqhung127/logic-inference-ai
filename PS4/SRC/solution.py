def PL_Resolve(C_1, C_2): # handle example case
    res = -1 
    C1 = C_1.split(';')
    C2 = C_2.split(';')
    # print('Initial ', C1, C2)
    for index, e1 in enumerate(C1): 
        for e2 in C2: # generalize here later
            if (e1[0] == '-' and e1[1] == e2[0]) or (e2[0] == '-' and e2[1] == e1[0]): 
                res = index 
                break 

    if res != -1:
        C1.pop(res)   
    C_1 = ';'.join(C1)


    return C_1
        
def PL_Add_Alpha(clauses_set, alpha): 
    neg_alpha = alpha
    if alpha[0] != '-':
        neg_alpha = '-' + alpha    
    else:
        neg_alpha = neg_alpha[1]
    clauses_set.add(neg_alpha)

def filter_redundant(clauses_set):
    tempo = set([])
    for element in clauses_set:
        ele = element.split(';')
        for e1 in ele:
            for e2 in ele: # generalize here later
                if (e1[0] == '-' and e1[1] == e2[0]) or (e2[0] == '-' and e2[1] == e1[0]): 
                    tempo.update({element}) 
    for temp in tempo:
        clauses_set.remove(temp)
    return clauses_set

def PL_Resolution(KB, alpha, logs):
    clauses_set = set(KB)
    PL_Add_Alpha(clauses_set, alpha)

    filter_redundant(clauses_set)


    new = set([])
    while True: 
        cnt = 0
        tempo = [] 
        check = False
        for index, C1 in enumerate(clauses_set):
            for C2 in clauses_set: 
                if C1 == C2 or len(C2) >= 3:
                    continue
                if len(C1) < len(C2):
                    C1, C2 = C2, C1 
                resolvents = PL_Resolve(C1, C2) 

                temporary_set = set([resolvents])
                if (not temporary_set.issubset(new)) and (not temporary_set.issubset(clauses_set)):
                    cnt += 1
                    tempo.append(resolvents)
                    print(temporary_set,', results from ', C1, ' and ', C2)
                if len(resolvents) == 0: 
                    # logs.append(cnt)
                    # logs.append(tempo)   
                    check = True 
                    # return True 
                
                new = new.union(temporary_set)
        logs.append(cnt)
        logs.append(tempo)        
        if check: # check the inferencing condition at the end of loops 
            return True 
        if new.issubset(clauses_set):
            return False 
        clauses_set.update(new)
        # print('clauses: ', clauses_set)
    
    return False