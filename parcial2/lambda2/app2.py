from bs4 import BeautifulSoup
import time
import boto3
import requests
import pandas as pd

def handler(event, context):
    s3 = boto3.resource('s3')
    localtime=time.localtime()
    paginaBBC = s3.Object('scrapingnewspaper', 'headlines/raw/periodico=BBC/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.html')
    paginaCNN = s3.Object('scrapingnewspaper', 'headlines/raw/periodico=CNN/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.html')
    file_contentBBC = paginaBBC.get()['Body'].read()
    file_contentCNN = paginaCNN.get()['Body'].read()
    dfBBC = scrapingBBC(file_contentBBC)
    dfCNN = scrapingCNN(file_contentCNN)

    put(dfBBC,"BBC",s3)
    put(dfCNN,"CNN",s3)

def put(df,periodico,s3):
    csv= df.to_csv(index = False)
    localtime=time.localtime()
    s3object = s3.Object('resultsnewspaper','news/final/periodico='+periodico+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/noticias.csv')
    s3object.put(
    Body = csv
    )
    
    

def scrapingBBC(text):
    soup = BeautifulSoup(text, 'html.parser')
    losDiv = soup.find_all("body")
    losLi = losDiv[0].find_all("li")

    losAA=[]
    for li in losLi:
        losA = li.find_all("a")
        losAA.append(losA)
    href=[]
    nomCate =[]
    for hr in losAA:
        href.append("https://www.bbc.com"+hr[0].get("href"))
        nomCate.append(hr[0].getText())

    #Categorias

    hrefPrin=[]
    nomCatePr =[]
    for i in range(1,12):
        hrefPrin.append(href[i])
        nomCatePr.append(nomCate[i])
    # Extracion de los links de cada pagina
    rr=[]
    for i in hrefPrin:
        rr.append(requests.get(i))
    
    categorias = []

    for r in rr:
        page=[]

        soup = BeautifulSoup(r.text, 'html.parser')
        losDiv = soup.find_all("body")
        losLi = losDiv[0].find_all("li")

        for li in losLi:
            losA = li.find_all("a")
            page.append(losA)
        categorias.append(page)

    cat0 = categorias[0]
    cat1 = categorias[1]
    cat2 = categorias[2]
    cat3 = categorias[3]
    cat4 = categorias[4]
    cat5 = categorias[5]

    titulos = []
    categoriasgen=[]
    links=[]

    for i in range(41,90):
        if cat0 [i] :
            if  (cat0 [i][0].getText()) != " Lee m??s sobre estos v??nculos":
                tit1=(cat0 [i][0].getText())
                titulos.append(tit1)
            if cat0 [i][0].get("href") != "https://www.bbc.co.uk/usingthebbc/terms/can-i-share-things-from-the-bbc":
                link =("https://www.bbc.com"+cat0 [i][0].get("href"))
                links.append(link)
                categoriasgen.append("America-Latina")

    for i in range(41,90):
        if cat1 [i] :
            if  (cat1 [i][0].getText()) != " Lee m??s sobre estos v??nculos":
                tit1 = cat1 [i][0].getText()
                titulos.append(tit1)
            if cat1 [i][0].get("href") != "https://www.bbc.co.uk/usingthebbc/terms/can-i-share-things-from-the-bbc":
                link=("https://www.bbc.com"+cat1 [i][0].get("href"))
                links.append(link)
                categoriasgen.append("Internacional")

    for i in range(28,len(cat2)-7):
        if cat2[i]:
            tit1 = cat2[i][0].getText()
            titulos.append(tit1)
            link = ("https://www.bbc.com"+cat2[i][0].get("href")) 
            links.append(link)
            categoriasgen.append("Medio Ambiente")

    for i in range(41,90):
        if cat3 [i] :
            if  (cat3 [i][0].getText()) != " Lee m??s sobre estos v??nculos":
                tit1=(cat3 [i][0].getText() )
                titulos.append(tit1)
            if cat3 [i][0].get("href") != "https://www.bbc.co.uk/usingthebbc/terms/can-i-share-things-from-the-bbc":
                link=("https://www.bbc.com"+cat0 [i][0].get("href"))
                links.append(link)
                categoriasgen.append("Coronavirus")

    for i in range(28,len(cat4)-7):
        if cat4[i]:
            tit1 =(cat4[i][0].getText())
            titulos.append(tit1)
            link =("https://www.bbc.com"+cat4[i][0].get("href")) 
            links.append(link)
            categoriasgen.append("Hay Festival")

    for i in range(41,90):
        if cat5 [i] :
            if  (cat5 [i][0].getText()) != " Lee m??s sobre estos v??nculos":
                tit1 = cat5 [i][0].getText()
                titulos.append(tit1)
            if cat5 [i][0].get("href") != "https://www.bbc.co.uk/usingthebbc/terms/can-i-share-things-from-the-bbc":
                link=("https://www.bbc.com"+cat5 [i][0].get("href"))
                links.append(link)
                categoriasgen.append("Economia")


    noticiasgen=[]
    for noticias in zip(titulos,categoriasgen,links):
        noticiasgen.append([noticias[0],noticias[1],noticias[2]])
    
    df = pd.DataFrame.from_records(noticiasgen,
                               columns=['Titulo','Categoria', 'Link'])
    return df

def scrapingCNN(text):
    soup = BeautifulSoup(text, 'html.parser')
    losDiv = soup.find_all("body")
    articles = losDiv[0].find_all("article")
    links=[]
    titulos=[]
    category=[]
    noticias=[]

    for article in articles:
        news = article.find("div",{'class':'news__data'})
        noticias.append(news)


    for noticia in noticias:
        cat = noticia.find("span",{'class':'news__label'})
        title = noticia.find("h2",{'class':'news__title'})
        if cat:
            cat1 = cat.find("a")
            tit1 = title.find("a")
            category.append(cat1.get("title"))
            titulos.append(tit1.get("title"))
            links.append(tit1.get("href"))

    noticiasgen=[]

    for noticias in zip(titulos,category,links):
        noticiasgen.append([noticias[0],noticias[1],noticias[2]])
    
    df = pd.DataFrame.from_records(noticiasgen,
                               columns=['Titulo','Categoria', 'Link'])

    return df
