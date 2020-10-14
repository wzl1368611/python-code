import requests
from lxml import etree
import time
import json
import re
url="http://lol.qq.com/data/info-heros.shtml"
uurl="http://lol.qq.com/space/index.shtml"
real_url="https://lol.qq.com/biz/hero/champion.js"
headers={
    

   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",

}
cookies={
    
   "_qpsvr_localtk": "0.8372297933069199",
   "eas_entry": "https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DazrzrkCaLCGDm94O9tGj75qoDqvUz6dYEG3wBagMxsJZ2Izjm7Kg3VGkrOlmaCPNM8uXr9gIqY%252BUuOfsoMQF5p8tjs0ryx3W6m2WN5lxmyP6LsEdiXiiZkElDopRA2Fp%252F94zYde%252BrR06qYcVuq1AK1%252BOZvgDVQpGopuOc%252F8RFbaxGwioea6s%252FmuWSSWjXN3GlExjnAHvvzxWZJiLksPYe2p%252FuBPtP2IF8l4SLpm%252BwsuNKapZh",
   "eas_sid": "L1y5N9X2b780m0C8Z5U474V0U6",
   "gpmtips_cfg": "%7B%22iSendApi%22%3A0%2C%22iShowCount%22%3A0%2C%22iOnlineCount%22%3A0%2C%22iSendOneCount%22%3A0%2C%22iShowAllCount%22%3A0%2C%22iHomeCount%22%3A0%7D",
   "IED_LOG_INFO2": "userUin%3D1793268783%26nickName%3D%2525E5%252590%2525AF%2525E8%252588%2525AA%26nickname%3D%25E5%2590%25AF%25E8%2588%25AA%26userLoginTime%3D1592700945%26logtype%3Dqq%26loginType%3Dqq%26uin%3D1793268783",
   "ied_qq": "o1793268783",
   "isActDate": "18434",
   "isHostDate": "18434",
   "isOsDate": "18434",
   "isOsSysDate": "18434",
   "lolqqcomrouteLine": "index-tool_index-page_index-page_main_search_news_a20200526astronaut",
   "LOLWebSet_AreaBindInfo_1793268783": "%257B%2522areaid%2522%253A%25221%2522%252C%2522areaname%2522%253A%2522%25E8%2589%25BE%25E6%25AC%25A7%25E5%25B0%25BC%25E4%25BA%259A%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221793268783%2522%252C%2522rolename%2522%253A%2522%25E6%25B3%25A1%25E6%25B3%25A1%25E7%25B3%2596%25E7%2588%25B1%25E4%25B8%258A%25E6%25B3%25A1%25E4%25BD%25A0%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1793268783%257C1%257C1793268783*%257C%257C%257C%257C%2525E6%2525B3%2525A1%2525E6%2525B3%2525A1%2525E7%2525B3%252596%2525E7%252588%2525B1%2525E4%2525B8%25258A%2525E6%2525B3%2525A1%2525E4%2525BD%2525A0*%257C%257C%257C1592701740%2522%252C%2522md5str%2522%253A%2522E9D71FD3902DDA2F71D45B82B1438E00%2522%252C%2522roleareaid%2522%253A%25221%2522%252C%2522sPartition%2522%253A%25221%2522%257D",
   "pgv_info": "ssid=7147013200",
   "pgv_pvi": "4868818944",
   "pgv_pvid": "7147013200",
   "pgv_si": "s3281275904",
   "psrf_access_token_expiresAt": "1600133799",
   "psrf_qqaccess_token": "CCE0E5DC69852204B562D27C6D708CC4",
   "psrf_qqopenid": "4360755883D4569AD83AE044E0AB9EB3",
   "psrf_qqrefresh_token": "6A1E071AA090531B7FA506DCD6764B72",
   "psrf_qqunionid": "AD1B0581FB95EDC11CEF79EDAF6A5D38",
   "ptcz": "42f56c93233ca5d5cbf5ee899cb61ae673087086cbf53037ac4a2b8880d9fa0e",
   "PTTactFirstTime": "1592697600000",
   "PTTosFirstTime": "1592697600000",
   "PTTosSysFirstTime": "1592697600000",
   "PTTuserFirstTime": "1592697600000",
   "ptui_loginuin": "1793268783",
   "RK": "Q66cNWk3al",
   "skey": "@0KH0Y5sJU",
   "tokenParams": "%3Fid%3D1",
   "topSearchRecord": "%u76AE%u80A4",
   "ts_last": "lol.qq.com/data/info-heros.shtml",
   "ts_uid": "7147013200",
   "uid": "872281668",
   "uin": "o1793268783",
   "uin_cookie": "o1793268783",
   "weekloop": "0-0-0-26"
}
#<a title="黑暗之女 安妮" onclick="PTTSendClick('btn,'heros1','黑暗之女安妮');" 
#href="info-defail.shtml?id=1"><img alt="黑暗之女 安妮" src="//game.gtimg.cn/images/lol/act/img/champion/Annie.png"><p>黑暗之女</p><span class="sbg"><i class="commspr commico-search"></i></span></a>
response=requests.get(real_url,headers=headers).content.decode("gb2312","ignore")
#print(response)
#print(response)
#pat=re.compile('"key":"(.*?)"')
pat2=re.compile('"id":"(.*?)"')
#"id":"Alistar"
hero_url=pat2.findall(response)

