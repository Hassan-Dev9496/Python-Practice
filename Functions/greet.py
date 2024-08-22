def greet(name = None , full = ""):
    if(name):
       print("Hello " + name + full)
    else:
        print("Hello Default " + full )

greet("" , "hassan")