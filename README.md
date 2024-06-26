# Fourier Calculator

I wrote this entire thing in less than 2 hours, so this is probably going to break. Here is the idea:

You have a list of images (black and white) and would like to turn it into sin and cosine graphs to be put on desmos. You would run the script and it would generate those graphs. 

# How to run code 

```
pip3 install -r requirements.txt 
python3 main.py
```

It would asked you for the path to your image and you would be able to generate the corresponding graphs. This would generate a file called waves.txt which stores all the fourier coefficient. 

```
python3 desmos.py
```
This would generate a list of functions that you could paste into desmos. You would have to run the code above before. You would likely have to zoom out to see the image. 

# Example 
Here is the original image: 

![cosine_graph](images/test_2.png)

Here is the image encoded by sine and cosines graphs:

![cosine_graph](images/plot.png)

Here is a graph in desmos 

![cosine_graph](images/desmos.png)