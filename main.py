# Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
#
#     What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration
# (use 1990 as the decade's start year).
#
#     A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the
# 1990s and save this integer as short_movie_count.
#
# Feel free to experiment after submitting the project!

## The data
### **netflix_data.csv**
# | Column | Description |
# |--------|-------------|
# | `show_id` | The ID of the show |
# | `type` | Type of show |
# | `title` | Title of the show |
# | `director` | Director of the show |
# | `cast` | Cast of the show |
# | `country` | Country of origin |
# | `date_added` | Date added to Netflix |
# | `release_year` | Year of Netflix release |
# | `duration` | Duration of the show in minutes |
# | `description` | Description of the show |
# | `genre` | Show genre |

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv('/home/gustavo-plc/PycharmProjects/Netflix/netflix_data.csv')

# FIRST QUESTION:
#
# What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration
# (use 1990 as the decade's start year).

# Sol: There is a column that has this values for all movies. I can plot a histogram that has the movie duration in the x
#     axis and the absolute frequency. The year will be filtered to start on 1990 and finish on 1999


#subsetting the original dataframe: selecting only the rows that refers to movies from the 90's
year_filter = np.logical_and(netflix_df['release_year'] >= 1990, netflix_df['release_year'] < 2000)

#creating a short dataframe containing the target data
netflix_relevant = netflix_df[year_filter]

#selecting the target columns from data
netflix_relevant_lite = netflix_relevant.loc[:, ['duration', 'release_year']]

#to calculate the value that appears the most, we can use the mode. The [0] is to directly an integer, not the Series
duration = netflix_relevant_lite['duration'].mode()[0]

print(f'The most frequent movie duration in the 1990s is: {duration}')

#to calculate how many times does it appear, we can use the function count
frequency = netflix_relevant_lite['duration'].value_counts()[duration]

print(f'The most frequent duration appeared {frequency} times.')

#we can also check this graphically

plt.hist(netflix_relevant_lite['duration'], 20)
plt.show()


# SECOND QUESTION:
#
# A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the
# 1990s and save this integer as short_movie_count.

short_action = np.logical_and(netflix_relevant['genre'] == 'Action', netflix_relevant['duration'] < 90)
netflix_short_action = netflix_relevant[short_action]

short_movie_count = netflix_short_action['genre'].value_counts()['Action']

print(f'There are {short_movie_count} action movies that lasts less than 90 minutes.')

