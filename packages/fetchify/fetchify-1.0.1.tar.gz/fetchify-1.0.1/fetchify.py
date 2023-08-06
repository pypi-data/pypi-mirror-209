import requests

url1 = "https://raw.githubusercontent.com/Anupam1707/Python_Programmes/main/"
url2 = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/"
url3 = "https://raw.githubusercontent.com/Anupam1707/ai/main/"
url4 = "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/"
url5 = "https://raw.githubusercontent.com/Anupam1707/SecuriPy/main/"

def python(filename):
    page = requests.get(url1 + filename)
    return page.text

def weather(filename):
    page = requests.get(url2 + filename)
    return page.text

def ai(filename):
    page = requests.get(url3 + filename)
    return page.text

def food(filename):
    page = requests.get(url4 + filename)
    return page.text

def secure(filename):
    page = request.get(url + filename)
    return page.text