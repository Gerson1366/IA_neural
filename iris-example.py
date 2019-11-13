from learning import *

iris = DataSet(name="poker-hand-training-true")
iris.classes_to_numbers()
print(iris)
nNL = NeuralNetLearner(iris)
print("Esperado: 0")
print(nNL([1,1,1,13,2,4,2,3,1,12]))
print("Esperado: 1")
print(nNL([4,2,4,12,2,12,2,7,3,10]))
print("Esperado: 3")
print(nNL([2,12,1,12,2,9,2,13,4,12]))
print("Esperado: 5")
print(nNL([1,13,1,8,1,1,1,4,1,11]))