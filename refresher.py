from matplotlib import pyplot as plt

import numpy as np


if __name__ == '__main__':
    # First, generate the sine and cosine series for one period [0, 2*PI]
    x = np.linspace(0, 2 * np.pi, 1001)
    sin2 = np.sin(x)
    cos2 = np.cos(x)
    tan2 = np.tan(x)

    tan2[tan2 > 3] = np.inf
    tan2[tan2 < -3] = np.inf

    # Then, plot both series on the same axis
    plt.plot(x, sin2, 'r-', label='sin')
    plt.plot(x, cos2, 'b-', label='cos')
    plt.plot(x, tan2, 'g-', label='tan')
    plt.xticks([0, np.pi/2, np.pi, (3*np.pi)/2, 2*np.pi], ['0', 'pi/2', 'pi', '3pi/2', '2pi'])
    plt.xlabel('Angle (in radians)')
    plt.ylabel('Value')
    plt.title('Sine, cosine, and tan over one period')
    plt.legend(loc=3)
    plt.ylim(-3, 3)
    plt.xlim(0, 2 * np.pi)
    plt.show()
