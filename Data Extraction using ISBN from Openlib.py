# Data Extraction using ISBN from Openlibrary


from pickle import TRUE
import string
import urllib
import json

from requests import request
import requests
from sqlalchemy import alias
from yaml import AliasEvent


link ="http://openlibrary.org/api/books?bibkeys=ISBN:0735222355&jscmd=details&format=json"
f = requests.get(link)

arr = json.loads(f.text)
arr= arr.values()
print(arr)
isbn_10 =""
isbn_13 =""
# bookname =arr['ISBN:0735222355']['details']['title']
# bookauthor =arr['ISBN:0735222355']['details']['authors'][0]['name']
# imgurl = arr['ISBN:0735222355']['thumbnail_url']
# bookpublisher =arr['ISBN:0735222355']['details']['publishers'][0]
# print(arr['ISBN:0735222355']['info_url'])
# print(arr['ISBN:0735222355']['preview_url'])
# print(arr['ISBN:0735222355']['thumbnail_url'])
# print(bookname)
# print(bookauthor)
# print(bookpublisher)
  #  {'ISBN:0735222355': {'bib_key': 'ISBN:0735222355', 'info_url': 'http://openlibrary.org/books/OL31970802M/The_Lincoln_Highway', 'preview': 'noview', 'preview_url': 'http://openlibrary.org/books/OL31970802M/The_Lincoln_Highway', 'thumbnail_url': 'https://covers.openlibrary.org/b/id/10648601-S.jpg', 'details': {'type': {'key': '/type/edition'}, 'title': 'The Lincoln Highway', 'authors': [{'key': '/authors/OL7018678A', 'name': 'Amor Towles'}], 'publish_date': 'Oct 05, 2021', 'source_records': ['amazon:0735222355', 'bwb:9780735222359'], 'number_of_pages': 416, 'publishers': ['Viking'], 'isbn_10': ['0735222355'], 'isbn_13': ['9780735222359'], 'physical_format': 'hardcover', 'full_title': 'The Lincoln Highway A Novel', 'subtitle': 'A Novel', 'notes': {'type': '/type/text', 'value': 'Source title: The Lincoln Highway: A Novel'}, 'covers': [10648601], 'works': [{'key': '/works/OL24205227W'}], 'key': '/books/OL31970802M', 'lc_classifications': ['PS3620.O945L56 2021'], 'latest_revision': 2, 'revision': 2, 'created': {'type': '/type/datetime', 'value': '2021-02-18T15:46:35.965325'}, 'last_modified': {'type': '/type/datetime', 'value': '2021-09-30T22:02:05.212784'}}}}