# coding: utf-8
import requests

class BuTian:

    def __init__(self,page):
        self.page = page if int(page) > 0 else 1
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
            "X-Requested-With":"XMLHttpRequest"
        }

    def butianBugpage(self):
        response = requests.get("http://loudong.360.cn/Loo/index/p/{}.html".format(self.page),headers=self.headers)
        titles = []
        for i in response.json().get("list"):
            update_time, company_name, title, level_360 = i.get("update_time"), i.get("company_name"),i.get("title2"),i.get("level_360")
            # appear = u"{update_time}  公司名称:{company} | 漏洞名称: {title},漏洞等级: {level}".format(
            #     update_time=update_time,
            #     company=company_name,
            #     title=title,
            #     level=level_360,
            # )
            # print appear
            appear = {"title":title,"company_name":company_name, "level":level_360, "update_time": update_time}
            titles.append(appear)
        return titles

    def butianSearch(self, keyword):
        response = requests.get("http://butian.360.cn/Loo/index/search/{keyword}/p/{page}.html".format(keyword=keyword, page=self.page), headers=self.headers)
        titles = []
        for i in response.json().get("list"):
            update_time, company_name, title, level_360 = i.get("update_time"), i.get("company_name"), i.get("title2"), i.get("level_360")
            appear = {"title": title, "company_name": company_name, "level": level_360, "update_time": update_time}
            titles.append(appear)
        return titles
# for i in BuTian(1).butianBugpage():
#     print i