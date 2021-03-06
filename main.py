import requests
from PIL import Image
import io
import os
import urllib
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


API_KEY = '2226989cc0f7cbd0f912d245c31efe74'
API_SECRET = '9f47605a5743e11b'



response = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=cd7062a3a8758f4c0bf0a9d963de498a&tags=dog&accuracy=100&per_page=1&format=json&nojsoncallback=1&auth_token=72157718534083926-21b452c6b460c0e3&api_sig=33d93dbb66dca6cb3e62d2b6c763c26d')
#print(request.json())

photo = response.json()['photos']['photo'][0]
print(photo)

server = photo['server']
photo_id = photo['id']
photo_secret = photo['secret']

url = f'https://live.staticflickr.com/{server}/{photo_id}_{photo_secret}.jpg'

image_file = urllib.request.urlretrieve(url, "dog-of-the-day.jpg")
SENDER_EMAIL = 'shepard.garrison.t@gmail.com'
RECIP_EMAIL = 'marinshepard210@gmail.com'
PASSWORD = 'Gt$092894'
SUBJECT = 'Dog Of The Day (BY GOOSE)'
def send_mail(file_name):
    img_data = open(file_name, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIP_EMAIL
    #msg['Subject'] = 'Dog of The Day'
    #msg['From'] = SENDER_EMAIL
    #msg['To'] = RECIP_EMAIL
    #text = MIMEText("This Dog Photo Was Sent From A Goose Program!")
    #msg.attach(text)
    #image = MIMEImage(img_data, name=os.path.basename(file_name))
    #msg.attach(image)
    #msg = 'Why,Oh why!'
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
        server.sendmail(SENDER_EMAIL, [RECIP_EMAIL], msg.as_string())
        server.close()
    except Exception as e:
    
        print(e)

send_mail("dog-of-the-day.jpg")

    #url = f'https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg'
#requests.download('')
#photo_repsonse = requests.get(url)
#print(photo_repsonse.)

#i = Image.open(io.BytesIO(photo_repsonse.content))
