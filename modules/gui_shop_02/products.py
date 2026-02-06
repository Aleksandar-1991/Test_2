import json
import tkinter as tk
from helpers import clean_screen
from canvas import app
import os
from PIL import Image, ImageTk


base_folder = os.path.dirname(__file__)
path = os.path.join("modules", "gui_shop_02", "db")

def update_current_user(username, product_id):
    with open(os.path.join(path, "users.txt"), "r+") as file:
        users = [json.loads(user.strip()) for user in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(user) + "\n" for user in users])
                return

def purchase_product(product_id):
    with open(os.path.join(path, "products.txt"), "r+") as file:
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
    with open(os.path.join(path, "current_user.txt"), "r") as file:
        username = file.read()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)

    render_product_screen()

def render_product_screen():
    clean_screen()

    with open(os.path.join(path, "products.txt"), "r") as file:
        products = [json.loads(p.strip()) for p in file]
        rows_for_product = len(products[0])
        products_per_row = 6
        for index, product in enumerate(products):
            row = index // products_per_row * rows_for_product
            col = index % products_per_row

            tk.Label(app, text=product["name"]).grid(row= row, column=col)

            img = Image.open(os.path.join(path, "images", product["img_path"])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(app, image=photo_image)
            image_label.image = photo_image
            image_label.grid(row= row+1, column=col)

            tk.Label(app, text=product["count"]).grid(row= row + 2, column=col)
            tk.Button(app, text=f"Buy {product["id"]}", command= lambda p = product["id"]: buy_products(p)).grid(row= row + 3, column=col)




