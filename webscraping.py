import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.oichub.org/")

print(response.text)
