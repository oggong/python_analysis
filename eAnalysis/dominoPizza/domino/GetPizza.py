from bs4 import BeautifulSoup
from urllib import request as req
from urllib import parse

from MenuList import Menu

# 1. 데이타 가져오기
import MySQLdb  # MySQLdb 설정

# db 연결
conn = MySQLdb.connect(host='192.168.0.59', user='scott', passwd='tiger', db='pythondb')

conn.set_character_set('utf-8')

cur = conn.cursor()

sql = "INSERT INTO menu "

#도미노 피자 base_url
base_url = 'https://web.dominos.co.kr/goods/'

#메뉴 리스트 page 반복문.
for k in ['C0102','C0201','C0202','C0203']:
    print("=="*50)
    html = req.urlopen('https://web.dominos.co.kr/goods/list?dsp_ctgr={0}'.format(k))

    soup = BeautifulSoup(html,'html.parser')
    #print(soup)

    #메뉴 이미지 리스트 가져오기
    img = soup.select('.prd_img_view img')


    #메뉴가 피자인경우,Large/medium price

    if k == 'C0102':
        price_L = soup.select('.price_large')
        price_M = soup.select('.price_medium')

    # 메뉴가 피자가 아닌 경우,사이즈 구분없음
    else:
        price = soup.select('.price_num')

    #print(btn_Url)



    # 메뉴명과 이미지 경로
    for j,i in enumerate(img):
        title = i.attrs['alt']
        img = i.attrs['src']

        #이미지 경로로 다운받아서 저장.
        imgName = './{0}/{1}.jpg'.format(k,j)
        req.urlretrieve(img,imgName)
        # 피자인 경우, 사이즈별 가격정보를 list로.
        if k == 'C0102':
            price_l=price_L[j].text
            price_m = price_M[j].text
            price = [price_l, price_m]
            print(title, img, price)


        else:
            price_side = price[j].text
            print(title, img, price_side)




        # 피자 / 사이드메뉴인 경우, 상세설명 가져오기
        if k in ['C0102', 'C0201']:
            btn_Url = soup.select('.btn_detail')
            #href 경로 가져와서 url parcing, 해당 내용 가져오기.
            btn_url = btn_Url[j].attrs['href']
            detail_url = parse.urljoin(base_url, btn_url)
            res_det = req.urlopen(detail_url)
            soup1 = BeautifulSoup(res_det,'html.parser')
            detail = soup1.select_one('.detail_view_info').text

            #공백제거
            print(detail.strip())

        print("*"*50)


