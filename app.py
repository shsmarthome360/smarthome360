from flask import Flask, render_template, request, url_for
import csv
import os

app = Flask(__name__, static_folder='static')

def load_products():
    file_path = "products.csv"
    if not os.path.exists(file_path):
        return []
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

@app.route("/anteprima-prodotti")
def anteprima_prodotti():
    categoria = request.args.get("category", "").strip().lower()
    products = load_products()
    for p in products:
        p.setdefault("category", "")
        p.setdefault("image_url", "")
        p.setdefault("sku", "")
        p.setdefault("name", "")
        p.setdefault("stock", "0")
        p.setdefault("price", "0")

    categorie = sorted({p["category"] for p in products if p["category"]})
    filtered = [p for p in products if p["image_url"] and (not categoria or categoria in p["category"].lower())]

    return render_template("anteprima_prodotti.html", products=filtered, categorie=categorie, categoria=categoria)

@app.route("/product-detail/<sku>")
def product_detail(sku):
    products = load_products()
    for p in products:
        p.setdefault("sku", "")
        p.setdefault("category", "")
        p.setdefault("image_url", "")
        p.setdefault("name", "")
        p.setdefault("stock", "0")
        p.setdefault("price", "0")

    categorie = sorted({p["category"] for p in products if p["category"]})
    prod = next((p for p in products if p["sku"] == sku), None)
    
    if not prod:
        return "Prodotto non trovato", 404

    return render_template("product_detail.html", product=prod, categorie=categorie, categoria=prod.get("category", ""))

if __name__ == "__main__":
    app.run(debug=True)
