# EV Battery Cost Index & Sensitivity Analysis Dashboard

## 📌 Project Overview
Questo progetto nasce per analizzare l'impatto della volatilità delle materie prime sui margini di produzione dei veicoli elettrici (EV). 
La dashboard permette di simulare scenari dinamici di costo basati sul prezzo in tempo reale di metalli industriali ed energia, normalizzati per il rischio di cambio.

## 🚀 Key Features
- **ETL Pipeline (Python):** Estrazione dati automatizzata tramite `yfinance` per Rame, Alluminio, Litio (ETF) e Petrolio.
- **FX Normalization:** Conversione automatica dei prezzi da USD/CNY a EUR per un'analisi coerente con il mercato europeo.
- **DAX Modeling:** Implementazione di una "Base 100 Dinamica" (Dynamic Re-basing) che permette di confrontare asset con magnitudini diverse partendo da un punto zero selezionabile dall'utente.
- **What-If Analysis:** Parametri interattivi per modificare il peso percentuale delle materie prime nella distinta base (BOM) della batteria.

## 🛠️ Tech Stack
- **Python:** Pandas, YFinance (Data Extraction & Cleaning).
- **Power BI:** DAX (Advanced Modeling), Power Query.
- **Financial Analysis:** Portafoglio pesato, Normalizzazione Base 100, Sensibilità dei costi.

## 📊 Dashboard Preview

---
*Progetto realizzato per dimostrare competenze end-to-end in Data Analytics applicata al settore Automotive/Finance.*
<img width="1767" height="738" alt="image" src="https://github.com/user-attachments/assets/55fe79ef-c6cd-4aab-842b-19da9604f43c" />
