import datetime

r"""
This is a datetime example python script 
"""

filename=datetime.datetime.now()

def create_file():
    """This function create an empty file"""
    with open(filename.strftime('%Y%b%d'), "w") as file:
        file.write("") #writting empty string

create_file()