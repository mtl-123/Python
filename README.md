# 项目目录

[Web Flask 开发项目](./web_framework/flask_proj/)

[Python 项目管理工具](./Management_tools.md)

[包管理工具](./packaging_tools.mm.md)



# faker

- faker是一个python包可以轻松生成工作中常用的数据，比如伪造文本、伪造信用卡号、地址、电话等
- pip install faker
[faker官方文档](https://faker.readthedocs.io/en/master/)

```python
from faker import Faker
fake = Faker()

print(fake.profile())
print(fake.credit_card_number())
```

# 快速创建项目的方法

https://zhuanlan.zhihu.com/p/101544546
