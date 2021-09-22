#!/usr/bin/env python
# coding: utf-8

# In[ ]:


capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
capitals


# In[ ]:





# In[ ]:


type(capitals)


# In[ ]:


capitals.get("India")


# In[ ]:


capitals["India"]


# In[ ]:


capitals["goa"] = "panji"


# In[ ]:


capitals


# In[ ]:


capitals.pop("goa")


# In[ ]:


capitals


# In[ ]:


del capitals["USA"]


# In[ ]:


capitals


# In[ ]:


capitals.clear()


# In[ ]:


capitals


# In[ ]:


capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}


# In[ ]:


CAPITALS = capitals.copy()


# In[ ]:


CAPITALS


# In[ ]:


child1 = {"name": "kiran", "father":"ramesh"}


# In[ ]:


child1["name"]


# In[ ]:


child2 = {"name": "ram", "father":"siva"}


# In[ ]:


child2


# In[ ]:


family = {"child1" :{"name": "kiran", "father":"ramesh"},"child2":{"name": "ram", "father":"siva"}}


# In[ ]:


myfamily = {
  "child1" : {
    "name" : "John",
    "year" : 1995,
    "hobbies":["Music","Cricket","TV"]
  },
  "child2" : {
    "name" : "Sammy",
    "year" : 2001
  }
}
myfamily


# In[ ]:


myfamily["child2"]["name"]


# In[ ]:



dict1 = { 
   "april_batch":{ "student":{ "name":"Mike","marks":{ "python":80,"maths":70
            
            
         
         
      
         }
      }
   }
}


# In[ ]:


dict1["april_batch"]["student"]["name"]


# In[ ]:


dict1["april_batch"]["student"]["marks"]


# In[ ]:


dict1["april_batch"]["student"]["marks"]["python"]


# In[ ]:





# In[ ]:




