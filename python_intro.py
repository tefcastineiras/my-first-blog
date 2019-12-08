def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hello(name):
    if name == "Hola":
        print("Hola Hola!")
    elif name== "Sonja":
        print("Hola Sonja")
    else:
        print("Hola anonimo!")

hello("Sonja")


def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

def hi(name):
    print("Hola" + name + "!")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print("Next girl")

    
