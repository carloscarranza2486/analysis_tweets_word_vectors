def vectortes_unitarios(n):
    vector_u = []
    for i in range(n):
        array = np.zeros(n)
        array[i] = 1
        vector_u.append(array)
    return vector_u

vectores_unitarios(4)
print(vectortes_unitarios)