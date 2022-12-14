# **Python project:**

******************************************************************************************************************************************************************* 
                                                      This repository contains python projects
******************************************************************************************************************************************************************* 

                                                                  **Python.ipynb**

**Jupyter Notebook file:** 
        Python.ipynb

**Synopsis:**
        
        Use of functions, http calls, global variables, list/dictionary traversal.
        The following python code makes a http call using requests library to weather url and gets the data in json format.
        We are using the .text attribute of response to read in strim
        It uses the json.loads() to deserialize and convert into dictionary
        We choose the dataseries key name and take it in a list known as listy. This list is comprised of dictionaries and subdictionaries.
        Iterate the listy and see if the timepoint key has the value 72.  If it is able to find then print only that key/value pairs.


**Input Used:**
        Using a http call, http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json 
        
**Tools Used:**
        Python functions, http calls, global variables, list/dictionary traversal

*******************************************************************************************************************************************************************                                                      
