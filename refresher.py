from matplotlib import pyplot as plt

import numpy as np


if __name__ == '__main__':
    # First, generate the sine and cosine series for one period [0, 2*PI]
    x = np.linspace(0, 2 * np.pi, 1001)
    sin2 = np.sin(x)
    cos2 = np.cos(x)

    # Then, plot both series on the same axis
    plt.plot(x, sin2)
    plt.plot(x, cos2)
    plt.xticks([0, np.pi/2, np.pi, (3*np.pi)/2, 2*np.pi], ['0', 'pi/2', 'pi', '3pi/2', '2pi'])
    plt.show()