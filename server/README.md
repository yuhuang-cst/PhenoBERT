# run phenobert locally

Since gcc7 is needed when installing fasttext, it should be updated if the version is too low:
```shell
sudo yum install centos-release-scl
sudo yum install devtoolset-7-gcc*
scl enable devtoolset-7 bash # or: source scl_source enable devtoolset-7
gcc -v
```

Env config:

```shell
conda create -n phenobert python=3.7
conda activate phenobert
pip install -r requirements.txt
export PYTHONPATH=`pwd`/phenobert/utils:$PYTHONPATH
```

Download nltk resource:

```shell
python py_pre_download.py
```

Go into work dir:
```
cd PhenoBERT/phenobert/utils
```

Try running python command:
```python
from api import annotate_text
print(annotate_text("I have a headache"))
```

## bug solve
### GLIBCXX not found
fasttext bug：

```
ImportError: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found
```
Solution：

```shell
strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX
yum provides libstdc++.so.6
cd /usr/local/lib64
wget http://www.vuln.cn/wp-content/uploads/2019/08/libstdc.so_.6.0.26.zip
unzip libstdc.so_.6.0.26.zip
ls ls -l /usr/lib64 | grep libstdc++ # should make sure there is no file with the same name before copy
cp libstdc++.so.6.0.26 /usr/lib64
cd  /usr/lib64
mv libstdc++.so.6 libstdc++.so.6_old
ln -s libstdc++.so.6.0.26 libstdc++.so.6
strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX # If GLIBCXX_3.4.20 exists, the bug is fixed
```

Reference：
- [https://blog.csdn.net/m0_54218917/article/details/120113221](https://blog.csdn.net/m0_54218917/article/details/120113221)

# Test server locally
Server: 

```shell
export PYTHONPATH=`pwd`/phenobert/utils:`pwd`/server:$PYTHONPATH
pip install -r server/requirements.txt
cd phenobert/utils
python3 ../../server/server/service.py
```

Client: 

```shell
cd server
python3 server/test_service.py
```

# Build server image
```shell
mv PhenoBERT/server/ . # Take out the server in advance
cd server # Go to dir where Dockerfile is located; 

# Build image (since docker can only contain things in the current directory, temporarily move other code packages in and out)
mv ../PhenoBERT .
docker build --network=host -t phenobert:v20230722 ./
mv ./PhenoBERT ../

# Try to run container
docker container run --rm -p 8085:8085 phenobert:v20230722
python server/test_service.py # In anather terminal

# Put server back
cd .. && mv server PhenoBERT
```

## debug in container
```shell
# Run container in the background：
docker run -itd --entrypoint /bin/bash -p 8085:8085 --name phenobert phenobert:v20230722
# Go into the container
docker exec -it phenobert bash
```

# Image export and import
```shell
# Export image tar
docker save [imageID] -o ./phenobert.tar

# Import image tar
docker load -i phenobert.tar
docker tag [imageID] phenobert:v20230722 # re-tag
```

# Running service
```shell
docker container run --rm -d -p 8085:8085 phenobert:v20230722
```
