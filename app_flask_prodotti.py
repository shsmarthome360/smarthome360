from flask import Flask, render_template_string, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(UPLOAD_FOLDER, "products.csv")
            file.save(filepath)
            return redirect(url_for("preview_products"))
    return render_template_string("""
<!DOCTYPE html>
<html lang="it">
<head><meta charset="UTF-8"><title>Upload CSV</title></head>
<body style="background-color:#111;color:#eee;font-family:sans-serif;text-align:center;">
<h2>Carica il file products.csv</h2>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file" accept=".csv">
    <input type="submit" value="Carica">
</form>
</body>
</html>
""")

@app.route("/preview")
def preview_products():
    filepath = os.path.join(UPLOAD_FOLDER, "products.csv")
    if not os.path.exists(filepath):
        return "Nessun file CSV caricato."

    df = pd.read_csv(filepath)
    if not {"SKU", "Titolo", "Prezzo", "URL_Immagine"}.issubset(df.columns):
        return "Il CSV non contiene le colonne richieste."

    df["Prezzo"] = df["Prezzo"].astype(float).round(2)
    html_rows = ""
    for _, row in df.iterrows():
        html_rows += f"<tr><td>{row['SKU']}</td><td>{row['Titolo']}</td><td>€ {row['Prezzo']}</td><td><img src='{row['URL_Immagine']}' width='100'></td></tr>"

    html_template = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head><meta charset="UTF-8"><title>Anteprima Prodotti</title></head>
    <body style="background-color:#111;color:#eee;font-family:sans-serif;">
    <h1>Anteprima Prodotti Caricati</h1>
    <table border="1" cellpadding="10" style="width:100%;border-collapse:collapse;">
    <tr><th>SKU</th><th>Prodotto</th><th>Prezzo</th><th>Immagine</th></tr>
    {html_rows}
    </table>
    <br><form action="/genera" method="post"><button type="submit">Genera prodotti_completo.csv</button></form>
    </body>
    </html>
    """
    return html_template

@app.route("/genera", methods=["POST"])
def genera_prodotti():
    filepath = os.path.join(UPLOAD_FOLDER, "products.csv")
    if not os.path.exists(filepath):
        return "Nessun file CSV caricato."

    df = pd.read_csv(filepath)
    df["Prezzo"] = df["Prezzo"].astype(float).round(2)
    output_path = os.path.join(UPLOAD_FOLDER, "prodotti_completo.csv")
    df.to_csv(output_path, index=False, encoding="utf-8")
    return f"File <strong>prodotti_completo.csv</strong> generato correttamente in {UPLOAD_FOLDER}."

if __name__ == "__main__":
    app.run(debug=True)
