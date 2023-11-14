#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install beautifulsoup4


# In[2]:


#  pip install seleniumBase


# In[65]:


from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time


# In[66]:


from seleniumbase import Driver


# In[67]:


driver = Driver()
driver.maximize_window()


# In[68]:


from selenium.webdriver.common.by import By


# In[91]:


url = "https://www.naukri.com/data-scientist-jobs-in-bangalore-bengaluru?k=data%20scientist&l=bangalore%2Fbengaluru&experience=2&nignbevent_src=jobsearchDeskGNB"
driver.get(url)


# In[70]:


t = driver.find_elements(By.XPATH,"//div[@class = ' row1']")
title = []
for i in t:
    title.append(i.text)
title


# In[71]:


c = driver.find_elements(By.XPATH,"//a[@class = ' comp-name mw-25']")
company = []
for i in c:
    company.append(i.text)
company


# In[72]:


# trying 
entries = driver.find_elements(By.XPATH, "//div[@class = 'cust-job-tuple layout-wrapper lay-2 sjw__tuple']")  # Update 'parent-class' with the actual parent class

title = []
company = []

for entry in entries:
    title_element = entry.find_element(By.XPATH, "//div[@class = ' row1']")  # Created relative XPath with './/'
    company_element = entry.find_element(By.XPATH, "//a[@class = ' comp-name mw-25']")  # Created relative XPath with './/'
    
    title.append(title_element.text)
    company.append(company_element.text)
print(title, company)


# In[73]:


ra = driver.find_elements(By.XPATH,"//a[@class = 'rating']")
rating = []
for i in ra:
    rating.append(i.text)
rating


# In[74]:


y = driver.find_elements(By.XPATH,"//span[@class = 'ni-job-tuple-icon ni-job-tuple-icon-srp-experience exp']")
experience = []
for i in y:
    experience.append(i.text)
experience


# In[75]:


jd = driver.find_elements(By.XPATH,"//div[@class = 'styles_JDC__dang-inner-html__h0K4t']")
job_description = []
for i in jd:
    job_description.append(i)


# In[76]:


t = driver.find_elements(By.XPATH,"//a[@class = 'title ']")
jd = []
for i in t:
    jd.append(i.get_attribute('href'))


# In[77]:


jd


# In[78]:


des = []
driver.get(jd[0])


# In[79]:


driver.find_element(By.XPATH,"//div[@class = 'styles_JDC__dang-inner-html__h0K4t']").text


# In[80]:


for i in jd:
    try:
        driver.get(i)
        time.sleep(2)
        des.append(driver.find_element(By.XPATH,"//div[@class = 'styles_JDC__dang-inner-html__h0K4t']").text)
    except:
        des.append("")


# In[81]:


des


# In[82]:


(len(title), len(company), len(rating), len(experience), len(des))


# In[ ]:





# In[85]:


df = pd.DataFrame({
    "Title": title,
    "Company":company,
    "Rating": rating,
    "Work_Experience": experience,
    "Job_Description": des
}) 


# # NEW METHOD

# In[92]:


ID = driver.find_elements(By.XPATH,"//div[@class = 'srp-jobtuple-wrapper']")
# ID = driver.find_elements(By.XPATH,"//*[@id="listContainer"]/div[2]/div/div[1]")
data = []
for i in ID:
    data.append(i.text)
data


# In[93]:


len(data)


# In[94]:


# data[0]
new_data = []
for i in range(len(data)):
    data_list = data[i].split('\n')
    new_data.append(data_list)
# Print the list
for item in new_data:
    print(item)


# In[95]:


# print(new_data[3])


# In[84]:


# new_data[3] = ['Sr . Data Scientist', 'Enlink',"NA","NA", '2-5 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Mumbai, Navi Mumbai, Hyderabad/Secunderabad, Pune, Chennai', 'The ideal candidate should possess strong JAVA development skills and a solid understan...', 'Computer scienceFront endData modelingMISJavascriptData structuresHTMLUnit testing', 'Few Hours Ago', 'Save']


# In[86]:


# print(new_data[8])


# In[87]:


# new_data[8] = ['Data Scientist', 'Careernet Technologies',"NA","NA", '2-7 Yrs', 'Not disclosed', 'Hybrid - Bangalore/Bengaluru', 'Experience in data mining techniques and methodologies. (data prep / modeling, classifi...', 'python AWS SQL Data Mining Machine Learning Deep Learning Data Machine', '23 Days Ago', 'Save']


# In[89]:


# print(new_data[18])


# In[90]:


# new_data[18] = ['Solution Architect', 'Scribble Data',"NA","NA", '1-2 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Kolkata, Mumbai, New Delhi, Hyderabad/Secunderabad, Pune, Chennai', 'Experience developing and implementing best-in-class algorithms for multiple among user...', 'NoSQLdata scienceTime series analysisCustomer engagementMATLABSolution ArchitectSQLPython', '30+ Days Ago', 'Save']


# In[101]:


# df = pd.DataFrame(new_data)
# df.columns = ['Job Title', 'Company', 'Rating', 'Reviews', 'Experience', 'Salary', 'Location', 'Job Description', 'Skills', 'Posted', 'Save']

# df


# In[106]:


new_data[3] = ['Sr . Data Scientist', 'Enlink',"?","?", '2-5 Yrs', 'Not disclosed', 'Bangalore/Bengaluru, Mumbai, Navi Mumbai, Hyderabad/Secunderabad, Pune, Chennai', 'The ideal candidate should possess strong JAVA development skills and a solid understan...', 'Computer scienceFront endData modelingMISJavascriptData structuresHTMLUnit testing', 'Few Hours Ago', 'Save']


# In[107]:


df = pd.DataFrame(new_data)
df.columns = ['Job Title', 'Company', 'Rating', 'Reviews', 'Experience', 'Salary', 'Location', 'Job Description', 'Skills', 'Posted', 'Save']

df


# In[108]:


df.replace('?',np.nan, inplace = True)


# In[110]:


df


# In[113]:


df.isna().sum()


# In[125]:


#write your code inside main function
def  main(st):
  a = int(input())
  b = int(input())
  
main();

