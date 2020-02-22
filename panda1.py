import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# We're now creating a dataframe straight from a data file
insurance= pd.read_csv(filepath_or_buffer='/home/reeta/python-notebook/insurance.csv',
                      sep=',',
                      header=0)



#2.Load the insurance.csv in a DataFrame using pandas. Explore the dataset using functions like to_string(), columns, index, dtypes, shape, info() and describe(). Use this DataFrame for the following exercises

#pretty_print("Printing an entire dataframe", insurance.to_string())
#pretty_print("Show all column names for a dataframe", insurance.columns)
#pretty_print("Show all index names for a dataframe", insurance.index)
#pretty_print("Getting the shape of a dataframe", insurance.shape)
#pretty_print("Pandas can automagically infer the type for a DataFrame by checking all values for us", insurance.dtypes)
#pretty_print("Summarized info on dataframe", insurance.info())
#pretty_print("Quick stats on all numeric columns for dataframe", insurance.describe())


#3.Print only the column age
#pretty_print("Selecting only the age column", insurance['age'])

#4.print only the columns age,children and charges

#pretty_print("Selecting multiple columns: the Age, Children and Charges columns", insurance[['age', 'children', 'charges']])


#5.Print only the first 5 lines and only the columns age,children and charges

#df = insurance.iloc[[0,1,2,3,4,5],[0,3,6]]

#print(df)


#pretty_print("Selecting rows by multiple criteria", insurance[insurance['age'] [:5, :]) & (insurance['children'] [:5, :]) & (insurance['charges'][:5, :])])



#6.What is the average, minimum and maximum charges ?

#print(insurance['charges'].mean(),insurance['charges'].max(),insurance['charges'].min())

#7.What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?

search = '10797.3362'
df= insurance.loc[insurance['charges'] == 10797.3362]
#print(df)
#print(df[['age','sex','smoker']])

#8.What is the age of the person who paid the maximum charge?

maxcharge= insurance['charges'].max()
df1= insurance.loc[insurance['charges'] == maxcharge]
#print(df1)
#print(df1[['age','charges']])


#9.How many insured people do we have for each region?

#print(insurance.region.value_counts())

#10.How many insured people are children?

#print(insurance.children.sum())

#11.What do you expect to be the correlation between charges and age, bmi and children?

##I think, charges are depend on age and bmi 

#12.Using the method corr(), check if your assumptions were correct.


#data = insurance[['charges','age','bmi','children']]
#c = data.corr(method='pearson')
#print(c)

###Yes, charges are depend or correlated  on age and bmi.  bmi and age are also correlated.


