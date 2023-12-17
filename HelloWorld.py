class HelloWorld:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"Hello {self.name}"

hello = HelloWorld("Sutham")
print("Hello", hello.name)
print(hello)
