import yfinance as yf
import pandas as pd

print("🚀 Avvio Pipeline ETL Macroeconomica Definitiva...")

# 1. Definiamo i Tickers
tickers = {
    'EUR_USD': 'EURUSD=X',   
    'EUR_CNY': 'EURCNY=X',   
    'Alluminio_USD': 'ALI=F',
    'Rame_USD': 'HG=F',      
    'Petrolio_WTI': 'CL=F',  
    'Inflazione_10Y': '^TNX',
    'Litio_ETF': 'LIT'       
}

# Estrazione Dati
data = yf.download(list(tickers.values()), start="2019-01-01", interval="1d")['Close']
data.columns = [list(tickers.keys())[list(tickers.values()).index(col)] for col in data.columns]
df = data.ffill().dropna()

# 2. Valori Assoluti (I prezzi veri in Euro)
df['Alluminio_EUR'] = df['Alluminio_USD'] / df['EUR_USD']
df['Rame_EUR'] = df['Rame_USD'] / df['EUR_USD']
df['Petrolio_EUR'] = df['Petrolio_WTI'] / df['EUR_USD']
df['Litio_EUR'] = df['Litio_ETF'] / df['EUR_USD'] 

# 3. Il nostro Modello Finanziario (Valore assoluto)
df['Indice_Costo_EV_EUR'] = (
    (df['Rame_EUR'] * 0.4) + 
    (df['Alluminio_EUR'] * 0.2) + 
    (df['Litio_EUR'] * 0.2) + 
    (df['Petrolio_EUR'] * 0.2)
)

# 4. NORMALIZZAZIONE (Base 100 per TUTTO)
# Inseriamo in questa lista tutto ciò che vogliamo comparare graficamente
colonne_da_normalizzare = [
    'Alluminio_EUR', 'Rame_EUR', 'Petrolio_EUR', 'Litio_EUR', 
    'Indice_Costo_EV_EUR', 'EUR_USD', 'EUR_CNY'
]

for col in colonne_da_normalizzare:
    # Calcolo Base 100: Prezzo odierno / Prezzo del 1° Gennaio 2019 * 100
    df[f'{col}_Base100'] = (df[col] / df[col].iloc[0]) * 100

# 5. Formattazione per Power BI
df.reset_index(inplace=True)
df['Date'] = df['Date'].dt.tz_localize(None) 
df.rename(columns={'Date': 'Data'}, inplace=True)
df = df.round(2)

# Esportazione nel formato Europeo corretto (virgole per decimali)
nome_file = 'dataset_macro_automotive.csv'
df.to_csv(nome_file, index=False, sep=';', decimal=',')
print(f"✅ FATTO! Il file '{nome_file}' ora contiene i valori assoluti e Base 100 per tutti gli asset.")