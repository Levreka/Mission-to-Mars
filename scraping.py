#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 


# In[2]:


# Set up Splinter excutable path 
executable_path = { 'executable_path' : ChromeDriverManager().install()}
#setting browser to chrome
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# ##review this comments for explanation on above code
# 
# With the following line, browser.is_element_present_by_css('div.list_text', wait_time=1), we are accomplishing two things.
# 
# One is that we're searching for elements with a specific combination of tag (div) and attribute (list_text). As an example, ul.item_list would be found in HTML as <ul class="item_list">.
# 
# Secondly, we're also telling our browser to wait one second before searching for components. The optional delay is useful because sometimes dynamic pages take a little while to load, especially if they are image-heavy.

# In[4]:


#set up html parser 
html = browser.html
news_soup = soup(html, 'html.parser')
#create a variable that will hold everything located in the div element
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


#call the slide_elem variable to further fileter through the data using .find the most recent
#title the first parameter is div the class if not sure use inspect on web page to 
#view 
slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text if your not sure the class name
#use inspect on the element withing the div and look for the class name
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button the indexation lets the code know
#which button element we want to click or extract if there is more than one
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# We've done a lot with that single line.
# 
# Let's break it down:
# 
# An img tag is nested within this HTML, so we've included it.
# .get('src') pulls the link to the image.
# 
# this is alaso important since if we were just to pull the image link with out this code everytime the web page would be updated we would manually have to update the source(src) link to it this automatizes it 
# 

# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[14]:


#using pandas to bring table in galaxyfacts-mars.com instead of scrapping each row 
#for data

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# This comments are for the above code and how it is working
# 
# df = pd.read_htmldf = pd.read_html('https://galaxyfacts-mars.com')[0] With this line, we're creating a new DataFrame from the HTML table. The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list. Then, it turns the table into a DataFrame.
# 
# df.columns=['description', 'Mars', 'Earth'] Here, we assign columns to the new DataFrame for additional clarity.
# 
# df.set_index('description', inplace=True) By using the .set_index() function, we're turning the Description column into the DataFrame's index. inplace=True means that the updated index will remain in place, without having to reassign the DataFrame to a new variable.

# In[15]:


#turning the table back into html using .to_html() pandas
df.to_html()


# In[16]:


browser.quit()


# In[ ]:




