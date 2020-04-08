#!/usr/bin/env python
# coding: utf-8

# # Web Scrapping - Case_Internshala.
# <p>Prepared by: <a href = 'https://github.com/sagsshakya'>Sagun Shakya</a></p>
# - GITAM Institute of Science.

# #### Imporing the necessary libraries.

# In[2]:


import requests
from bs4 import BeautifulSoup as BS


# In[3]:


url = 'https://internshala.com/internships/work-from-home-data%20science-jobs'
page = requests.get(url)
soup = BS(page.text, 'html.parser')

print(soup.prettify())


# In[4]:


company_class = soup.find_all(class_ = 'company')

print(company_class[0])
print('----------------------------------------')
print(company_class[0].h4.a.text)
print('----------------------------------------')


# ## Getting the Fields list.

# In[5]:


fields_list = [company_class[ii].h4.a.text for ii in range(len(company_class))]
print(len(fields_list))
print('---------------------')
print(fields_list)


# <hr><hr>

# ## Getting the company list.

# In[6]:


company = soup.find_all(class_ = 'link_display_like_text')
company_list = [company[ii].text for ii in range(len(company))]
company_list[:5]


# #### Cleaning process.

# In[8]:


for ii in range(len(company_list)):
    company_list[ii] = company_list[ii].replace('\n','')
company_list[:5]


# #### Removing the extraspaces at the front and the back of the string.

# In[9]:


for ii in range(len(company_list)):
    company_list[ii] = company_list[ii].replace('                        ','')
for ii in range(len(company_list)):
    company_list[ii] = company_list[ii].replace('                    ','')
company_list[:5]


# <hr><hr>

# ## Testing the above results in a dataframe. 

# In[10]:


import pandas as pd
pd.DataFrame({'Companies':company_list, 
             'Fields': fields_list})


# ## Getting the internship description.

# In[11]:


x = soup.find_all(class_ = 'table-responsive')
print(x[0])
print('------------------')
print(x[1])


# #### Putting all the data into lists.

# In[13]:


start_date_list = []
duration_list = []
stipend_list = []
posted_on_list = []
apply_by_list = []

x = soup.find_all(class_ = 'table-responsive')
for ii in range(len(x)):
    details = x[ii].find_all('td')
    
    start_date_list.append(details[0].text)
    duration_list.append(details[1].text)
    stipend_list.append(details[2].text)
    posted_on_list.append(details[3].text)
    apply_by_list.append(details[4].text)


# ## Cleaning the data one by one.

# #### Cleaning start_date_list.

# In[15]:


start_date_list[:5]


# In[16]:


for ii in range(len(start_date_list)):
    start_date_list[ii] = start_date_list[ii].replace('\n','')
start_date_list[:10]


# #### Cleaning duration_list.

# In[17]:


duration_list[:5]


# In[18]:


for ii in range(len(duration_list)):
    duration_list[ii] = duration_list[ii].replace('\n','')
    duration_list[ii] = duration_list[ii].replace('                                ','')
    duration_list[ii] = duration_list[ii].replace('                            ','')
    
duration_list[:5]


# #### Cleaning stipend_list.

# In[19]:


stipend_list[:5]


# In[20]:


for ii in range(len(stipend_list)):
    stipend_list[ii] = stipend_list[ii].replace('                            ','')
    stipend_list[ii] = stipend_list[ii].replace('\n','')
    #duration_list[ii] = duration_list[ii].replace('                            ','')
    
stipend_list[:5]


# ## Converting our data into a dataframe and exporting them into a .csv file.

# In[21]:


import pandas as pd
import os
os.chdir(r'C:\Users\acer\Desktop\PythonProgramming')


# In[22]:


df = pd.DataFrame()

df['Companies'] = company_list 
df['Fields'] =  fields_list
df['Start Date'] = start_date_list
df['Duration'] = duration_list
df['Stipend'] = stipend_list
df['Posted On'] = posted_on_list 
df['Apply By'] = apply_by_list 
df.head(10)


# ### Exporting into .csv file.

# In[24]:


df.to_csv('internshala.csv', index = False)


# # The End.
