import random
import matplotlib.pyplot as plt
import matplotlib
from gensim.models import KeyedVectors
from main import dimensional_compression

matplotlib.rcParams['font.family'] = 'MS Gothic'
WV = KeyedVectors.load_word2vec_format('./wiki.model', binary=True)

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

def tournament_compression(variables: list[int]) -> int:
    while len(variables) > 1:
        next_round = []
        for i in range(0, len(variables) - 1, 2):
            winner = dimensional_compression(variables[i], variables[i + 1])
            next_round.append(winner)
        if len(variables) % 2 == 1:
            next_round.append(variables[-1])
        variables = next_round
    return variables[0]

def word2vec_and_compression(word: str) -> tuple[int, int]:
    vs = [int((v + 10) * 10) for v in WV[word]]
    return (tournament_compression(vs[:len(vs) // 2]), tournament_compression(vs[len(vs) // 2:]))

def sample3():
    ziped_locations = (
                       word2vec_and_compression("コンピューター"),
                       word2vec_and_compression("パソコン"),
                       word2vec_and_compression("カメラ"),
                       word2vec_and_compression("電車"),
                       )
    xs = [x for (x, _) in ziped_locations]
    ys = [y for (_, y) in ziped_locations]
    plt.scatter(xs, ys)
    for i, k in enumerate(("コンピューター", "パソコン", "カメラ", "電車")):
        plt.annotate(k, ziped_locations[i])
    plt.show()
