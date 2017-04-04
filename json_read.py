import json
import collections
import chardet

def get_popular_words(file,encoding):
 d = collections.defaultdict(int)
 with open(file, encoding= encoding) as json_content:
  data_file = json.load(json_content)
  if file != 'newsit.json':
   for key, value in data_file.items():
    for c in value['channel']['item']:
     for i in c['description']['__cdata'].split(" "):
       if len(i) > 6:
        d[i] += 1
       else:
        continue
  else:
    for value in data_file['rss']['channel']['item']:
     for i in value['description'].split(" "):
      if len(i) > 6:
        d[i] += 1
      else:
         continue
 top_10 = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]
 return top_10



def main():
 list_file = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
 for file in list_file:
  rawdata = open(file, 'rb').read()
  result = chardet.detect(rawdata)
  top_10= get_popular_words(file,result['encoding'])
  print('\n10 самых часто употребляемых слов из файла ',file,': ', top_10,'\n')
main()