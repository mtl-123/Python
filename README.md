
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
