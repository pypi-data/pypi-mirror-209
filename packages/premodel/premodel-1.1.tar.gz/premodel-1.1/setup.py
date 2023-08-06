from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
    name = "premodel",
    author = "Akshat Sabharwal",
    version = "1.1",
    package_dir={"":"src"},
    package=['premodel'],
    author_email = "akshatsabharwal35@gmail.com",
    description="Pre-built Machine Learning Models",
    long_description = """
    K-Nearest Neighbours

    \n\npredict: Returns the predicted value
    \n\nvisualize: Returns  a matplotlib scatter plot of the data along with the predicted point and its value. (Requires the calling of predict() method first)
    \n\neuclidean: Returns the Euclidean distance of the given point from all the points given in the dataset
    
    \n\n\nLinear Regression

    \n\nfit: Trains the model to the given data and return the slope and intercept values
    \n\npredict: Returns the predicted value""",
    install_requires = [
        'numpy',
        'matplotlib',
        'random2',
        'pandas'
    ]
    )
