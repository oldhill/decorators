# Define some decorators

def hello(f):
  def prepend_hello():
    return 'hello, %s ' % f() 
  return prepend_hello

def whatup(f):
  def prepend_whatup():
    return 'whatup? %s ' % f() 
  return prepend_whatup

# Apply decorators to a function. Decorators are applied bottom-to-top:
# 'In Python, @g @f def foo() translates to foo=g(f(foo).' - PEP318

@hello
@whatup
def say_goodbye():
  return 'goodbye!'

# Go

print say_goodbye()

# Without decorator syntax

def say_later():
  return 'later!'

say_later = hello(whatup(say_later))

print say_later()

# TODOs 
# (1) read these:
# http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python
# http://www.jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/
