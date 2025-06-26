

def deleteline(text):
    with open("products.txt","r") as  file:
        lines=file.readlines()
        
        updatedlines=[line for line in lines if text not in line]
        
        with open("products.txt","w") as file:
            file.writelines(updatedlines)
    