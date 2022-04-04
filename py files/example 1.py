import random
import numpy as np
import matplotlib.pyplot as plt


def coin_flip():
    return random.randint(0, 1)


def monte_carlo(n):
    results = 0
    list_of_probabilities = []

    for i in range(n):
        flip_result = coin_flip()
        results = results + flip_result
        probability_value = results / (i + 1)
        list_of_probabilities.append(probability_value)

    plt.axhline(y=0.5, color='r', linestyle='-')
    plt.xlabel("Iterations")
    plt.ylabel("Probability")
    plt.plot(list_of_probabilities)
    plt.show()

    return results / n


answer = monte_carlo(100000)
print("Final value :", answer)
