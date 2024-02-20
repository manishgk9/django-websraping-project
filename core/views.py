from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.


def ElectronicPage(request, pk):
    i = 1
    data_dict = {}
    if request.method == 'GET':
        i += 1
        surl = f"https://www.flipkart.com/search?q={pk}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
            str(i)
    if request.method == 'POST':
        name = request.POST.get('search')
        if name is not None:
            surl = f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
                str(i)

    rq = requests.get(surl)
    data = rq.text
    soap = BeautifulSoup(data, "lxml")
    try:
        box = soap.find("div", class_="_1YokD2 _2GoDe3")
        names = box.find_all("div", class_="_4rR01T")

        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = box.find_all("ul", class_="_1xgFaf")
        reviews = box.find_all('div', class_="_3LWZlK")
        image_urls = box.find_all('img', class_="_396cs4")
        source_url = box.find_all('a', class_="_1fQZEK")

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
    except Exception as e:
        raise Exception(e)
    return render(request, 'product.html', {'rout': pk, 'pagename': 'Elctronic', 'data_dict': data_dict})


def home(request):
    data_dict = {}

    url = "https://www.flipkart.com/search?q=tending&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    rq = requests.get(url)
    soap = BeautifulSoup(rq.text, 'lxml')
    box = soap.find('div', class_="_1YokD2 _3Mn1Gg")

    title = box.find_all('a', class_="s1Q9rs")
    price = box.find_all('div', class_="_30jeq3")
    ratings = box.find_all('div', class_="_3LWZlK")
    imgs = box.find_all('img', class_="_396cs4")
    source_url = box.find_all('a', class_="_2rpwqI")
    product_data = {}
    for name, price, rating, img, source in zip(title, price, ratings, imgs, source_url):
        # print(name.text, price.text, rating.text, img.get('src'))
        product_info = {
            'product name': name.text,
            'price': price.text,
            'rating': rating.text,
            'url': img.get('src'),
            'source': "https://www.flipkart.com"+source.get('href')
        }
        product_data[name.text] = product_info
    if request.method == 'POST':
        sitem = request.POST.get('search')
        print(sitem)

        surl = f"https://www.flipkart.com/search?q={sitem}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
            str(1)
        rq = requests.get(surl)
        data = rq.text
        soap = BeautifulSoup(data, "lxml")
        try:
            box = soap.find("div", class_="_1YokD2 _2GoDe3")
            names = box.find_all("div", class_="_4rR01T")

            prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
            descriptions = box.find_all("ul", class_="_1xgFaf")
            reviews = box.find_all('div', class_="_3LWZlK")
            image_urls = box.find_all('img', class_="_396cs4")
            source_url = box.find_all('a', class_="_2rpwqI")

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

            render('base.html', {'data': data_dict, 'rout': sitem})
        except Exception as e:
            print("Exception Found", e)

        print(data_dict)
        print(product_data)
    return render(request, 'base.html', {'data_dict': data_dict, 'data': product_data})


def Product(request, pk):
    i = 1
    if request.method == 'GET':
        i += 1
        surl = f"https://www.flipkart.com/search?q={pk}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
            str(i)
    if request.method == 'POST':
        name = request.POST.get('search')
        if name is not None:
            surl = f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
                str(i)

    rq = requests.get(surl)
    data = rq.text
    soap = BeautifulSoup(data, "lxml")
    data_dict = {}
    try:
        box = soap.find("div", class_="_1YokD2 _2GoDe3")
        names = box.find_all("div", class_="_4rR01T")

        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = box.find_all("ul", class_="_1xgFaf")
        reviews = box.find_all('div', class_="_3LWZlK")
        image_urls = box.find_all('img', class_="_396cs4")
        source_url = box.find_all('a', class_="_1fQZEK")

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
    except Exception as e:
        print("Exception Found")

    return render(request, 'product.html', {'rout': pk, 'data_dict': data_dict})


def Smart_tv(request, pk):
    i = 1
    if request.method == 'GET':
        i += 1
        surl = f"https://www.flipkart.com/search?q={pk}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
            str(i)
    if request.method == 'POST':
        name = request.POST.get('search')
        if name is not None:
            surl = f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
                str(i)

    rq = requests.get(surl)
    data = rq.text
    soap = BeautifulSoup(data, "lxml")
    data_dict = {}
    try:
        box = soap.find("div", class_="_1YokD2 _2GoDe3")
        names = box.find_all("div", class_="_4rR01T")

        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = box.find_all("ul", class_="_1xgFaf")
        reviews = box.find_all('div', class_="_3LWZlK")
        image_urls = box.find_all('img', class_="_396cs4")
        source_url = box.find_all('a', class_="_1fQZEK")
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
    except Exception as e:
        print("Exception Found")

    return render(request, 'product.html', {'rout': pk, 'data_dict': data_dict})


def About(request):
    return render(request, 'about.html')
