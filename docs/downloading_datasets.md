# Downloading Datasets via API 

The CKAN API can be utilized to search for relevant key words. It returns all details related to the resource, including the exact URL. In the two provided examples, we utilize `wget` to download queried datasets. 

### Example 1
This examples shows how to download datasets that have a specific tag. If a queried dataset has a URL, it is printed in a text file that is named after the tag. 

You can run this with the following: 
```
python search_tags.py <tag> <api_key>
```

where you would replace <tag> with a tag of your choosing and <api_key> with a valid API key. 

### Example 2 

This examples shows how to download datasets based off of a key work (or metatdata). If a queried dataset has a URL, it is printed in a text file that is named after the key word. 

You can run this with the following: 
```
python search_metadata.py <key_word> <api_key>
```

where you would replace <key_word> with a key word of your choosing and <api_key> with a valid API key. 
