#!/usr/bin/env python
# coding: utf-8

# In[34]:


import instaloader

#gets instance of instaloader
L = instaloader.Instaloader()


# In[35]:


#Creates class for mapping posts
class geoPosts:
    def __init__(self, username, url, description, location):
        self.username = username
        self.url = url
        self.description = description
        self.location = location
       # self.description = description
    
    def getUsername(self):
        return self.username
    def getURL(self):
        return self.url
    def getDescription(self):
        return self.description
    def getLocation(self):
        return self.location
    
    


# In[23]:


locationList = []
posts = L.get_hashtag_posts("materialmelttest")
postInfo = []

for post in posts:
    #filters out posts missing geotags
    if hasattr(post.location,'name'):
        try:
            #for testing purposes
            print(post.owner_username)
        
            #creates new geoPost object that stores information about post
            postInfo.append(geoPosts(post.owner_username, post.url, post.caption, post.location.name))

           # locationList.append(post.location.name)
        except AttributeError:
            print("breaking")
            #break


# In[33]:



for x in range(0,len(postInfo)):
    print(("%i.")%(x+1))
    print(postInfo[x].getUsername())
    print(postInfo[x].getURL())
    print(postInfo[x].getDescription())
    print(postInfo[x].getLocation())


# In[ ]:




