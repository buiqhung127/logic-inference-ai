def eliminated(e1, e2):
    pass 
def PL_Resolve(C_1, C_2): # handle example case
    res = -1 
    C1 = C_1.split(';')
    C2 = C_2.split(';')
    for index, e1 in enumerate(C1): 
        for e2 in C2: # generalize here later
            if (e1[0] == '-' and e1[1] == e2[0]) or (e2[0] == '-' and e2[1] == e2[0]): 
                res = index 
                break 
    if res != -1:
        C1.pop(res)   
    return C1 
        
def PL_Add_Alpha(clauses_set, alpha): 
    neg_alpha = alpha
    if alpha[0] != '-':
        neg_alpha = '-' + alpha    
    clauses_set.add(neg_alpha)

def PL_Resolution(KB, alpha):
    clauses_set = set(KB)
    PL_Add_Alpha(clauses_set, alpha)
    new = set([])
    # print(clauses_set)
    while True: 
        for index, C1 in enumerate(clauses_set):
            print(index) 
            for C2 in clauses_set: 
                # print(C1 + '      '  + C2)
                if C1 == C2 or len(C2) >= 3:
                    continue
                if len(C2) >= len(C1):
                    C1, C2 = C2, C1 
                resolvents = PL_Resolve(C1, C2) 
                if len(resolvents) == 0: 
                    return True 
                new = new.union(resolvents)
        
        if new.issubset(clauses_set):
            return False 
        clauses_set.update(new)
    
    return False