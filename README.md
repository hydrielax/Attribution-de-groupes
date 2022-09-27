# Group assignment algorithm

This is an algorithm to assign different people to different groups,
according to their preferences.

## How to use it?

* Create a spreadsheet, with people on rows and groups/projects on columns.
    The first row must be the name of the project, the second one indicates
    the number of people wanted for this project/group.
* Export the spreadsheet as a csv file, and name it `input.csv`
* Install the `scipy` dependency: `pip3 install scipy`
* Run the algorithm: `python3 algo.py > results.py
* The results are exported into the `results.txt` file.

## How does the algorithm work?

* See [this page](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html) for more info of the algorithm used. It is based on [this research paper](https://ieeexplore.ieee.org/document/7738348).