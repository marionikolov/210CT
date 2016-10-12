m1 = {(2,2): 1, (3,1): 2}
m2 = {(1,1): 1, (3,1): 3}

m1a = {(1,1): 4, (1,3): 1, (2,2): 1}
m2a = {(1,1): 1, (2,2): 2}
m1aDim = (2, 3)
m2aDim = (3, 2)

def addMatrices(m1, m2):
    m3 = {}
    for key in m1:
        if key in m2:
            m3[key] = m1[key] + m2[key]
        elif key not in m2:
            m3[key] = m1[key]
    for key in m2:
        if key in m1:
            pass
        elif key not in m1:
            m3[key] = m2[key]
    return m3

def substractMatrices(m1, m2):
    m3 = {}
    for key in m1:
        if key in m2:
            m3[key] = m1[key] - m2[key]
        elif key not in m2:
            m3[key] = -m1[key]
    for key in m2:
        if key in m1:
            pass
        elif key not in m1:
            m3[key] = -m2[key]
    return m3

def multiplyMatrices(m1a, m2a, m1aDim, m2aDim):
    if m1aDim[1] != m2aDim[0]:
        print("Error. Cannot multiply due to...")
    else:
        m3a = {}
        for j in range (1, m1aDim[0] + 1): # 2 rows in first matrix = rows in new matrix
            for i in range(1,m2aDim[1] + 1): # 2 cols in second matrix = cols in new matrix
                for k in range (1, m1aDim[1] + 1): # 3 cols in first matrix
                    if (j,k) in m1a and (k,i) in m2a:
                        if (j,i) not in m3a:
                            m3a[(j,i)] = 0
                        m3a[(j, i)] += m1a[(j,k)]*m2a[(k,i)]
        return m3a

m3 = addMatrices(m1, m2)
m4 = substractMatrices(m1, m2)
print(m3)
print(m4)

m5 = multiplyMatrices(m1a, m2a, m1aDim, m2aDim)
print(m5)