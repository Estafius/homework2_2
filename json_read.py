import json

with open('newsafr.json', encoding='utf-8') as newsafr:
 data_newsafr = json.load(newsafr)
 dictlist_newsafr = []
 for key, value in data_newsafr.items():
    temp = [key,value]
    dictlist_newsafr.append(temp)

with open('newscy.json', encoding='utf-8') as newscy:
 data_newscy = json.load(newscy)
 dictlist_newscy = []
 for key, value in data_newscy.items():
    temp = [key,value]
    dictlist_newscy.append(temp)
    
with open('newsfr.json', encoding='utf-8') as newsfr:
 data_newsfr = json.load(newsfr)
 dictlist_newsfr = []
 for key, value in data_newsfr.items():
    temp = [key,value]
    dictlist_newsfr.append(temp)
    
    
with open('newsit.json', encoding='utf-8') as newsit:
 data_newsit = json.load(newsit)
 dictlist_newsit = []
 for key, value in data_newsit.items():
    temp = [key,value]
    dictlist_newsit.append(temp)
    
print(dictlist_newsafr,'\n\n\n',dictlist_newscy, '\n\n\n', dictlist_newsfr,'\n\n\n', dictlist_newsit)

