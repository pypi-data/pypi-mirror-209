import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def pray(number):
    file_path = os.path.join(current_dir, "code"+str(number)+".txt")
    file = open(file_path, "r")
    file_content = file.read()
    file.close()
    return file_content    
print(pray(1))