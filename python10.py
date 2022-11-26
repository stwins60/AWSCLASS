# import sqlite3 as sql


# conn = sql.connect("users.db")


# def create_users_table():
#     try:
#         conn.execute("DROP TABLE IF EXISTS users")
#         print("Table dropped successfully")
#         query = '''
#         CREATE TABLE IF NOT EXISTS users(
#             userID integer NOT NULL,
#             username text NOT NULL,
#             password text NOT NULL,
#             PRIMARY KEY(userID)
#         );

#         '''
#         conn.execute(query)
#         conn.commit()
#         print("Table created successfully")
#     except Exception as e:
#         print("Error while creating table", e)

# def insert_user(username, password):
#     try:
#         query = '''
#         INSERT INTO users(username, password)
#         VALUES(?, ?);
#         '''
#         conn.execute(query, (username, password))
#         conn.commit()
#         print("User inserted successfully")
#     except Exception as e:
#         print("Error while inserting user", e)


# user_list = [
#     ("user1", "pass1"),
#     ("user", "pass"),
#     ('admin', 'admin'),
#     ("admin", "password")
# ]

# create_users_table()
# for user in user_list:
#     insert_user(user[0], user[1])

import mysql.connector as mysql

conn = mysql.connect(
    host="",
    user="",
    password="",
    database=""
)



import requests as req
from bs4 import BeautifulSoup as bs


headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-us,en;q=0.5",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
    "Keep-Alive": "300",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
items = ["iphone", "stove"]
for item in items:

    url = "https://www.amazon.com/s?k=iphone"

    response = req.get(url, headers=headers)

    soup = bs(response.content, "html.parser")

    data = soup.find_all("div", {"data-component-type": "s-search-result"})

    # # find next page
    # next_page = soup.find("li", {"class": "a-last"})
    # next_page_url = next_page.find("a")["href"]

    # get all the data


    cursor = conn.cursor()

    # cursor.execute("DROP TABLE IF EXISTS amazon_laptops")

    # query = '''
    # CREATE TABLE IF NOT EXISTS amazon_laptops(
    #     title text NOT NULL,
    #     price text NOT NULL,
    #     rating text NOT NULL
    # );
    # '''

    # cursor.execute(query)  

    # cursor.execute("INSERT INTO amazon_laptops(title, price) VALUES(%s, %s)", (title, price))



    # for item in data:
    #     title = item.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).text
    #     price = item.find("span", {"class": "a-offscreen"}).text
    #     print(title, price)

    # cursor = conn.cursor()

    # cursor.execute("DROP TABLE IF EXISTS amazon_laptops")

    # query = '''
    # CREATE TABLE IF NOT EXISTS amazon_laptops(
    #     title text NOT NULL,
    #     price text NOT NULL
    # );
    # '''

    # cursor.execute(query)

    # for item in data:
    #     title = item.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).text
    #     price = item.find("span", {"class": "a-offscreen"}).text
    #     cursor.execute("INSERT INTO amazon_laptops(title, price) VALUES(%s, %s)", (title, price))
    # print("Data inserted successfully")

    # conn.commit()

    for item in data:
        # get the title
        title = item.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
        if title:
            title = title.text
        else:
            title = "No title"
        # get the price
        price = item.find("span", {"class": "a-offscreen"})
        if price:
            price = price.text
        else:
            price = "No price"
        # get the rating
        rating = item.find("span", {"class": "a-icon-alt"})
        if rating:
            rating = rating.text
            print(rating)
        else:
            rating = "No rating"
            print(rating)
        # get the number of reviews
        reviews = item.find("span", {"class": "a-size-base"})
        if reviews:
            reviews = reviews.text
            print(reviews)
        else:
            reviews = "No reviews"
            print(reviews)
        # get the image url
        image = item.find("img", {"class": "s-image"})
        if image:
            image = image["src"]
            print(image)
        else:
            image = "No image"
            print(image)
        # get the product url
        product_url = item.find("a", {"class": "a-link-normal a-text-normal"})
        if product_url:
            product_url = "https://www.amazon.com" + product_url["href"]
            print(product_url)
        else:
            product_url = "No product url"
            print(product_url)
        
        cursor.execute("INSERT INTO amazon_laptops(title, price, rating) VALUES(%s, %s, %s)", (title, price, rating))
        conn.commit()

    cursor.close()

    conn.close()


