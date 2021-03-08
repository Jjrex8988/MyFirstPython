## Task 1: Instructions
## 1. TV, halftime shows, and the Big Game
# Import pandas
import pandas as pd

# Load the CSV data into DataFrames
super_bowls = pd.read_csv("super_bowls.csv")
tv = pd.read_csv("tv.csv")
halftime_musicians = pd.read_csv("halftime_musicians.csv")



## Task 2: Instructions
## 2. Taking note of dataset issues
# Display the first five rows of each DataFrame
print(super_bowls.head())
print("-"*38)
print(tv.head())
print("-"*38)
print(halftime_musicians.head())
print("-"*38)

# Summary of the TV data to inspect
print(super_bowls.info())
print("-"*38)

print(tv.info())
print("-"*38)

# Summary of the halftime musician data to inspect
print(halftime_musicians.info())
print("-"*38)



## Task 3: Instructions
## 3. Combined points distributio
# Import matplotlib and set plotting style
from matplotlib import pyplot as plt
plt.style.use("seaborn")

# Plot a histogram of combined points
plt.hist("combined_pts")
plt.xlabel("Combined Points")
plt.ylabel("Number of Super Bowls")
plt.show()


# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls["combined_pts"] > 70])
print("-"*38)
print(super_bowls[super_bowls["combined_pts"] < 70])
print("-"*38)



## Task 4: Instructions
## 4. Point difference distribution
# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.xlabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls["difference_pts"] == 1])
print("-"*38)
print(super_bowls[super_bowls["difference_pts"] >=35])
print("-"*38)



## Task 5: Instructions
## 5. Do blowouts translate to lost viewers
# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn
import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)
plt.show()



## Task 6: Instructions
## 6. Viewership and the ad industry over time
# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

plt.tight_layout()
plt.show()


## Task 7: Instructions
## 7. Halftime shows weren't always this great
# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
print(halftime_musicians.musician[halftime_musicians.super_bowl <= 27])
print("-"*38)



## Task 8: Instructions
## Who has the most halftime show appearances?
# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

print(halftime_appearances.head())
print("-"*38)

# Display musicians with more than one halftime show appearance
print(halftime_appearances.musician[halftime_appearances.super_bowl > 1])
print("-"*38)



## Task 9: Instructions
## 9. Who performed the most songs in a halftime show?
# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Song Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
print(no_bands.head(15))
print("-"*38)


## Task 10: Instructions
## 10. Conclusion
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

super_bowls_LIII_winner = rams
print('The winner of Super Bowl LIII will be the', super_bowls_LIII_winner)