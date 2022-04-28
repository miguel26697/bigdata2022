import boto3
import requests
import time

def handler(event, context):
    
    rBBC = requests.get('https://www.bbc.com/mundo')
    rCNN = requests.get('https://cnnespanol.cnn.com/')
    
    put(rBBC,"BBC")
    put(rCNN,"CNN")
    

def put(r,periodico):
    localtime=time.localtime()
    print("Creating temporaly file...")
    file="/tmp/pagina.html"
    f = open(file,"w")
    print("Saving file from BBC")
    f.write(r.text)
    f.close()

    s3 = boto3.resource('s3')
    data={
        'file':file,
        'bucket': 'scrapingnewspaper',
        'path':('headlines/raw/periodico='+periodico+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.html')
    }

    s3.meta.client.upload_file(data['file'],data['bucket'] ,data['path'])

