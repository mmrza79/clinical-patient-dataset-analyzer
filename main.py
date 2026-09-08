from src.data_loader import load_patient_data
from src.analysis import basic_statistics


data = load_patient_data("data/patients.csv")

print("Clinical Patient Dataset")
print("------------------------")
print(data.head())

print("\nClinical Patient Analysis")
print("------------------------")

statistics = basic_statistics(data)

for key, value in statistics.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")