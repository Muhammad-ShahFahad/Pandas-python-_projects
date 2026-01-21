import pandas as pd

# Creating 100 rows of messy data using pandas list multiplication
# None represents missing data
data = {
    'commit_id': list(range(100, 200)),
    'repo_name': ['web-app', 'api-core', None, 'data-tool', 'auth-service'] * 20,
    'user_name': ['octocat', None, 'dev_alice', 'dev_bob'] * 25,
    'lines_added': [120, 45, None, 0, 300, 15, None, 50, 10, 5] * 10,
    'status': ['merged', None, 'open', None] * 25,
    'stars': [10, 20, 30, 40, 50, 60, 70, 80, 90, None] * 10
}

df = pd.DataFrame(data)

#checking how many missing values are there.
print(df.isnull().sum())

#calculating the percentage of the missing data
percentage_missing_data=(df.isnull().sum()/len(df))*100

print(percentage_missing_data)

#filling the not availabe username to unknown
df['user_name']=df['user_name'].fillna('Unknown user')

#dropping the commit_id where status is missing ,because if we have not status it doesnt make any sence to keep commit id

df.dropna(axis=0,subset=['status'],inplace=True)


#cleaning the line_added

#create mean of the line added that are non null values
mean_row=df['lines_added'].mean()
print(mean_row)

#creating whole mean of the line_added considering the missing values are 0

whole_mean_rows=df['lines_added'].fillna(0).mean()

print(whole_mean_rows)

#the reason why we calculate the mean and whole is if we see the data with mean the diffrince is high bcause some rows are missing 
#the whole mean include the missing row by filling 0 in them which calculate the mean with little difference

#filling the whole mean in lines_added
df['lines_added']=df['lines_added'].fillna(0)

#fixing the repo_name

#changing the name to lower and fixing the spaces that are extra before and after of the repo_name
df['repo_name'].str.lower().str.strip()

#whe have two option here we can fill the repo_name with the forward fill or whe can mark then unknow
#we are filling the repo_name with forward fill

df['repo_name']=df['repo_name'].ffill()
print(df)
print(df.isnull().sum())

