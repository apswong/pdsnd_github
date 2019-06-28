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
    # get user input for city (chicago, new york city, washington)
    city=input('Enter the city (chicago, new york city or washington): ')

    # get user input for month (all, january, february, ... , june)

    month=input('Enter the month (all or january, february, ..., june): ')
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day=input('Enter the day of the week (all or monday, tuesday, ... sunday): ')
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    if month!='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month=df['month'].mode()[0]
    print('Most popular month: ', popular_month)

    # display the most common day of week
    popular_week=df['day_of_week'].mode()[0]
    print('Most popular day of week: ', popular_week)

    # display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print('Most popular hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_startstation=df['Start Station'].mode()[0]
    print('Most popular start station: ', popular_startstation)

    # display most commonly used end station
    popular_endstation=df['End Station'].mode()[0]
    print('Most popular end station: ', popular_endstation)

    # display most frequent combination of start station and end station trip
    popular_startend=df[['Start Station', 'End Station']].mode()
    print('Most popular start end combo: ', popular_startend)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_traveltime=df['Trip Duration'].sum()
    print('Total travel time: ', total_traveltime)

    # display mean travel time
    mean_traveltime=df['Trip Duration'].mean()
    print('Mean travel time: ', mean_traveltime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usertypes=df['User Type'].value_counts()
    print('Count user type: ', usertypes)

    # Display counts of gender
    gender=df['Gender'].value_counts()
    print('Count gender: ', gender)

    # Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    print('Earliest year of birth: ', earliest)
    latest=df['Birth Year'].max()
    print('Most recent year of birth: ', latest)
    common=df['Birth Year'].mode()[0]
    print('Most common year of birth: ', common)
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
