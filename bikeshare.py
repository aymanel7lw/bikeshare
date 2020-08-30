import time
import pandas as pd
import numpy as np

CITY_DATA   = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city        = ''
months  = ['january','february','march','april','may','june']
days    = ['monday','sunday','tueday','wednesday','thursday','friday','saturday','sunday']

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
    city    = input('Would you like to see data for chicago, New York, or Washington?\n')
    city    = city.lower()


    if city == 'new york':
        city    = 'new york city'
    # TO DO: get user input for month (all, january, february, ... , june)
    choice  = input('Would you like to filter the data by month, day, both?\n')
    choice  = choice.lower()
    if choice == 'month' :
        month   = input('Which month? January, February, March, April, May or June\n')
        month   = month.lower()
        day     = 'all'
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if choice == 'day' :
        day     = input('Which day?\n')
        day     = day.lower()

        month   = 'all'

    if choice == 'both' :
        month   = input('Which month? January, February, March, April, May or June\n')
        month   = month.lower()

        day     = input('Which day? Please type your response as a day name (e.g., Sunday)\n')
        day     = day.lower()


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
    df          = pd.read_csv(CITY_DATA[city])
    
    print(df.head())
    
    n   = 2
    while True:
        answer  = input('\n Would you like to display 5 more row of the raw data ? Press [y/n] ')
        if answer == 'y' :
            print(df.head(5 * n))
            n += 1
        else :
            break

    df['Start Time']  = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']   = df['Start Time'].dt.dayofweek

    if month != 'all' :

        month   = months.index(month) + 1
        df      = df[df['month'] == month]
    if day != 'all' :

        day     = days.index(day)
        df      = df[df['day_of_week'] == day]

    return  df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all': 
        counts  = df['month'].value_counts()
        most_common_month    =  counts[counts == counts.max()].index.tolist()[0]
        month   = 'Most common month : {}'.format(months[most_common_month - 1].title())
        print('\n',month)
    # TO DO: display the most common day of week
    if day == 'all':
        counts  = df['day_of_week'].value_counts()
        most_common_day_of_week = counts[counts == counts.max()].index.tolist()[0]
        day_of_week   = 'Most common day of week : {}'.format(days[most_common_day_of_week].title())
        print('\n',day_of_week)
    # TO DO: display the most common start hour
    counts  = df['Start Time'].dt.hour.value_counts()
    most_common_start_hour = counts[counts == counts.max()].index.tolist()[0]
    start_hour   = 'Most common start hour : {}'.format(most_common_start_hour)
    print('\n',start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    counts  = df['Start Station'].value_counts()
    most_common_start_station   = counts[counts == counts.max()].index.tolist()[0]
    start_station   = 'Most common start station : {}'.format(most_common_start_station)

    # TO DO: display most commonly used end station
    counts  = df['End Station'].value_counts()
    most_common_end_station = counts[counts == counts.max()].index.tolist()[0]
    end_station   = 'Most common end station : {}'.format(most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_of_start_end_stations']   = df['Start Station'] + ' - ' + df['End Station']
    counts  = df['combination_of_start_end_stations'].value_counts()
    most_common_combination_start_end_stations  = counts[counts == counts.max()].index.tolist()[0]
    combination_start_end   = 'Most common combination : {}'.format(most_common_combination_start_end_stations)

    print('\n',start_station,'\n',end_station,'\n',combination_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total   = 'Total travel time : {}'.format(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    mean    = 'Mean travel time : {}'.format(df['day_of_week'].mean())

    print('\n',total,'\n',mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts      = df['User Type'].value_counts()
    subscribers  = 'Subscribers : {}'.format(counts['Subscriber'])
    customers   = 'Customers : {}'.format(counts['Customer'])

    if city == 'washington':
        print ('\n',subscribers,'\n',customers)
    # TO DO: Display counts of gender
    else:
        counts  = df['Gender'].value_counts()
        males   = 'Males : {}'.format(counts['Male'])
        females = 'Females : {}'.format(counts['Female'])

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest    = 'Earliest year of birth {}'.format(df['Birth Year'].min())
        most_recent = 'Most recent year of birth : {}'.format(df['Birth Year'].max())

        counts      = df['Birth Year'].value_counts()
        most_common = 'Most common year of birth : {}'.format(counts[counts == counts.max()].index.tolist()[0])

        print('\n',subscribers,'\n',customers,'\n',males,'\n',females,'\n',earliest,'\n',most_recent,'\n',most_common)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)             

def main():
    while True:
        try:
       
           city, month, day    = get_filters()
           df = load_data(city, month, day)

           time_stats(df,month,day)
           station_stats(df)
           trip_duration_stats(df)
           user_stats(df,city)
           restart = input('Would you like to restart? Enter y or n.\n')
            
           if restart.lower() != 'y':
                break
        except:
            print('Make Sure There Are No TYPO')
                
if __name__ == "__main__":
	main()
