import json


filepath = "abc.json"

with open(filepath, "r", encoding="utf-8")as f:
    abc = json.load(f)


_a_ = abc["a"]
_b_ = abc["b"]
_c_ = abc["c"]
_one_ = abc["1"]


print(_a_)
print(_b_)
print(_c_)
print(_one_)
print(type(_one_))

