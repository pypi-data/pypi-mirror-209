from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
    name = "premodel",
    author = "Akshat Sabharwal",
    version = "1.0",
    package_dir={"":"src"},
    package=['premodel'],
    author_email = "akshatsabharwal35@gmail.com",
    description="Pre-built Machine Learning Models",
    long_description = """
    \bK-Nearest Neighbours\b

    predict: Returns the predicted value
    visualize: Returns  a matplotlib scatter plot of the data along with the predicted point and its value. (Requires the calling of predict() method first)
    euclidean: Returns the Euclidean distance of the given point from all the points given in the dataset""",
    install_requires = [
        'numpy',
        'matplotlib',
        'random2',
        'pandas'
    ]
    )
