# user:zjw pass:jjjj
python3 manage.py createsuperuser

python3 manage.py makemigrations testModel  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate testModel   # 创建表结构
