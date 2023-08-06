import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def pray(number):
    try:
        file_path = os.path.join(current_dir, "code"+str(number)+".txt")
        file = open(file_path, "r")
        file_content = file.read()
        file.close()
        return file_content
    except:
        return "Madarchod number toh yaad krke aata!!"
    
print(pray(1))