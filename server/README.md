# 本地运行phenobert
由于fasttext安装编译需要gcc7，如gcc版本不够应先升级gcc：
```shell
sudo yum install centos-release-scl
sudo yum install devtoolset-7-gcc*
scl enable devtoolset-7 bash # 或 source scl_source enable devtoolset-7
gcc -v
```

环境配置：

```shell
conda create -n phenobert python=3.7 # 创建环境
conda activate phenobert # 切换环境
pip install -r requirements.txt # 安装依赖包
export PYTHONPATH=`pwd`/phenobert/utils:$PYTHONPATH
```

下载nltk资源：

```shell
python py_pre_download.py
```

进入执行目录（保证代码中的相对路径正确）：
```
cd PhenoBERT/phenobert/utils
```


试运行python命令：

```python
from api import annotate_text
print(annotate_text("I have a headache"))
```

## bug解决
### GLIBCXX not found
调用fasttext报错：

```
ImportError: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found
```
解决步骤：

```shell
strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX
yum provides libstdc++.so.6
cd /usr/local/lib64
wget http://www.vuln.cn/wp-content/uploads/2019/08/libstdc.so_.6.0.26.zip
unzip libstdc.so_.6.0.26.zip
ls ls -l /usr/lib64 | grep libstdc++ # copy 前应确认目标文件夹没有同名
cp libstdc++.so.6.0.26 /usr/lib64
cd  /usr/lib64
mv libstdc++.so.6 libstdc++.so.6_old
ln -s libstdc++.so.6.0.26 libstdc++.so.6
strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX # 存在GLIBCXX_3.4.20则表示修复成功
```

参考：
- [https://blog.csdn.net/m0_54218917/article/details/120113221](https://blog.csdn.net/m0_54218917/article/details/120113221)

# 本地测试server
服务器：

```shell
export PYTHONPATH=`pwd`/phenobert/utils:`pwd`/server:$PYTHONPATH
pip install -r server/requirements.txt
cd phenobert/utils
python3 ../../server/server/service.py
```

客户端：

```shell
cd server
python3 server/test_service.py
```

# 构建server镜像
```shell
mv PhenoBERT/server/ . # 提前把server拿出来
cd server # Dockerfile所在目录; 

# 生成镜像（由于docker只能包含当前目录的东西，暂时把其他代码包移进来再移出去）
mv ../PhenoBERT .
docker build --network=host -t phenobert:v20230722 ./
mv ./PhenoBERT ../

# 镜像试运行
docker container run --rm -p 8085:8085 phenobert:v20230722
python server/test_service.py # 在另一个窗口

# 把server放回去
cd .. && mv server PhenoBERT
```

## 镜像运行debug
```shell
# 后台运行容器：
docker run -itd --entrypoint /bin/bash -p 8085:8085 --name phenobert phenobert:v20230722
# 进入容器
docker exec -it phenobert bash
```

# 镜像导入导出
```shell
# 导出
docker save [imageID] -o ./phenobert.tar

# 导入
docker load -i phenobert.tar
docker tag [imageID] phenobert:v20230722 # 重新打tag
```

# 镜像部署
```shell
docker container run --rm -d -p 8085:8085 phenobert:v20230722
```
