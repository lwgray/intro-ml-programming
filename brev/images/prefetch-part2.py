"""Bake the weeks 6-7 Keras datasets (KERAS_HOME cache) into the image."""

from keras.datasets import cifar10, fashion_mnist, mnist

mnist.load_data()          # week 6
fashion_mnist.load_data()  # week 7
cifar10.load_data()        # week 7 day 2

print('part2 prefetch complete')
