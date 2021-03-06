# ioet-test

This is a simple program to calculate the weekly salary of the employees based on the hours they worked. To complete this assignment, I decided to use Python because it provides the easiest and most elegant solution for reading data from a file. I also used the [datetime module](https://docs.python.org/3/library/datetime.html) from the [Python Standard Lbrary](https://docs.python.org/3/library/).

# Preliminaries

In order to run the code, you need to have Python installed on your computer. Here is the link to [download the latest version](https://www.python.org/downloads/).

# Execution

Open a Terminal (if you're on Mac) or command line (if you're on PC) and then run ```python schedule.py <your-file.txt>```. You can either use the file provided in this repository or create your own. In case you choose the second option, make sure that the file is properly formatted.

# Testing

I included two sets of tests: one to check the file that is being passed to the program and another one to test the function that counts the weekly salary. In order to execute the first test, from the root directory, run ```python tests\test_schedule.py```. As for the second one, the command is ```python tests\test_functions.py```.
