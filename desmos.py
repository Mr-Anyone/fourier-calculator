import numpy as np

def get_function_from_file(path_to_file):
    function_string = ""
    with open(path_to_file, "r") as f:
        function_string += f.readline().replace("\n", "")
        period = float(f.readline())

        lines = f.readlines()
        for i in range(len(lines)): 
            current_line = lines[i].replace("\n", "")
            a_n, b_n = current_line.split("|")[0] , current_line.split("|")[1]

            angular_frequency = 2* np.pi * (i + 1) / period
            if i !=  len(lines) - 1:
                function_string +=  f"+ {a_n}cos({angular_frequency}x) + {b_n}sin({angular_frequency}x) "
            else: 
                function_string +=  f"{a_n}cos({angular_frequency}x) + {b_n}sin({angular_frequency}x)"
    
    return function_string

if __name__ == "__main__":
    function = get_function_from_file("waves.txt")
    print(function)