import os
def get_key():
    b = []
    with open(os.getenv('PUIDATA')+'/api.txt','r') as f:
        x = f.read()
        b.append(x)

    return x
