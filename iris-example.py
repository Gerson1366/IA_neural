from learning import *
import csv
import time



start = time.time()
learning_rate = 0.01
hidden_layer = [30]
epochs = 5000
iris = DataSet(name="balance-scale")
iris.classes_to_numbers()
print(iris)
nNL = NeuralNetLearner(iris,hidden_layer,learning_rate,epochs)
right = 0
total = 0
with open('./aima-data/balance-test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        total = total+1
        if(row[4]=='B'):
            resul = 0
        elif(row[4]=='L'):
            resul = 1
        elif(row[4]=='R'):
            resul = 2
        teste = nNL([int(row[0]),int(row[1]),int(row[2]),int(row[3])])
        if(teste==resul):
            right = right+1
acertos = (right/total)*100
end = time.time()
elapsed = end - start

print('')
print('Taxa Aprendizado: ' ,learning_rate)
print('Numero de vezes que o algoritmo passa pelo dataset: ' ,epochs)
print('Tamanho das camadas escondidas: ' ,hidden_layer)
print('')
print('Tempo: ' ,elapsed, 'segundos')
print('Taxa de acerto: ',acertos,'%')



