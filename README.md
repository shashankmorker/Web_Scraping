 # **Web Scraping Naukri.com.**

![image](https://github.com/shashankmorker/Web_Scraping/assets/150799907/99779781-9424-416b-ad5b-16787935bdc8)


# **CONTENT:**

**1. Introduction**

**2. Python Libraries used**

**3. Work Flow**

**4. Outcome**



## **Introduction:**

**Web scraping refers to the extraction of data from a website. This information is collected and then exported into a more useful format for the user. Be it a spreadsheet or CSV file. Although web scraping can be done manually, in most cases, automated tools are preferred when scraping web data as they can be less costly and work at a faster rate. But in most cases, web scraping is not a simple task. Websites come in many shapes and forms, as a result, web scrapers vary in functionality and features.**


## **Python Libraries Used:**

**a. pandas**

**b. numpy**

**c. matplotlib.pyplot**

**d. seaborn**

**e. Import driver from seleniumBase**

**g. from bs4 import BeautifulSoup**

**h. from selenium.webdriver.common.by import By**


## **Work Flow:**

**1. Import all the required libraries.**

**2. Select the URL we want to scrape and then open it using the driver created.**

**3. Scrape the required data and start saving it in empty lists.**

**4. After checking the data frame fill the missing values with np.NaN.**

**5. Create a CSV file and save the data in it.** 

**6. Using the CSV file create a data frame and handle the missing values using fillna().**

**7. Once the data frame is ready start with visualization.**



## **Outcome:**

 **I managed to scrape all the required data like job role, location, job description, experience, etc by web scraping and creating visuals from the collected data. If you want to scrape data other than free sites seleniumBsase would be useful because beautifulsoup wont work** 





