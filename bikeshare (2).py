"""This bikeshare code uses Python to explore and understand the data in the bike share system for the United States-Chicago, Washington, and New York City. The data results for all cities will have the start and end times; trip duration; start and end stations; the user type; gender; and birth year columns in the computed statistics. Additionally, the code has a script that takes in raw input to create an interactive experience in the terminal to present these statistics."""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input('Enter the name of the city you would like to explore:').lower()
        if city not in CITY_DATA:
            print('That is an invalid entry, try again!')
            continue
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        time = input('what would you like to analyse between month,day and all:')
        if time == 'month':
            month= input("May you please enter the month, between january and june that you would like to explore:").lower()
            day = 'all'
            break
        
        elif time == 'day':
            day = input('May you please enter the day of the week you would like to explore:').lower()
            month = 'all'
            break
        elif time == 'all':
            month = input('May you please enter the month, from january to june that you would like to explore:').lower()
            day = input('May you please enter the day of the week you would like to explore:').lower()
            break
        else:
            print('Entry invalid, try again!')

                     
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
   
def view_raw_data(df):
    
    """
    Function is used to display the lines of the data.
    """
    print(df.iloc[0:5]) 
    next_rows = 0
    while True:
        rows = input('Please enter YES if you would like to see the 5 lines of raw data: ') 
        rows = rows.lower()
        if rows != 'yes': 
            print('Canceled by user\n, the user would not like to see the 5 lines of raw data') 
            break
        next_rows  = next_rows  + 5 
        print(df.iloc[next_rows:next_rows +5])
        print('-'*40)
        
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most frequent month:', common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most frequent day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most frequent hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['Start Station'] = df['Start Station'].mode()[0]
    df['End Station'] = df['End Station'].mode()[0]

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(' The most common Start Station is:', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(' The most common End Station is:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['common_trip_combination'] = df['Start Station'] + " " + df['End Station']
    print(' The most common combination of Start and End Stations is:', df['common_trip_combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

import datetime 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('The total travel time is:', Total_Travel_Time)

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The average travel time is:', str(datetime.timedelta(seconds = Mean_Travel_Time)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        User_type = df['User Type'].value_counts()
        print('The user count for type {} is:\n', format(User_type))
    else:
        print('There is no gender in the city data')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        Gender = df['Gender'].value_counts()
        print('The gender count is:\n', Gender)
    else:
        print('There is no gender in the city data')
    
       
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        #The oldest year
        earliest_year = df['Birth Year'].min()
        #The most recent year
        most_recent = df['Birth Year'].max()
        #The common most year
        common_year = df['Birth Year'].mode()[0]
        print('The earliest year is:', earliest_year)
        print('The most recent year is:', most_recent)
        print('the most common year is:', common_year)
        
    else:
        print('There is no Birth Year in the city data')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        view_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
