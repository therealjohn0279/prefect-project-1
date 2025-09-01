from python_devcontainer_template.greet.greeter import Greeter

if __name__ == "__main__":
    greeter = Greeter()
    greeter.greet()
    print(greeter)
    print(repr(greeter))
