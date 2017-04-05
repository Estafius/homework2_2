import json
import collections
import chardet


def get_popular_words(file, encoding):
 d = collections.defaultdict(int)
 with open(file, encoding=encoding) as json_content:
  data_file = json.load(json_content)
  for i in data_file['rss']['channel']['item']:
     if isinstance(i['description'], str):
      description = i['description']
     else:
      description = i['description']['__cdata']
     for i in description.split(" "):
       if len(i) > 6:
         d[i] += 1
       else:
        continue
  top_10 = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]
  return top_10


def main():
 list_file = ['newsafr.json', 'newscy.json', 'newsit.json', 'newsfr.json']
 for file in list_file:
  rawdata = open(file, 'rb').read()
  result = chardet.detect(rawdata)
  top_10 = get_popular_words(file, result['encoding'])
  print('\n10 самых часто употребляемых слов из файла ', file, ': ', top_10, '\n')
main()
