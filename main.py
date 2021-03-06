import requests
from PIL import Image
import io
import os
import urllib
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


SITE_KEY = os.environ.get('SITE_KEY')
SITE_SEC = os.environ.get('SITE_SEC')
SITE_AUTH =  os.environ.get('SITE_AUTH')

SENDER_EMAIL = 'shepard.garrison.t@gmail.com'
RECIP_EMAIL = 'marinshepard210@gmail.com'
RECIP_EMAIL_COW = 'ourrosiegirl3@gmail.com'
GOOSE_IT = 'garrisontshepard@gmail.com'
PASSWORD = 'Gt$092894'
SUBJECT = 'Dog Of The Day (BY GOOSE)'
FILE_NAME =  "dog-of-the-day.jpg"

def get_image():
    response = requests.get(f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={SITE_KEY}&tags=dog&accuracy=100&per_page=1&format=json&nojsoncallback=1&auth_token={SITE_AUTH}&api_sig={SITE_SEC}')
    photo = response.json()['photos']['photo'][0]
   
    server = photo['server']
    photo_id = photo['id']
    photo_secret = photo['secret']

    url = f'https://live.staticflickr.com/{server}/{photo_id}_{photo_secret}.jpg'
    image_file = urllib.request.urlretrieve(url, FILE_NAME)


def prepare_and_send_mail(file_name):
    img_data = open(file_name, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = GOOSE_IT
  
    text = 'this email was sent from a goose program'
    msg.attach(MIMEText(text, "plain"))
    #text = MIMEText("test")
    image = MIMEImage(img_data, name=os.path.basename(file_name))
    image.add_header('Content-Disposition','attachment',filename=file_name)
    msg.attach(image)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, [GOOSE_IT], msg.as_string())
        server.close()
    except Exception as e:
    
        print(e)

def photo_of_the_day():
    prepare_and_send_mail(FILE_NAME)
    time.sleep(86400)

get_image()
prepare_and_send_mail(FILE_NAME)
#while True:
    #photo_of_the_day()
#url = f'https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg'
#requests.download('')
#photo_repsonse = requests.get(url)
#print(photo_repsonse.)

#i = Image.open(io.BytesIO(photo_repsonse.content))
