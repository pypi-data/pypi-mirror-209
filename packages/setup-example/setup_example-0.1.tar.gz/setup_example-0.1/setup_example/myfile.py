import requests
import numpy as np

def myfunction():
    r = requests.get('https://www.google.com')
    print(r.status_code)
    print(np.random.rand())
