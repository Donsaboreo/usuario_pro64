import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, feature, measure
from scipy.optimize import curve_fit

def ellipse(x, a, b, h, k):
    return k + np.sqrt(1 - ((x - h) / a) ** 2) * b

def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c

def detect_curves(image_path):
    # Leer la imagen en escala de grises
    image = color.rgb2gray(cv2.imread(image_path))

    # Realizar detección de bordes con el operador Canny
    edges = feature.canny(image, sigma=2.0, low_threshold=0.55, high_threshold=0.8)

    # Detección de elipses utilizando la transformada de Hough
    ellipses = measure.find_contours(edges, 0.8)

    # Ajuste de curva para parábola
    x_points = np.arange(len(edges[0]))
    y_points = np.argmax(edges, axis=0)

    try:
        params, covariance = curve_fit(parabola, x_points, y_points)
        a, b, c = params
        parabola_fit = parabola(x_points, a, b, c)

        # Mostrar la imagen original y las curvas detectadas
        fig, ax = plt.subplots()
        ax.imshow(image, cmap=plt.cm.gray)

        for ellipse in ellipses:
            ax.plot(ellipse[:, 1], ellipse[:, 0], '-r', linewidth=2)

        ax.plot(x_points, parabola_fit, label='Parabola Fit', color='blue')
        ax.legend()
        plt.show()

    except Exception as e:
        print(f"Error al ajustar la parábola: {e}")

if __name__ == "__main__":
    image_path = 'ruta_de_tu_imagen.jpg'  # Reemplaza con la ruta de tu imagen
    detect_curves(image_path)
    