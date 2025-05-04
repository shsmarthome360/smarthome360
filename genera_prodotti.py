import pandas as pd
import os

INPUT_CSV = "products.csv"
OUTPUT_CSV = "prodotti_completo.csv"

def process_products():
    if not os.path.exists(INPUT_CSV):
        print(f"File non trovato: {INPUT_CSV}")
        return

    df = pd.read_csv(INPUT_CSV)

    required_columns = ["SKU", "Titolo", "Descrizione", "Prezzo", "Categoria", "URL_Immagine"]
    for col in required_columns:
        if col not in df.columns:
            print(f"Colonna mancante: {col}")
            return

    # Pulisce i dati e salva un nuovo CSV
    df["Prezzo"] = df["Prezzo"].astype(float).round(2)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"File generato: {OUTPUT_CSV}")

if __name__ == "__main__":
    process_products()