'''html=etree.HTML(response)
hero_url=html.xpath('//ul[@class=imgtextlist]/li/a/@href')
print(hero_url)'''
#('//ul[@class=imgtextlist]/li/a/@href')
#hero_title=html.xpath('//ul[@class=imgtextlist]/li/a/@title')
#('//ul[@class=imgtextlist]/li/a/@title')

for i in range(0,len(hero_url)):
    #http://lol.qq.com/data/info-defail.shtml?id=1
    #id_url="http://lol.qq.com/data/info-defail.shtml?id="+hero_url[i]
    id_url="http://lol.qq.com/biz/hero/%s.js" % hero_url[i]
    #http://lol.qq.com/biz/hero/Aatrox.js
    print(id_url)

    res2=requests.get(id_url).content.decode()
    #"id":"266000","num"
    pattern1=re.compile('"id":"(.*?)","num"')
    #res2=json.load(res22, strict=False)
    img_data=pattern1.findall(res2)
    img_data.pop(0)
    print(img_data,"===============")
    pattern2=re.compile('"data":{"id":"(.*?)"')
    name1=pattern2.findall(res2)[0]
    #"num":\d,"name":"(.*?)","chromas"
    pattern3=re.compile(r'"num":\d*,"name":"(.*?)","chromas"')
    #"name":"\u9ad8\u4e3d\u98ce\u60c5 \u963f\u72f8","chromas"
    #"name":"(.*?)","chromas"
    name1=pattern2.findall(res2)[0]
    name2=pattern3.findall(res2)
    name2.pop(0)
    print("长度为：",len(img_data),len(name2))
    #html2=etree.HTML(res2)
    #img_url=html2.xpath('//div[@class="defail-skin-bg"]/ul/li/img/@src')
    
    #http://lol.qq.com/biz/hero/Aatrox.js
    #https://game.gtimg.cn/images/lol/act/img/skin/big266000.jpg
    for x in range(0,len(img_data)):
        img_url="https://game.gtimg.cn/images/lol/act/img/skin/big"+img_data[x]+".jpg"
        print(img_url)
        data=requests.get(img_url).content
        #img_title=html2.xpath('//div[@class="defail-skin-bg"]/ul/li/@title')
        print(type(name2[x]))
        img_title=name2[x].encode('utf-8').decode('unicode_escape','ignore')
        print(img_title,"===================")
        try:
            with open(r'D:\pifu/{}.jpg'.format(img_title),"wb") as f:
                f.write(data)
        except Exception as e:
            print('报错错误，出错了！')

    time.sleep(0.5)

print('结束')


#http://lol.qq.com/data/info-defail.shtml?id=1
#http://lol.qq.com/data/info-defail.shtml?id=1
#https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg
#<li title="小红帽 安妮"><img alt="小红帽 安妮" src="https://game.gtimg.cn/images/lol/act/img/skin/big1002.jpg"></li>
#<img alt="黑暗之女" src="https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg">
#
'''('//div[@class="defail-skin-bg"]/ul/li/img/@src')
('//div[@class="defail-skin-bg"]/ul/li/@title')
'''


