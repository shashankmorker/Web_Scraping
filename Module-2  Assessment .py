#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install beautifulsoup4,seleniumBase # installing beautifulsoup and seleniumBase


# # The data keeps updating in every few days so I am saving the current dataFrame to a CSV file on 6/11/2023, So that my data doesn't change.

# In[22]:


from bs4 import BeautifulSoup # importing beautifulSoup, numpy and pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


from seleniumbase import Driver # importing drivers from seleniumBase
driver = Driver()
driver.maximize_window()
from selenium.webdriver.common.by import By # importing By from selenium.webdriver.common.by to open a new selenium browser.


# In[3]:


url = "https://www.naukri.com/data-scientist-jobs-in-bangalore-bengaluru?k=data%20scientist&l=bangalore%2Fbengaluru&experience=2&nignbevent_src=jobsearchDeskGNB"
driver.get(url) # Using this step we will be adding the above url to the selenium browser for scraping.  


# In[4]:


ID = driver.find_elements(By.XPATH,"//div[@class = 'srp-jobtuple-wrapper']")
data = [] # Here I scraped all the job Id's in that page which gave me all the required information.  
for i in ID:
    data.append(i.text)
data


# In[5]:


len(data) # Here I checked the length of data


# In[6]:


# I created a new list named new_data, used for loop to iterate and used spilit function to split individual job openings. 

new_data = [] # I created a new list named new_data 
for i in range(len(data)):
    data_list = data[i].split('\n')
    new_data.append(data_list)
# Print the list
for item in new_data:
    print(item) # When I run this code I get all 20 job openings in seperate lists. 


# In[7]:


new_data[1] = ['Sr . Data Scientist', 'Enlink', '?', '?', '2-5 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Mumbai, Navi Mumbai, Hyderabad/Secunderabad, Pune, Chennai', 'The ideal candidate should possess strong JAVA development skills and a solid understan...', 'Computer scienceFront endData modelingMISJavascriptData structuresHTMLUnit testing', '2 Days Ago', 'Save']


# In[8]:


new_data[5] = ['Data Scientist', 'Careernet Technologies','?','?', '2-7 Yrs', 'Not disclosed', 'Hybrid - Bangalore/Bengaluru', 'Experience in data mining techniques and methodologies. (data prep / modeling, classifi...', 'pythonAWSSQLData MiningMachine LearningDeep LearningDataMachine', '26 Days Ago', 'Save']


# In[9]:


new_data[16] = ['Solution Architect', 'Scribble Data','?', '?', '1-2 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Kolkata, Mumbai, New Delhi, Hyderabad/Secunderabad, Pune, Chennai', 'Experience developing and implementing best-in-class algorithms for multiple among user...', 'NoSQLdata scienceTime series analysisCustomer engagementMATLABSolution ArchitectSQLPython', '30+ Days Ago', 'Save']


# In[10]:


df = pd.DataFrame(new_data)
df.columns = ['Job Title', 'Company', 'Rating', 'Reviews', 'Experience', 'Salary', 'Location', 'Job Description', 'Skills', 'Posted', 'Save']
df.to_csv('job_portal.csv',index=False)
df # Here when I am running the code and empty values in Ratings and Reviews are showing as "?" 


# # This is the CSV file. 

# In[112]:


df = pd.read_csv('job_portal.csv')
df


# In[113]:


# # Managed the data by replacing "?" in the missing area  
# new_data[3] = ['Sr . Data Scientist', 'Enlink',"?","?", '2-5 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Mumbai, Navi Mumbai, Hyderabad/Secunderabad, Pune, Chennai', 'The ideal candidate should possess strong JAVA development skills and a solid understan...', 'Computer scienceFront endData modelingMISJavascriptData structuresHTMLUnit testing', 'Few Hours Ago', 'Save']
# # new_data[8] = ['Data Scientist', 'Careernet Technologies',"?","?", '2-7 Yrs', 'Not disclosed', 'Hybrid - Bangalore/Bengaluru', 'Experience in data mining techniques and methodologies. (data prep / modeling, classifi...', 'python AWS SQL Data Mining Machine Learning Deep Learning Data Machine', '23 Days Ago', 'Save']
# new_data[18] = ['Solution Architect', 'Scribble Data',"?","?", '1-2 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Kolkata, Mumbai, New Delhi, Hyderabad/Secunderabad, Pune, Chennai', 'Experience developing and implementing best-in-class algorithms for multiple among user...', 'NoSQLdata scienceTime series analysisCustomer engagementMATLABSolution ArchitectSQLPython', '30+ Days Ago', 'Save']


# In[114]:


df.replace('?',np.nan, inplace = True) # I have replaced "?" to NaN values so that I can further manage the data.
df


# In[115]:


df.shape # Here I checked number of rows and columns.


# In[116]:


# Remove non-numeric values from 'reviews' column
df['Reviews'] = df['Reviews'].str.replace(r'\D', '', regex = True) # Infuture update we have to add regex=True after ''
# Change the object type to float
df['Reviews'] = df['Reviews'].astype(float)
df


# In[117]:


# pd.to_numeric() function is used to convert the column to a numeric type and convert non_numeric number to NaN
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce') 
df


# In[118]:


df['Rating'].fillna(value=df['Rating'].mean(), inplace=True) # fillings 
df['Reviews'].fillna(value=df['Reviews'].mean(), inplace=True)
df['Rating'] = df['Rating'].round(1)
df['Reviews'] = df['Reviews'].round(1)


# In[119]:


df['Experience'] = df['Experience'].str.replace(r'\D', '', regex = True) # Infuture update we have to add regex=True after ''
# Change the object type to float
df['Experience'] = df['Experience'].astype(float)
df


# In[120]:


df["Experience_min"] = df["Experience"]// 10
df["Experience_max"] = df["Experience"]% 10
del df["Experience"]
df


# In[121]:


# Saved column is useless and also salary column values are all "not disclosed" so we can terminate both these columns.
del df["Save"]
del df["Salary"]


# In[122]:


df


# In[123]:


df.shape


# In[96]:


sns.distplot(df['Rating'])
plt.title('Distribution of Ratings')


# In[100]:


value_counts = df['Job Title'].value_counts()

# Create a pie chart
plt.figure(figsize=(10,6))
plt.pie(value_counts, labels = value_counts.index, autopct='%1.0f%%')
plt.title('Pie chart of Job Title')
plt.show()


# ### Conclusion:
# Based on this pie-chart 55% of the job openings are related to the specific job role, and rest is for Data Scientist role. 

# In[104]:


sns.histplot(df["Experience_min"], bins = 30)


# ### Conclusion :
# Most of the job titles are for senior level which requires minimum of 0 - 2.5 yrs of experience. Also there are few companies which requires over 20 yrs of experience. 

# In[111]:


sns.distplot(df["Experience_max"])


# ### Conclusion :
# In an average 5 yrs of experince is enough to get a senior level job. 
