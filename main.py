from src.data_loader import load_patient_data


data = load_patient_data("data/patients.csv")

print("Clinical Patient Dataset")
print("------------------------")
print(data.head())