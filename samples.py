import random
import matplotlib.pyplot as plt
from main import dimensional_compression

def sample1():
    n = 100
    xs, ys = [i for i in range(1, n + 1)], [i for i in range(1, n + 1)]
    random.shuffle(xs)
    random.shuffle(ys)
    for x, y in zip(xs, ys):
        print(dimensional_compression(x, y))
        
def sample2():
    n = 100
    xs, ys = [i for i in range(1, n + 1)], [i for i in range(1, n + 1)]
    compresseds = [dimensional_compression(x, y) for x, y in zip(xs, ys)]
    plt.scatter(xs, compresseds)
    plt.show()
