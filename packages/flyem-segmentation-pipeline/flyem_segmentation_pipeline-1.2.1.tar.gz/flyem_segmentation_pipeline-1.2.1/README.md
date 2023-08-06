# CS410_FlyEM_PyPi
This repository hosts the segmentation pipeline to segment fly retina images using traditional segmentation algorithms.


## Authors

* [Prof. Daniel Haehn](https://github.com/haehn)
* [Sai Harshavardhan Reddy Kona](https://github.com/kshvr16)
* [Nikhila Yadav Lankela](https://github.com/Nikhila1003)
* [Varshitha Hantur Dinakar](https://github.com/varshi-123)
* [Varuni Manjunath](https://github.com/Varunii)
* [Kiran Sandilya](https://github.com/Kiransandilya)
* [Kunal Jain](https://github.com/jainkhere)


## Package Installation

Install this python package by executing the following command.
```bash
  pip install flyem_segmentation_pipeline
```
If the above command throws any error, please run the following command and install the dependency packages individually.
```bash
pip install flyem_segmentation_pipeling --no-deps
```


## Required Python packages

* [numpy](https://pypi.org/project/numpy/)
* [mahotas](https://pypi.org/project/mahotas/)
* [matplotlib](https://pypi.org/project/matplotlib/)
* [scikit-image](https://pypi.org/project/scikit-image/)

    ## Dependency package issues
All the above-mentioned packages are required to use this package, but due to the version issues with numpy and mahotas, during installation only matplotlib and scikit-image are installed; numpy and mahotas has to be installed separately.
