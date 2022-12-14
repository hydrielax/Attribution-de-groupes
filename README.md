# Group assignment algorithm

This is an algorithm to assign different people to different groups,
according to their preferences.

## How to use it?

* Create a spreadsheet, with people on rows and groups/projects on columns.
    The first row must be the name of the project, the second one indicates
    the number of people wanted for this project/group.
* Export the spreadsheet as a csv file, and name it `input.csv`
* Install the `scipy` dependency:
    ```bash
    pip3 install scipy
    ```
    or
    ```bash
    conda install scipy
    ```
* Run the algorithm:
    ```bash
    python3 algo.py > results.txt
    ```
* The results are exported into the `results.txt` file.

## How does the algorithm work?

* The function used is a standard function of `scipy` (see [this page](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html)). The algorithm used in this function is based on [this research paper](https://ieeexplore.ieee.org/document/7738348).