from matrix import Matrix

matrixA = Matrix(2,2)

matrixA.get()
print("")
matrixA.add(0,0,1)
matrixA.add(0,1,2)
matrixA.add(1,0,3)
matrixA.add(1,1,4)

matrixA.get()
matrixB = matrixA * 3

print("aqui va")
matrixB.get()
matrixA.get()

print(matrixA)

