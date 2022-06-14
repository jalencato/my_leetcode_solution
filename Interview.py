# import matplotlib.pyplot as plt
# import numpy as np
#
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# # x = np.linspace(0, 10)
# x = np.array([32, 64, 96, 128, 160, 192, 224, 256, 320, 352, 384, 416, 448, 480, 512, 544
#                  , 576, 608, 640, 672, 704, 736, 768, 800, 832, 864, 896, 928, 960,
#               992, 1024])
# y_416 = np.array([1.13, 5.23, 8.24, 10.2, 10, 10.8, 11.2, 11.5, 11.7, 11.9, 12.1, 12.9, 11.9, 12.1, 11.7, 12.2
#                  , 12.1, 11.9, 11.7, 12.1, 12.3, 12.1, 11.7, 12.1, 11.7, 12.3, 12.1, 11.9, 12.1,
#               12.1, 11.7])
# y_412 = np.array([1.14, 6.29, 12.9, 16.9, 15.8, 18.3, 20.7, 21.4, 21, 22.9, 23.6, 22.7, 23.3, 23.9, 23.8,23.6
#                  , 23.7, 24.1, 24.1, 23.6, 23.9, 24.2, 24.1, 23.9, 22.7, 24.5, 24.4, 24.3, 24.3,
#               24.4, 22.8])
# y_48 = np.array([1.16, 6.42, 12.7, 16.8, 15.8, 18.3, 20.1, 21, 21.7, 22.4, 22.9, 22.5, 22.7, 23.3, 23, 23
#                  , 23.3, 23.4, 23.9, 23.3, 23.4, 23.5, 23.7, 23.2, 23.5, 23.9, 23.9, 23.6, 23.8,
#               24.1, 23.8])
# y_naive = np.array([2.5645, 2.16, 1.9, 1.7, 1.89, 1.67, 1.78, 1.93, 1.87, 1.64, 1.76, 1.74, 1.58, 1.76, 0.88, 1.69
#                  , 1.75, 1.69, 1.71, 1.67, 1.56, 1.47, 1.52, 1.37, 1.27, 1.34, 1.28, 1.15, 1.17,
#               1.19, 0.14])
# y_blas = np.array([17.185, 24.01, 26.45, 28.62, 29.14, 30.23, 31.23, 32.445, 32.435, 32.98, 33.41, 33.67, 33.17, 33.78, 34.21, 34.56
#                  , 34.6, 34.8, 35.1, 34.6, 35.34, 35.45, 35.67, 35.78, 35.43, 35.17, 35.5, 35.674, 34.9,
#               35.1, 34.965])
# with plt.style.context('Solarize_Light2'):
#     plt.plot(x, y_416, label = "4*16 microkernel")
#     plt.plot(x, y_412, label = "4*12 microkernel")
#     plt.plot(x, y_48, label="4*8 microkernel")
#     plt.plot(x, y_naive, label = "naive")
#     plt.plot(x, y_blas, label="blas")
#     # Number of accent colors in the color scheme
#     plt.title('AVX256 -- Overall Performance')
#     plt.xlabel('Matrix Size', fontsize=14)
#     plt.ylabel('Performance(GFLOPS)', fontsize=14)
#     plt.legend()
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.array([128, 192, 256, 384])
# y_824 = np.array([0.82, 8.17, 19.2, 32.1, 33.3, 35.3, 31.7, 41.2, 43.4, 40, 42, 37.3, 40.3, 44.3, 38.5, 39.7, 39.3])
# y_816 = np.array([1.21, 8.17, 18.7, 30, 30.2, 32.5, 34.7, 33.8, 36.7, 35.7, 34.8, 35.4, 36.2, 34.6, 40.5, 34.4, 34.2])
# y_88 = np.array([1.07, 7.96, 19.7, 34.7, 33.7, 37.5, 40.3, 37.2, 40.8, 41.9, 41.9, 41.3, 42.4, 36.2, 41.4, 41.8, 42.2])
y_n1 = np.array([1084, 1585, 2176, 3079])
y_n2 = np.array([142.5, 303.1, 536.8, 1606])
with plt.style.context('Solarize_Light2'):
    # plt.plot(x, y_824, label ="8*24 microkernel")
    # plt.plot(x, y_816, label ="8*16 microkernel")
    # plt.plot(x, y_88, label="8*8 microkernel")
    plt.plot(x, y_n1, label = "GFlops on N1")
    plt.plot(x, y_n2, label="GFlops on N2")
    # Number of accent colors in the color scheme
    plt.title('Strong and Weak Scaling')
    plt.xlabel('Matrix Size', fontsize=14)
    plt.ylabel('Performance(GFLOPS)', fontsize=14)
    plt.legend()

plt.show()