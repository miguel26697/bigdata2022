import boto3
import requests
from bs4 import BeautifulSoup
import time

def handler(event, context):
    localtime=time.localtime()
    rBBC = requests.get('https://www.bbc.com/mundo')
    soupBBC = BeautifulSoup(rBBC.text, 'html.parser')
    rCNN = requests.get('https://cnnespanol.cnn.com/')
    soupCNN = BeautifulSoup(rCNN.text, 'html.parser')


    s3 = boto3.resource('s3')
    s3object = s3.Object('scrapingnewspaper', 'BBC/headlines/raw/periodico=BBC/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.txt')
    s3object.put(
    Body=soupBBC
    )
    s3object2 = s3.Object('scrapingnewspaper', 'CNN/headlines/raw/periodico=CNN/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.txt')
    s3object2.put(
    Body=soupCNN
    )