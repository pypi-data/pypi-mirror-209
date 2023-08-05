# jwtools


### 构建
在项目文件夹中运行以下命令
python setup.py sdist bdist_wheel

### 上传：
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
或
python -m twine upload dist/*
按照提示，输入pypi的用户名、密码，就可以成功了。若中途提示有些库没有安装，则使用pip安装一下，需要用到twine库。