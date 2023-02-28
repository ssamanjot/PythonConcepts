A thread is a path which is followed during a programs execution. There could be multiple threads in a
process.

MultiThreading.py is coded to use Thread Pool Executor to run the threads. The list of urls can be found in the url.txt file found in the handout. urlopen is used in this program to open each link and measure the time taken. Then plotted the time on the X-axis and number of urls visited on the Y-axis using 1,2 and 4 processes. Plot.show is used to open plot in figure and save plot as image with name including number of process.