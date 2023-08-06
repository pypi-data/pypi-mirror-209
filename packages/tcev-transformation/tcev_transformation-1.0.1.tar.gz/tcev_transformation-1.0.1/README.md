# **TCEV Data Transformation Library**

Library for common data transformations used in machine learning models, utilizing only the standard Python library and/or Numpy. Includes transposition, time series windowing & cross-correlation.
_______________________________________________________________________

## **Description**

The repository contains 3 data transformation and associated unit tests for the following functions:

* `transpose2d` -> a function that takes in a 2D matrix of real numbers and swaps the axis (standard transpose logic).
* `window1d` -> a function that converts a 1D list / np.array into window subsets of the input, given additional parameters on size of window, shift between windows & stride within a window.
* `convolution2d` -> a function that takes an input 2D array, a kernel 2D array and combines them to produce a 2D array using cross-correlation operations. Allows for an optional stride parameter, which determines the slide or "shift" between cross-correlation operations.

The repo has been packaged, built and published to PyPi.
________________________________________________________________________

### **Dependencies**

* Poetry
* Numpy
* Pytest (for running user tests only)

After cloning the repository, run bash command `poetry install`.
________________________________________________________________________    

## **Authors**

Ernestas Vainorius
[@LinkedIn](https://www.linkedin.com/in/ernestas-vainorius-742711181/)
________________________________________________________________________

## **Version history**
* __v1.0.0:__
    * Added an additional unit test for `convolution2d` for testing larger matrices.
    * Changed `src` directory name to `tcev_transformation` to allow easier to understand library import post publishing. 
    * Finalized README.md.
    * Packaged, built and published repo to PyPi.
    * See [change notes](https://github.com/TuringCollegeSubmissions/evaino-DE2.1/releases/tag/v0.3.0)
* __v0.3.0:__
    * Created a `convolution2d` function that takes an input 2D array, a kernel 2D array and combines them to produce a 2D array using cross-correlation operations.
    * Created unit tests for checking `convolution2d` functionality and parameter intake.
    * See [change notes](https://github.com/TuringCollegeSubmissions/evaino-DE2.1/releases/tag/v0.3.0)
* __v0.2.0:__
    * Implemented `window1d` function, which allows to create window subsets from a starting input array/list, with additional parameters for window size, shift between each window, stride within a window.
    * Wrote unit tests for `transpose2d` & `window1d` functions
    * See [change notes](https://github.com/TuringCollegeSubmissions/evaino-DE2.1/releases/tag/v0.2.0)
* __v0.1.0:__
    * Created `transpose2d` function, which allows for transposition of any 2D real-number matrices
    * Base file structure created, including Poetry files for dependency management
    * See [change notes](https://github.com/TuringCollegeSubmissions/evaino-DE2.1/releases/tag/v0.1.0)