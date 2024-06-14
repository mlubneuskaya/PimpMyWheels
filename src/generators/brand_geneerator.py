import pandas as pd

car_brands = [
    "Toyota", "Volkswagen", "Ford", "Skoda", "Opel", "Renault", "Peugeot", "BMW",
    "Mercedes-Benz", "Audi", "Hyundai", "Kia", "Nissan", "Fiat", "Suzuki", "Seat",
    "Honda", "Mazda", "Citroen", "Dacia", "Volvo", "Mitsubishi", "Lexus", "Subaru",
    "Porsche", "Jaguar", "Alfa Romeo", "Mini", "Land Rover", "Jeep", "Chevrolet",
    "Tesla", "Chrysler", "Dodge", "Infiniti", "Lancia", "Smart", "SsangYong", "Saab",
    "Daewoo", "Ferrari", "Maserati", "Bentley", "Lamborghini", "Rolls-Royce", "Aston Martin"
]

brands = {
    "marka": car_brands
}
df = pd.DataFrame(brands)
file_path = "data/brands.csv"
df.to_csv(file_path, index=False)
