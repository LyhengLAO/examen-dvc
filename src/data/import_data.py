import requests
import os

data_path = './data/raw/'
url = 'https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv'

def import_data():
    responses = requests.get(url)
    name = os.path.basename(url)
    print(responses.text[:20])

    os.makedirs(data_path, exist_ok = True)
    if responses.status_code == 200:
        content = responses.text
        with open(os.path.join(data_path,name),'wb') as f:
            f.write(content.encode('utf-8'))
        print('import success')
    else:
        print('an error occure')

if __name__ == '__main__':
    import_data()