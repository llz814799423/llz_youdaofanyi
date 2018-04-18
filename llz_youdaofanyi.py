import urllib.request
import urllib.parse
import json

while True:
    content = input('请输入需要翻译的内容：')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1517293642982'
    data['sign'] = '98e456f6f70df9688b44f40de98f9913'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('UTF-8')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('UTF-8')
    target = json.loads(html)
    print('结果是:%s' % (target['translateResult'][0][0]['tgt']))
    print()
    # print(html)
    # print(target)
