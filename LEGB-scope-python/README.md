## Scope in python

### Built-in Variable
- python本身內置的變量或方法

### Global Variables 全局變量
- 以下範例會報錯: 因為函式中不存在x變量，若在局域中操作應該先全局聲明
	```python
	x = "global"
	def foo():
	    # TODO: global x
	    x = x * 2
	    print(x)
	foo()
	```
	```
	UnboundLocalError: local variable 'x' referenced before assignment
	```

### Local Variables 局域變量
- 以下範例會報錯: 因為局域變量作用域僅在局域
	```python
	def foo():
	    # TODO: global y here
	    y = "local"
	    # TODO: print y here
	foo()
	print(y)
	```
	```
	NameError: name 'y' is not defined
	```

### Nonlocal Variables 非局域變量
- 非局域變量常用於嵌套函式(閉包)，作用域不在局域也不在全局時會使用，會去上層找變量
	```python
	def make_handler():
	    sequence = 0
	    def handler(result):
	        nonlocal sequence
	        sequence += 1
	        print("[{}] Got: {}".format(sequence, result))
	    return handler
	```
