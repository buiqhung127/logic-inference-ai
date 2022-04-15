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

def PL_Resolution(KB, alpha, logs):
    clauses_set = set(KB)
    PL_Add_Alpha(clauses_set, alpha)
    new = set([])
    while True: 
        cnt = 0
        tempo = [] 
        for index, C1 in enumerate(clauses_set):

            for C2 in clauses_set: 
                if C1 == C2 or len(C2) >= 3:
                    continue
                if len(C1) < len(C2):
                    C1, C2 = C2, C1 
                resolvents = PL_Resolve(C1, C2) 

                temporary_set = set([resolvents])
                if not temporary_set.issubset(new):
                    cnt += 1
                    tempo.append(resolvents)
                    print(temporary_set)
                if len(resolvents) == 0: 
                    logs.append(cnt)
                    logs.append(tempo)   
                    return True 
                


                new = new.union(temporary_set)
        logs.append(cnt)
        logs.append(tempo)        
        
        if new.issubset(clauses_set):
            return False 
        clauses_set.update(new)
        print('clauses: ', clauses_set)
    
    return False