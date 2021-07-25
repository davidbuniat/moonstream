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
    uri = './data/v5' # put s3 link here
    uri = "s3://internal-datasets/bugout/ethereum/v2"
    if False:
        sample = get_sample('./ethereum.json')
        ds = create_dataset(sample, uri)
        with ds:
            for s in tqdm([sample]*100000): # 1.2B
                for k,v in s.items():
                    ds[k].append(v)

    ds = hub.Dataset(uri)

    for el in tqdm(ds):
        el.gas.numpy()
        # el.to.numpy() # error in reading string
        # el['from'].numpy()
        # el.hash.numpy()
        # el.value.numpy()
        # el.input.numpy()
        el.gasPrice.numpy()
        # print(el.gas.numpy())
