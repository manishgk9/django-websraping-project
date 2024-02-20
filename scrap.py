import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=vivo&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


Product_name = []
Price = []
Description = []
Reviews = []
Image_urls = []


def scrap(phoneName):
    fnp = "https://www.flipkart.com/search?q=vivo&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
        str(1)

    fnps = f"https://www.flipkart.com/search?q={phoneName}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
        str(1)
    rq = requests.get(fnps)
    data = rq.text
    soap = BeautifulSoup(data, "lxml")
    box = soap.find("div", class_="_1YokD2 _2GoDe3")
    names = box.find_all("div", class_="_4rR01T")

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    descriptions = box.find_all("ul", class_="_1xgFaf")
    reviews = box.find_all('div', class_="_3LWZlK")
    image_urls = box.find_all('img', class_="_396cs4")
    source_url = box.find_all('a', class_="_1fQZEK")
    data_dict = {}

    for name, price, desc, rew, url, source in zip(names, prices, descriptions, reviews, image_urls, source_url):
        product_info = {
            'Product_name': name.text,
            'Price': price.text,
            'Description': desc.text,
            'Reviews': rew.text,
            'Image_url': url.get('src'),
            'source': "https://www.flipkart.com"+source.get('href')
        }
        data_dict[name.text] = product_info

    print(data_dict)
    # Accessing data from the dictionary
    for url in source_url:
        print(url.get('href'))


scrap("vivo T2 5G (Velocity Wave, 128 GB)  (6 GB RAM)")


# def scraping(search):
#     url = "https://www.amazon.in/s?k=" + search + \
#         "&crid=2I1EQN7W8VDRD&sprefix=o%2Caps%2C847&ref=nb_sb_noss_2"
#     rq = requests.get(url)
#     print(rq)
#     soap = BeautifulSoup(rq.text, 'lxml')
#     name = soap.find(
#         'span', class_='a-size-medium a-color-base a-text-normal')
#     price = soap.find('span', class_="a-price-whole")
#     print(name.text)
#     print(price.text)

#  <!-- <a href="{% url 'detailpage' %}"> -->
# scraping('SAMSUNG Galaxy F13 (Nightsky Green, 64 GB)')
# def trainding():
#     rq = requests.get(
#         "https://www.flipkart.com/search?q=tending&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
#     # print(rq)
#     soap = BeautifulSoup(rq.text, 'lxml')
#     box = soap.find('div', class_="_1YokD2 _3Mn1Gg")

#     title = box.find_all('a', class_="s1Q9rs")
#     price = box.find_all('div', class_="_30jeq3")
#     ratings = box.find_all('div', class_="_3LWZlK")
#     imgs = box.find_all('img', class_="_396cs4")
#     product_data = {}
#     for name, price, rating, img in zip(title, price, ratings, imgs):
#         # print(name.text, price.text, rating.text, img.get('src'))
#         product_info = {
#             'product name': name.text,
#             'price': price.text,
#             'rating': rating.text,
#             'url': img.get('src'),
#         }
#         product_data[name.text] = product_info

#     print(product_data)


# trainding()
