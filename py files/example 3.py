import random
import math
import matplotlib.pyplot as plt


def monte_carlo(runs, needles, n_length, b_width):
    pi_values = []

    plt.axhline(y=math.pi, color='r', linestyle='-')

    for i in range(runs):
        # Initialize number of hits/intersections as 0.
        n_hits = 0

        # For all needles :
        for j in range(needles):
            # We will find the distance from the nearest vertical line :
            # Min = 0     Max = b_width/2
            x = random.uniform(0, b_width / 2.0)

            # The theta value will be from 0 to pi/2 :
            theta = random.uniform(0, math.pi / 2)

            # Checking if the needle crosses the line or not :
            xtip = x - (n_length / 2.0) * math.cos(theta)
            if xtip < 0:
                n_hits += 1

        # Going with the formula :
        numerator = 2.0 * n_length * needles
        denominator = b_width * n_hits

        # Append the final value of pi :
        pi_values.append((numerator / denominator))

    # Final pi value after all iterations :
    print(pi_values[-1])

    plt.plot(pi_values)
    plt.show()


# Total number of runs :
runs = 500

# Total number of needles :
needles = 50

# Length of needle :
n_length = 2

# space between 2 vertical lines :
b_width = 2

monte_carlo(runs, needles, n_length, b_width)
