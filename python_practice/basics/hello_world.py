

class HelloWorld:
    
    def __init__(self):
        self.name = None

    def greet(self, name):
        self.name = name
        return f"hello {name}"


hello = HelloWorld()
print(hello.greet("World"))
