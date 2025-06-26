

def productviews():
    with open("products.txt","r") as file:
        data=file.read()
        return data