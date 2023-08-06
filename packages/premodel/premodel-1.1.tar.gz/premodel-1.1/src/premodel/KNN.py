import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

class kNN:
    def __init__(self, k):
        self.k = k

    def fit(self, x: list, y: list, labels: list):
        global data_x
        global data_y
        global label
        global targets
        global colormap
        data_x = np.array(x)
        data_y = np.array(y)
        label = np.array(labels)
        targets = np.unique(label)
        colormap = dict(zip(targets, [tuple(np.array([random.random() for i in range(3)]).astype(np.float16)) for k in range(len(targets))]))

        if len(label) != len(data_x) != len(data_y):
            raise ValueError("Array lengths don't match")
        else:
            pass
    
    def euclidean(self, point: tuple):
        self.x, self.y = point
        distance_array = []
        points_array = []
        for a, b in zip(data_x, data_y):
            distance_array.append(((a-self.x)**2 + (b-self.y)**2)**0.5)
            points_array.append((a, b))
        return distance_array, points_array
    
    def predict(self, point: tuple):
        self.x, self.y = point
        dist, points = kNN(self.k).euclidean((self.x, self.y))
        near_dist = np.argsort(dist)[:self.k]
        class_near_points = [label[x] for x in near_dist]
        class_count = [class_near_points.count(f"{x}") for x in targets]
        return targets[np.argmax(class_count)]
    
    def visualize(self):
        plt.scatter(data_x, data_y, c = pd.Series(label).map(colormap))
        plt.scatter(self.x, self.y, c = tuple([random.random() for i in range(3)]))
        print(kNN(self.k).predict((self.x, self.y)))
        plt.show()


        







