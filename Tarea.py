from math import floor
from flask import Flask
from random import randint

app = Flask(__name__)

def lineal(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary(arr, x):

    n = len(arr)
    L = 0
    R = n-1

    while L <= R:
        mid = floor((L+R)/2)
        if arr[mid] < x:
            L = mid + 1
        elif arr[mid] > x:
            R = mid - 1
        else:
            return mid
    return -1

@app.route('/lineal/<int:numero>/<int:buscador>', methods=['GET'])
def lin(numero, buscador):
    a = []
    count = 0

    while (count <= numero):
        a.append(randint(1,50))
        count += 1
    a.sort()

    LS = lineal(a, buscador)
    if LS == -1:
        print("El numero no esta en la lista")
        return "False"
    else:
        print("El numero está en el puesto: " + str(LS))
        return "True"

@app.route('/binario/<int:numero>/<int:buscador>', methods=['GET'])
def bin(numero, buscador):
    b = []
    count = 0

    while (count <= numero):
        b.append(randint(1,50))
        count += 1
    b.sort()

    BS = binary(b, buscador)
    if BS == -1:
        print("El numero no esta en la lista")
        return "False"
    else:
        print("El numero está en el puesto: " + str(BS))
        return "True"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)