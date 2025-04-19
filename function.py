def printing_function():
    print("hello Payal")

printing_function()


# arguments, perametters
def add_number(a, b):
    return a + b

sum = add_number(10,20)
print(sum)


# payal.verma@google.com
def genrate_mail(first_name, last_name, domain = "google.com"):
    print(first_name + "." + last_name + "@" +  domain)
    print(first_name, ".", last_name, "@" ,domain)
    print(f"{first_name}.{last_name}@{domain}")
    print("{name}.{name2}@{name3}".format(name=first_name, name2=last_name, name3=domain))
    # sep

genrate_mail("payal", "verma")


def sum(*a):
    print(a)
    print(*a)

# sum(1)
sum(1,2,3,4,5)

def multiply(x,y,z):
    print(x*y*z)

def muliply(**kwards):
    print(kwards)
    
muliply(z=2,y=1,x=0, t=1,e=2,d="a")