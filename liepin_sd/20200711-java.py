import urllib.request as r
import json
from lxml.html import etree
import xlwt
import time
import re
job_info={}
        #with open('20200711-II.json','w',encoding='utf-8') as f:
f=open("20200711-II.json",'w',encoding='utf-8')
headers={
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        }
localtime=time.asctime(time.localtime(time.time()))
for i in range(0,9):
    url='https://www.liepin.com/zhaopin/?compkind=&dqs=250&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=java&siTag=k_cloHQj_hyIn0SLM9IfRg%7EE08QNgJtmOV680BaDaEpHQ&d_sfrom=search_sub_site&d_ckId=dd76a316c51f1293138fe7dedd804143&d_curPage='+str(i+1)+'&d_pageSize=40&d_headId=1a799268763593806c00b1d94a01eeb8&curPage='+str(i)
    response=r.Request(url=url,headers=headers)
    data=r.urlopen(response).read().decode("utf-8")
    data1=etree.HTML(data)
    
    for j in range(40):
        #data2=data1.xpath("//div[@class='job-info']//a[@target='_blank']/@href".format(j))
        #print(data2)
        #for I in data2:
        job_title = data1.xpath("//div[@class='job-info']/h3/a/text()")[j]
        try:
            job_title_url=data1.xpath("//div[@class='company-info nohover']/p//a[@target='_blank']/@href")[j]
        except:
            job_title_url=[]
        job_company = data1.xpath("//div[@class='company-info nohover']/p/a/text()")[j]
        try:
            job_company_url = data1.xpath("//div[@class='company-info nohover']/p//a[@target='_blank']/@href")[j]
        except:
            job_company_url = []
        try:
            job_address = data1.xpath("//div[@class='job-info']/p/a/text()")[j]
        except:
            job_address
        job_salary = data1.xpath("//div[@class='job-info']/p/span/text()")[j]
        job_href = data1.xpath("//div[@class='job-info']/p/time/text()")[j]
        a=''.join(job_salary)
        b=re.findall(r"\d+\.?\d*",a)

        job_info['job_sourse']="5"
        job_info['job_title']=str(job_title)
        if len(job_title_url)==0:
            job_info['job_url']=[]
        else:
            job_info['job_url']=str(job_title_url)
        job_info['job_company']=str(job_company)
        if len(job_company_url)==0:
            job_info['job_company_url']=[]
        else:
            job_info['job_company_url']=str(job_company_url)
        job_info['job_location']=str(job_address)
        job_info['job_salary']=job_salary
        if len(b)>1:
            job_info['job_max_salary']=eval(b[1])*1000
            job_info['job_min_salary']=eval(b[0])*1000
        else:
            job_info['job_max_salary']=[]
            job_info['job_min_salary']=[]
        job_info['job_release_data']=job_href
        job_info['job_collect_data']=localtime

        print(job_info)

        json.dump(job_info,f,ensure_ascii=False)
        print("finish")
