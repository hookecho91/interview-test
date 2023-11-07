import numpy as np
import pandas as pd
from datetime import datetime
import pytz


## The following questions will test basic python skills. You can use any method you find appropriate to answer each question.
## You may not use all of or be familiar with the specific packages imported here. Feel free to look up the documentation (but do not plagiarize from the internet!)
## Try to be as "pythonic" as possible, meaning succint but still readable.
## Be sure to add comments where necessary to explain your thought process.


## Question 1: Calculate the max/min/mean/standard deviation of the following list of air temperatures
air_temps = [
    51.602615, 49.859524, 48.470085, 47.697525, 46.687443, 45.541073,
    44.666286, 43.98942 , 43.860275, 47.822605, 54.229942, 58.627052,
    63.653683, 67.31779 , 68.91037 , 68.90883 , 68.44998 , 67.293236,
    63.35947 , 59.533646, 56.772343, 53.93309 , 51.96423 , 50.234543,
    48.528698, 47.21918 , 46.48837 , 45.06273 , 42.408543, 41.13023 ,
    40.309933, 39.65729 , 39.458275, 43.752995, 47.865948, 50.738102,
    52.33936 , 53.329998, 53.931004, 54.148808, 54.06773 , 53.12362 ,
    50.489536, 46.007336, 44.048527, 43.15188 , 41.78754 , 40.966366,
    39.933105, 38.623367, 37.90904 , 36.994263, 35.838776, 34.954704,
    34.06569 , 33.2098  , 32.339573, 35.66508 , 40.866337, 44.688206,
    47.569973, 49.677372, 50.54046 , 50.73338 , 50.08771 , 48.369778,
    44.550438, 40.140743, 38.389744, 37.05095 , 36.3442  , 35.434532,
    34.190277, 33.62047 , 33.422   , 33.530163, 32.91954 , 32.755077,
    32.842472, 32.582703, 32.332653, 36.336895, 41.79034 , 45.8371  ,
    48.98073 , 50.808525, 51.95094 , 52.86253 , 53.178604, 52.917953,
    47.139805, 44.303574, 43.340843, 42.04418 , 41.28618 , 41.000206,
    40.969936, 39.65493 , 38.662537, 38.642044, 37.28573 , 36.476807,
    36.03043 , 35.12796 , 34.394073, 41.09529 , 45.74855 , 48.628563,
    51.227818, 53.366634, 54.949986, 56.19979 , 56.689396, 56.486973,
    49.926376, 46.488865, 46.33006 , 45.067398, 43.294754, 42.17338 ,
    41.031353, 39.02069 , 37.169437, 40.941044, 56.268288, 62.012985,
    55.2236  , 45.32338 , 44.33582 , 43.0452  , 40.150906, 44.510006,
    58.955162, 63.818535, 57.26376 , 52.627037, 47.87111 , 46.45964 ,
    43.882633, 46.99627 , 56.874844, 61.227684, 55.79703 , 53.713253,
    49.435177, 47.794205, 46.04359 , 47.64891 , 56.66962 , 61.106064,
    57.80808 , 50.499424, 48.42449 , 44.345707, 42.472538, 45.68571 ,
    56.844303, 61.79205 , 54.202312, 48.072433, 45.97987 , 43.678177,
    41.940197, 45.616276, 57.6524
    ]

## Put your code here


mean = 
max = 
min = 
std = 

## Print the answers to Q1
print(
    f"""Q1:
    Mean: {mean}
    Max: {max}
    Min: {min}
    Std: {std}
    """
    )


## Question 2: Format/convert the datetime object into these following patterns/timezones:
## A) YY-MM-DD HH:MM in Eastern Standard Time (i.e. 23-11-07 07:30 EST)
## B) YYYYMMDDHH in Central Standard Time
## C) YYYYMMDDHH in UTC
date = datetime(year=2023, month=11, day=7, hour=13, minute=30, tzinfo=pytz.timezone('UTC'))

## Print the answers to Q2
print(
    """
    Q2A: {}
    Q2B: {}
    Q2C: {}
    """
)

