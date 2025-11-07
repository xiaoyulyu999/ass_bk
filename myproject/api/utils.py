import json
import csv
import os
import pandas as pd

script_directory = os.path.dirname(os.path.abspath(__file__))
path_of_config = os.path.join(script_directory, "config.json")
path_of_csv = os.path.join(script_directory, "data/samples.csv")
path_of_dummy_csv = os.path.join(script_directory, "csv_files/dummy.csv")

def read_config(path_of_config):
    if not os.path.exists(path_of_config):
        raise FileNotFoundError(f"Config file does not exist: {path_of_config}")
    with open(path_of_config, "r") as read_config:
        config = json.load(read_config)
    return config

config = read_config(path_of_config)

def read_csv_columns(path_of_csv):
    with open(path_of_csv, "r") as read_csv:
        columns = csv.DictReader(read_csv).fieldnames
    return columns

def update_existing_config_headers():
    headers = df.columns.tolist()
    if headers:
        config["headers_csv"] = headers

        with open(path_of_config, "w")as write_config:
            json.dump(config, write_config, indent=4)
            print("Updating configration ... ...")
        print(config["headers_csv"])
    else:
        raise ValueError("There are no columns in the data frame.")

def get_patient_detail_by_id(patient_id):
    if not isinstance(patient_id, int):
        raise ValueError("Patient ID must be an integer.")

    patient = df[df["patient_id"] == patient_id].to_dict(orient='records')
    if patient:
        return patient[0]
    else:
        raise ValueError(f"No patient found with the given patient Id: {patient_id}")

def get_column_by_header(header):
    if header in config["headers_csv"]:
        return df[header].unique().tolist()
    else:
        raise ValueError(f"No header was found, header: {header}. Check again.")

def drop_down_select(given_list):
    drop_down_select = []
    for element in given_list:
        drop_down_select.append((element, element))
    return drop_down_select

df = pd.read_csv(path_of_csv)

if __name__ == "__main__":
    update_existing_config_headers()