# Downloading Datasets via API 

The CKAN API utilizes http request to download datasets. This is okay for smaller datasets but slow and inefficient for larger datasets.

There are two examples provided that shows how to download multiple datsets utilzing the API. 


#### Example 1
This examples shows how to download datasets that have a specific tag. You can run this with the following: 
```
python search_tags.py <tag> <api_key>
```

where you would replace <tag> with a tag of your choosing and <api_key> with a valid API key. 

#### Example 2 

This examples shows how to download datasets based off of a key work (or metatdata).  You can run this with the following: 
```
python metadata_search <key_word> <api_key>
```

where you would replace <key_word> with a key word of your choosing and <api_key> with a valid API key. 
