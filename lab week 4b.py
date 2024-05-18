#Surya Hardiansyah

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.
import os
import pandas as pd

base_path = r'D:\UCHICAGO\DATA ANALYSIS PYTHON I\W4_Lab'
path = os.path.join(base_path, 'iris.csv')
data = pd.read_csv(path)
#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values, and the standard deviation?  How 
#   would you find the mean values per type of flower?  Right now you
#   can implement this with subsetting; next week we will cover how to
#   do this using groupby.
categories = list(data['species'].unique())
print(f"There are {len(categories)} categories of flowers in the data: {categories}")
# mean, median, and std of all four measures as a whole data
for column in [c for c in data.columns if data[c].dtypes == 'float64']:
    print(f"__\nThe {column} mean is {data[column].mean()}.")
    print(f"\nThe {column} median is {data[column].median()}.")
    print(f"\nThe {column} std is {data[column].std()}.\n")
# mean of four measures as per category
for category in categories:
    filtered_data = data[data['species'] == category]
    for column in [c for c in filtered_data.columns if filtered_data[c].dtypes == 'float64']:
        print(f"___\nThe {category}'s {column} mean is {data[column].mean()}.")
        print(f"\nThe {category}'s {column} median is {data[column].median()}.")
        print(f"\nThe {category}'s {column} std is {data[column].std()}.\n")
    
#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.
for column in [c for c in data.columns if data[c].dtypes == 'float64']:
    print(f"\nRows with max {column}:")
    print(data.loc[data[column] == data[column].max()])

#3. How many of observations for each species of iris is in the data?
for category in categories:
    print(f"\nThere are {len(data[data['species'] == category])} observations of Iris {category}.")

#4. Using one line of code for each column, divide each value by the mean 
#   for that measure, and assign the result to four new columns.  How is this 
#   different from a zscore?  How would you make this a zscore instead?  What's 
#   the problem with doing this without accounting for the values in the 
#   species column?
# divide by mean
data['sepal_length_norm'] = data['sepal_length'] / data['sepal_length'].mean()
data['sepal_width_norm'] = data['sepal_width'] / data['sepal_width'].mean()
data['petal_length_norm'] = data['petal_length'] / data['petal_length'].mean()
data['petal_width_norm'] = data['petal_width'] / data['petal_width'].mean()
# transform to z
data['sepal_length_z'] = (data['sepal_length'] - data['sepal_length'].mean()) / data['sepal_length'].std()
data['sepal_width_z'] = (data['sepal_width'] - data['sepal_width'].mean()) / data['sepal_width'].std()
data['petal_length_z'] = (data['petal_length'] - data['petal_length'].mean()) / data['petal_length'].std()
data['petal_width_z'] = (data['petal_width'] - data['petal_width'].mean()) / data['petal_width'].std()
# z by species
for category in categories:
    filter = data['species'] == category
    for measure in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
        data.loc[filter, f'{measure}_z_species'] = (
            data.loc[filter, measure] - data.loc[filter, measure].mean(
                )) / data.loc[filter, measure].std()
# normalizing data without taking species difference into account might mix up data 
# with different distributions and resulting misleading conclusion

#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.
data['petal_area'] = data['petal_length']*data['petal_width']

#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.
virginica_data = data[data['species'] == 'virginica'].copy()
# copy method used to overcome SettingWithCopyWarning, 
# ensuring the modifications to be independent with original DataFrame
# reference: https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
virginica_mean_sepal_length = virginica_data['sepal_length'].mean()
virginica_data['isLonger?'] = virginica_data['sepal_length'].apply(
    lambda x: 1 if x > virginica_mean_sepal_length else 0)

