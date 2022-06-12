from matrix import Matrix

matrixA = Matrix(2,2)

print("")
matrixA.add(0,0,1)
matrixA.add(0,1,2)
matrixA.add(1,0,3)
matrixA.add(1,1,4)


matrixA = matrixA * 3
matrixA = matrixA * 0.5
print("aqui va")

print(matrixA)

for i in matrixA:
    print(i)

