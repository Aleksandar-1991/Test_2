from helpers import clean_screen
import os
import json
import tkinter as tk
from canvas import app
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)

def update_current_user(username, product_id):
    with open(os.path.join(base_folder, "db", "users.txt"), "r+") as file:
        users = [json.loads(u.strip()) for u in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(u) + "\n" for u in users]) ## writelines
                return

def purchase_product(product_id):
    with open(os.path.join(base_folder, "db", "products.txt"), "r+") as file:
        products = [json.loads(product.strip()) for product in file]
        products = [p for p in products if p["count"] > 0]
        for prod in products:
            if prod["id"] == product_id:
                prod["count"] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(p) + "\n" for p in products])
                return

def buy_products(product_id):
    with open(os.path.join(base_folder, "db", "current_user.txt"), "r") as file:
        username = file.read()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)

    render_products_screen()


def render_products_screen():
    clean_screen()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    with open(os.path.join("modules", "gui_shop",  "db", "products.txt"), "r") as file:
        products = [json.loads(p.strip()) for p in file]
        rows_for_product = len(products[0])
        products_per_row = 6
        for index, product in enumerate(products):
            row = index // products_per_row * rows_for_product
            col = index % products_per_row

            tk.Label(app, text=product["name"]).grid(row = row, column= col)


            img = Image.open(os.path.join(base_folder, "db", "images", product["img_path"])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(app, image=photo_image)
            image_label.image = photo_image
            image_label.grid(row= row + 1, column=col)

            tk.Label(app, text= product["count"]).grid(row= row + 2, column=col)
            tk.Button(app, text=f"Buy {product["id"]}", command= lambda p=product["id"]: buy_products(p)).grid(row= row + 3, column=col)