import pandas as pd
import numpy as np

df=pd.read_csv(r"Countries.csv")
print(df)
# Identifying the shape of the dataframe
print(df.shape)
#Identifying data
print(df.info())
print(df.describe())
#Searching for any missing data
print(df.isna().sum())


#Q1- Which country has the highest population
print(df[df['population']==df['population'].max()]) # if we want to see all other information about the most populated country we use this
print('Highest populated country is',df.loc[df['population'].idxmax(),'country']) # if we want only name of the country which is most populated we use this
print(df['population'].max(),'people') #This show the max population by number

#Q2- What is the capital of the country with highest population
print('Highest populated country`s capital is',df.loc[df['population'].idxmax(),'capital_city']) 

#Q3- Which country has the least population
print(df[df['population']==df['population'].min()]) # for all info about least populated country
print('least populated country is',df.loc[df['population'].idxmin(),'country']) # for name of the least populated country only

#Q4-What is the capital of the least populated country
print('least populated country`s capital is',df.loc[df['population'].idxmin(),'capital_city']) 

#Q5-Give the top 5 countries with highest democratic score
print(df.columns)
print(df.nlargest(5,'democracy_score')[['country','democracy_score']])# we can also sort and then print top 5 but this is the best method to do this

#Q6- How many total region are there 
print(df['region'].value_counts()) # This print all the region along with the number of appearance
print(df['region'].value_counts().count()) # This print the total number of region not the total of appearance

#Q7-How many countries lies in eastern europe region
print(df['region'].value_counts()['Eastern Europe'])
print(df[df['region']=='Eastern Europe'])

#Q8-Who is the poltical leader of the 2nd highest populated country
print(df[df['population']==df['population'].nlargest(2).iloc[1]]['political_leader'])

#Q9-How many country are there whoes political leader are NaN
print(df[df['political_leader'].isna()]['country'].count())
#Q10-How many country which have republic in there name
count=0
def republic_name_count(txt):
    global count
    if 'republic' in txt.lower():
        count+=1
    return txt

df['country_long']=df['country_long'].apply(republic_name_count)
print(count)

#Q11-Which country in affrican country have highest population
africa_df=df[df['continent']=='Africa']
print(africa_df)
print(africa_df[africa_df['population']==africa_df['population'].max()]['country'])

