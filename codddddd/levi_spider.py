import re
import time
import requests
from lxml import etree

url = 'https://www.levi.com.cn/products?categoryId=%E6%96%B0%E5%93%81'
url1 = 'https://www.levi.com.cn/api/graphql'
session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}
res = session.get(url=url, headers=headers)

storeCode = re.findall('"storeCode":"(.*)","picPrefix":"https:', res.text)[0]
tenantCode = re.findall('"tenantCode":"(.*)","cnWapUrl"', res.text)[0]
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    'Host': 'www.levi.com.cn',
    'Origin': 'https://www.levi.com.cn',
    'Referer': 'https://www.levi.com.cn/products?categoryId=%E6%96%B0%E5%93%81',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'UNEX-STORE-CODE': storeCode,
    'UNEX-TENANT-CODE': tenantCode,
    # 'UNEX-USER-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc1Zpc2l0b3IiOnRydWUsInVzZXJOYW1lIjoiVmlzaXRvciIsImV4cCI6MTYwMjQ4OTQ5MCwidXNlckNvZGUiOiI5OTIwMDkxMjAwMDAxMTgxIn0.mnRdRhAQxlXtxEHgqNOblvbeKU9dTxP7pvEC_H8BofQ'

}

from_data = {

}
# session.get(url='http://uia.whxy.edu.cn/cas/signout/logoutFull?service=http://59.172.226.5:80/eams/login.action')
# time.sleep(3)


# print(storeCode, '----')
# print(tenantCode)
print(res.text)

payloadData = {"operationName": "fetchProductList",
               "variables": {"filters": {"attributes": [], "categories": ["19091700000211"], "keyword": ""},
                             "sort": {"name": "LIST_TIME", "sort": "DESC"}, "first": 12},
               "query": "query fetchProductList($filters: ProductFilterInput, $sort: SortInput, $before: String, $first: Int, $after: String, $last: Int) {\n  shop {\n    products(filters: $filters, sort: $sort, before: $before, first: $first, after: $after, last: $last) {\n      maxPrice {\n        amount\n        __typename\n      }\n      minPrice {\n        amount\n        __typename\n      }\n      pageInfo {\n        hasNextPage\n        startCursor\n        endCursor\n        totalCount\n        __typename\n      }\n      options {\n        attributeType\n        code\n        name\n        values {\n          key\n          value\n          frontName\n          imageUrl\n          total\n          __typename\n        }\n        __typename\n      }\n      categories {\n        code\n        name\n        frontName\n        categoryPath\n        count\n        __typename\n      }\n      edges {\n        node {\n          ...productListDetailLiteFragment\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment productListDetailLiteFragment on Product {\n  id\n  title\n  subTitle\n  code\n  inventory\n  images {\n    url\n    __typename\n  }\n  labels {\n    code\n    frontName\n    description\n    __typename\n  }\n  attributes {\n    code\n    frontName\n    values {\n      code\n      displayName\n      attributeValue\n      url\n      frontName\n      images {\n        url\n        __typename\n      }\n      thumbnails {\n        url\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  activityPrice {\n    activityLabel\n    activityName\n    promotionPrice {\n      amount\n      currencyCode\n      __typename\n    }\n    __typename\n  }\n  listPrice {\n    currencyCode\n    amount\n    __typename\n  }\n  salePrice {\n    currencyCode\n    amount\n    __typename\n  }\n  options {\n    ...productOptionFragment\n    __typename\n  }\n  __typename\n}\n\nfragment productOptionFragment on ProductOption {\n  code\n  frontName\n  values {\n    code\n    displayName\n    url\n    frontName\n    images {\n      url\n      images {\n        url\n        __typename\n      }\n      __typename\n    }\n    thumbnails {\n      url\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n",
"variables": {"filters": {"attributes": [], "categories": ["19091700000211"], "keyword": ""}}
"filters": {"attributes": [], "categories": ["19091700000211"], "keyword": ""}
    "attributes": []
    "categories": ["19091700000211"]
    "keyword": ""
    "first": 12
"sort": {"name": "LIST_TIME", "sort": "DESC"}
"name": "LIST_TIME"
"sort": "DESC"
               }


"variables": {"filters": {"attributes": [], "categories": ["19091700000211"], "keyword": ""}}
"filters": {"attributes": [], "categories": ["19091700000211"], "keyword": ""}
"attributes": []
"categories": ["19091700000211"]
"keyword": ""
"first": 12
"sort": {"name": "LIST_TIME", "sort": "DESC"}
"name": "LIST_TIME"
"sort": "DESC"