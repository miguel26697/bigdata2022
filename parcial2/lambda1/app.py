import boto3
import requests
import time

def handler(event, context):
    localtime=time.localtime()
    rBBC = requests.get('https://www.bbc.com/mundo')
    rCNN = requests.get('https://cnnespanol.cnn.com/')
    
    
    print("Creating temporaly file...")
    fileBBC="/tmp/BBC.html"
    f = open(fileBBC,"w")
    print("Saving file from BBC")
    f.write(rBBC.text)
    f.close()

    print("Creating temporaly file...")
    fileCNN="/tmp/CNN.html"
    f = open(fileCNN,"w")
    print("Saving file from BBC")
    f.write(rCNN.text)
    f.close()

    s3 = boto3.resource('s3')
    data={
        'file':fileBBC,
        'bucket': 'scrapingnewspaper',
        'path':('headlines/raw/periodico=BBC/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.html')
    }

    s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])

    data2={
        'file':fileCNN,
        'bucket': 'scrapingnewspaper',
        'path':('headlines/raw/periodico=CNN/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/pagina.html')
    }

    s3.meta.client.upload_file(data2['file'],data2['bucket'] ,data2['path'])
