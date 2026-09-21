import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
netflix_dataset=pd.read_csv('combined_data_1.txt',header=None,names=['Cust_ID','Ratings'],usecols=[0,1])

print(netflix_dataset.head())

netflix_dataset.isnull().sum()

movie_count=netflix_dataset.isnull().sum()

movie_count

movie_count=movie_count['Ratings']

total_count=netflix_dataset['Cust_ID'].nunique()
print("Total Customer Count:", total_count)

Customer_Count=total_count-movie_count
print("Customer Count:", Customer_Count)

rating_count=netflix_dataset['Cust_ID'].count()-movie_count
print("Rating Count:", rating_count)

stars=netflix_dataset.groupby('Ratings')['Ratings'].agg(['count'])
print("Stars Distribution:")
print(stars)

ax=stars.plot(kind='barh',legend=False,figsize=(15,10))
plt.title(f'Total movie ={movie_count} ,total customer={Customer_Count},total rating={rating_count}',fontsize=20)
plt.grid(True)
plt.show()


movid_id=None
movie_np=[]
for i in netflix_dataset['Cust_ID']:
  if ':' in i:
    movie_id=int(i.replace(':',''))
  movie_np.append(movie_id)

print("movie_np:",movie_np[:10])

netflix_dataset['Movie_ID']=movie_np
print(netflix_dataset.head())

netflix_dataset=netflix_dataset[netflix_dataset['Ratings'].notna()]
print("After removing null ratings:", netflix_dataset.head())

netflix_dataset.info()

netflix_dataset['Cust_ID']=netflix_dataset['Cust_ID'].astype(int)

netflix_dataset.info()

movie_summary=netflix_dataset.groupby('Movie_ID')['Ratings'].agg(['count'])
print("Movie Summary:",movie_summary)


movie_benchmark=round(movie_summary['count'].quantile(0.60),0)
print("Movie Benchmark:", movie_benchmark)

drop_movie_list=movie_summary[movie_summary['count']<movie_benchmark].index
print("Movies to drop:", drop_movie_list)


cust_summary=netflix_dataset.groupby('Cust_ID')['Ratings'].agg(['count'])
print("Customer Summary:", cust_summary)

cust_benchmark=round(cust_summary['count'].quantile(0.60),0)
print("Customer Benchmark:", cust_benchmark)

drop_cust_list=cust_summary[cust_summary['count']<cust_benchmark].index
print("Customers to drop:", drop_cust_list)

df_title=pd.read_csv(r"C:\Users\user\OneDrive\Documents\netflix project A\movie_titles (3).csv",encoding='latin-1',header=None,names=['Movie_ID','Year','Name'],usecols=[0,1,2])

print(df_title.head())

from surprise import Reader,SVD,Dataset
from surprise.model_selection import cross_validate

reader=Reader()

data=Dataset.load_from_df(netflix_dataset[['Cust_ID','Movie_ID','Ratings']][:100000],reader)

model=SVD()

cross_validate(model,data,measures=['RMSE'],cv=3)

user_rating=netflix_dataset[netflix_dataset['Cust_ID']==2632461]

len(user_rating)

user_2632461=df_title.copy()
print("user_2632461:", user_2632461.head())

user_2632461=user_2632461[~user_2632461['Movie_ID'].isin(drop_movie_list)]
print("user_2632461 after dropping movies:", user_2632461.head())

user_2632461['Estimated_Ratings']=user_2632461['Movie_ID'].apply(lambda X:model.predict(2632461,X).est)
print("user_2632461 with estimated ratings:", user_2632461.head())

user_2632461.sort_values('Estimated_Ratings',ascending=False,inplace=True)
print("user_2632461 sorted by estimated ratings:", user_2632461.head())








