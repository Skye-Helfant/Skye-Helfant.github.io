# PixelPlus Network Information Data
#### Video Demo:  <URL HERE>
#### Description:
My project is a website which displays network information concerning servers under the jurisdiction of the Web 2.0 company PixelPlus.

#### Overview:


#### Step 1:
I need to collect the server data. I use a *url* and *API KEY* to access the data. I use *requests*, a python library which assists in *HTTP requests*, to collect the data in a variable.
The data is currently in JSON format. To make the data easier to work with I use the built-in json library in python to convert the json data to a dictionary. I use the *pprint* module
to format this dictionary into a *human-friendly reading* format. I then write this data into two files, temp_key_values.txt, and data.txt. data.txt contains all the server data in
easily readable dictionary form. temp_key_values.txt contains the key values for each respective drive. The combination of these two files makes it easier to understand what information
is actually contained in the data.

#### Step 2:
I need to output the extracted data to a website. In order to accomplish this I use a combination of html, css, and bootstrap. Since my website is relatively simple I decide it only needs
one homepage. This page is formatted using html in the file index.html. I use css and boostrap to stylize my page