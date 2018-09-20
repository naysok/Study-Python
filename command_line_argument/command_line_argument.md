# command_line_argument.md  



コマンドライン引数、python 実行時に渡す引数  
ファイル自体がゼロ番目の引数??  

```python
import sys

args = sys.argv

print(args)
print("length :" +len(args))
print(args[0])
print("第1引数：" + args[1])
print("第2引数：" + args[2])
print("第3引数：" + args[3])



"""
$ python3 test.py Hello world "Hello Python"

['test.py', 'Hello', 'world', 'Hello Python']
length : 4
'test.py'
第1引数：Hello
第2引数：world
第3引数：Hello Python
"""
```


### Ref.  

Python: コマンドライン引数とは？（超基礎）(Qiita)  
[https://qiita.com/orange_u/items/3f0fb6044fd5ee2c3a37](https://qiita.com/orange_u/items/3f0fb6044fd5ee2c3a37)  



