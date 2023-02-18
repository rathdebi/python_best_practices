import pandas as pd
import random


def define_string_encoding(text_str,byte_encoding_flag=True):
    if len(text_str)== 0:
        raise Exception("not a valid string input!!!")
    elif type(text_str) == bytes and byte_encoding_flag:
        text_str = str(text_str,"UTF-8")
    else:
        pass
    return text_str


def dict_key_val(model_eval_dict, **key_val):
    if model_eval_dict.keys() and (model_eval_dict.keys() == key_val.keys()):
        for key, value in key_val.items():
            model_eval_dict[key] += value  # append to existing mapped key-values
    elif not key_val.keys():
        model_eval_dict.update(key_val)  # update new key-values
    else:
        raise Exception("not a proper dictionary with required (keys-values)")
    return model_eval_dict


def update_dictionary_key_values(input_dict={"name":["prem","abhilash","debi"],
                                             "domain":["healthcare","NLP R&D", "API and Model"],
                                             "address":["PUNE","BLR","CMBT"],
                                             "tenure":["2y","2y","3y"]},
                                 **key_values):
    if isinstance(input_dict, dict) and (input_dict.keys() == key_values.keys()):
        print("keys are matching-->an append operation")
        for key, value in key_values.items():
            input_dict[key] += value

    elif not input_dict.keys():
        print("no keys are matching-->an update operation")
        input_dict.update(key_values)
    else:
        raise Exception("not a dictionary with correct key values!!!")

    return input_dict



def generate_features_from_df(df):
    df = df.copy()
    for col in df.columns:
        yield col



def csv_reader_using_open_context(file_name):
    for row in open(file_name, "r"):
        yield row

def csv_reader_using_itertuples_context(file_name):
    for row in pd.read_csv(file_name).itertuples():
        yield row

def read_csv_from_parquet_file(filename):
    for row in pd.read_parquet("train.parquet",engine="fastparquet"):
        yield row



def fetch_unique_values_from_df(file_name):
    for column in pd.read_csv(file_name).columns:
        yield pd.read_csv(file_name)[column].unique().shape[0]

def reading_csv(filename,seed1=0,seed2=42):
    # TODO-check if file exists as well
    with open(filename, 'rb') as rawdata:
        rawdata.seek(seed1)
        file_encoding = rawdata.encoding # refer below
        #:::--use raw_data.encoding ascii encoding--:::#

    num_lines = sum(1 for l in open(filename))
    if num_lines > 80000:
        file_tenpercent = divmod(num_lines, 10)[0]
        size = max(file_tenpercent, 80000)
        print('             Lines: ', size)
        random.seed(seed2)
        skip_idx = random.sample(range(1, num_lines), num_lines - size)
        csv = pd.read_parquet(filename, skip_idx=skip_idx, engine="fastparquet", encoding=file_encoding,)
        #:::--use pandas read_parquet file loader with skip_idx and engine params--:::#
    else:
        csv = pd.read_csv(filename, engine="c", encoding=file_encoding)
        #:::--use pandas read_csv file loader with engine and encoding params--:::#

    return csv