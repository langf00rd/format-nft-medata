import json
import os

index = 0
current_path = os.path.abspath(os.getcwd()+'/metadata')
files =  os.listdir(current_path)
sorted_files = sorted(files)

if('.DS_Store' in files):
    files.remove('.DS_Store')

for file in sorted_files:
    index += 1
    print(file, index)

    with open(os.path.join(current_path, file), 'r+') as f:
        data = json.load(f)
        data['image'] = 'https://ipfs.infura.io/ipfs/1234/' + str(index) + '.jpg'
        data['id'] = index
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
