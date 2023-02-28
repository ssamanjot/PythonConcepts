import concurrent.futures
import time
import urllib.request
import matplotlib.pyplot as plt
from random import sample
import numpy as np


def OpenUrl(n):
     start_time = time.time()
     urllib.request.urlopen(n)
     return time.time(),start_time


def main(NoOfProcess,Urls):
    StopTimeLists = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=NoOfProcess) as executor:
        for processing_time in (executor.map(OpenUrl, Urls)):
            StopTimeLists.append(processing_time)
    return StopTimeLists


def visualize_processing_time(results,colors,MaxWorker):
    start, stop = np.array(results).T
    fig = plt.figure()
    plt.barh(range(len(start)), stop - start, left=start, color=colors)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.title("Tasks for URL Server Responses; " + str(MaxWorker) +" Thread")
    plt.savefig('foo'+str(MaxWorker)+'.png')
    plt.show()


def generate_bar_colors(number_of_threads_or_subprocesses):
    good_colors = ['firebrick', 'darkgreen', 'royalblue', 'rebeccapurple', 'dimgrey', 'teal', 'chocolate', 'darkgoldenrod']
    colors = sample(good_colors, number_of_threads_or_subprocesses)
    return colors


Urls=[]
MaxWorker=[1,2,4]

with open('C:/Users/cool dude/PycharmProjects/hello\Multithreading/Data/url.txt', "r", encoding=None) as y:
    for line in y:
        Urls.append(line)

for v in MaxWorker:
 Stop_Time=[]
 if __name__ == '__main__':
    Stop_Time = main(v,Urls)
    colors = generate_bar_colors(v)
    visualize_processing_time(Stop_Time,colors,v)
