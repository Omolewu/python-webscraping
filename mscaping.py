from bs4 import  BeautifulSoup
html= """<!doctype html>
<html lang="en">
  <head>
    <title>Title</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  </head>
  <body>
    <div class="container">
        <h2>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Id debitis sequi accusantium aspernatur magnam pariatur aliquam illo. Veritatis debitis quas, porro repudiandae laudantium, iusto fugiat corrupti officia itaque quaerat inventore.
        </h2>
        <p id="oic">OIC Hub </p>
        <div class="link">
        <a href="https://www.oichub.org/">OIC</a>
        <a href="https://www.oicfoundation.org.ng/">OIC Foundation</a>
        <p>We train create and develop</p>
    </div>
    <p>We train create and develop</p>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
"""
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# d = soup.find('body')
# d = soup.find_all('p')
# d = soup.find(class_='container')
# d = soup.find_all(class_='container')[0]
# d = soup.find(id='oic')
# d = soup.find(class_="link").find_all('a')
# d = soup.find(class_="link").parent
# d = soup.find(class_="link").next_sibling.next_sibling
d = soup.find(class_="link").find_next_sibling().get_text()
# d = soup.select(".container")
# find ddgddgdgdgd
# find_all [jsjsjssjsj, yhdydydyd, bdghdghdd]
# for link in d:
#       # print(link['href'])
#       print(link.get_text())

print(d)