import hub
import json
from tqdm import tqdm

def get_sample(source='./sample.json'):
    with open(source) as f:
        sample = json.load(f)
    return sample

def create_dataset(sample, uri='./data/v1'):
    ds = hub.Dataset(uri) # put S3 link here
    for k in sample.keys():
        ds.create_tensor(k)
    return ds

if __name__ == "__main__":
    uri = './data/v4'
    if True:
        sample = get_sample('./sample_2.json')
        ds = create_dataset(sample, uri)

        for s in tqdm([sample]*100000): 
            for k,v in s.items():
                ds[k].append(v)
    
    ds = hub.Dataset(uri)

    for el in ds.pytorch():
        print(el.gas.numpy())
