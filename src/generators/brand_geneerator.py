import pandas as pd

import pandas as pd

# Dane samochodów z przykładowymi cenami

marka = ["Toyota"] * 10 + ["Volkswagen"] * 10 + ["Ford"] * 10
model = [
        "Corolla", "Camry", "RAV4", "Yaris", "Aygo",
        "Auris", "C-HR", "Highlander", "Land Cruiser", "Supra",
        "Golf", "Passat", "Tiguan", "Polo", "Arteon", 
        "T-Roc", "Touran", "Touareg", "ID.4", "ID.3",
        "Focus", "Mondeo", "Kuga", "Puma", "Fiesta", 
        "S-Max", "Galaxy", "Mustang", "Ranger", "Explorer"
    ]
cena = [
        90000, 130000, 110000, 75000, 50000, 
        95000, 115000, 200000, 300000, 250000,
        95000, 140000, 130000, 80000, 160000, 
        110000, 120000, 250000, 180000, 170000,
        85000, 120000, 130000, 90000, 60000, 
        140000, 150000, 270000, 160000, 250000
    ]

brands = {"marka": marka, "model": model, "cena": cena}
df = pd.DataFrame(brands)
file_path = "data/brands.csv"
df.to_csv(file_path, index=False)
