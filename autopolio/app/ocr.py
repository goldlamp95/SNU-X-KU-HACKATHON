from .models import *
from autopolio.settings import OCR_API_URL, OCR_SECRET_KEY
import requests
import uuid
import time
import json


def toefl_ocr(request):
  # url과 secret_key는 수정하지 말 것!
  api_url = OCR_API_URL
  secret_key = OCR_SECRET_KEY
  image_file = request.FILES['Eng_score']

  # if image_file.split('.')[-1] is not 'png':
  #   return print('file format is not matching')

  request_json = {
      'images': [
          {
              'format': 'png',
              'name': 'demo'
          }
      ],
      'requestId': str(uuid.uuid4()),
      'version': 'V2',
      'timestamp': int(round(time.time() * 1000)),
      'templateIds': 0
  }

  payload = {'message': json.dumps(request_json).encode('UTF-8')}
  files = [
    # ('file', open(image_file,'rb'))
    image_file
  ]
  headers = {
    'X-OCR-SECRET': secret_key
  }

  response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

  full_text = response.text.encode('utf8')

  result = json.loads(full_text)

  print('--------')

  a = result['images'][0]['fields']

  for i in a:
    print(i['name'] +'  '  +  i['inferText'])