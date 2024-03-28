from PIL import Image
import numpy as np
from fourier import *
import matplotlib.pyplot as plt

THRESHOLD = 100

def cast_image_into_y_coordinates(image):
    image_size = len(image)
    y = []
    for col in range(len(image[0])): 
        has_a_value = False
        for row in range(len(image)):
            if image[row][col] < THRESHOLD:
                y.append(image_size - (row + 1))
                has_a_value = True
                break
                
        if not has_a_value:
            print(f"Warning: THERE ARE ENTIRE ROWS THAT HAS NO BLACK SPOT")
            y.append(0)
    
    return np.array(y) 

def export_to_file(path_to_file, a_n, b_n, a_o):
    with open(path_to_file, 'w') as f: 
        f.write(f"{a_o}\n")
        for i in range(len(a_n)):
            if i == len(a_n) - 1:
                f.write(f"{a_n[i]}|{b_n[i]}")
            else:
                f.write(f"{a_n[i]}|{b_n[i]}\n")


def create_sine_cosine_graph(a_n, b_n, a_o, period):
    x = np.linspace(0, period, 1000)
    y = []
    for i in range(len(x)):
        y.append(compute_one_value_at_x(a_n, b_n, a_o, period, x[i]))

    return x, y

if __name__ == "__main__":
    filename = input("filename?")
    sine_cosine_count = int(input("number of sin waves?"))
    image = Image.open(filename).convert("L")
    image = np.array(image)

    
    image_y = cast_image_into_y_coordinates(image)
    period = len(image_y)
    a_n, b_n, a_o = get_an_and_bn(image_y, period, sine_cosine_count)
    x, y = create_sine_cosine_graph(a_n, b_n, a_o, period)

    # creating the plots
    plt.plot(np.linspace(0, len(image_y), len(image_y)), image_y, label="Data From Image")
    plt.plot(x, y, label="X Y Data From Sine Waves: N={}".format(sine_cosine_count))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Preview of Graphs")
    plt.legend()

    export_to_file("waves.txt", a_n, b_n, a_o)

    plt.show()