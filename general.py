
def file_to_set(file_name):
    result = set()
    with open(file_name, 'r') as file:
        for line in file:
            result.add(line.replace('\n',''))
    return result

def append_to_file(file, link):
    with open(file, "a") as f:
        f.write(link + '\n')

def delete_from_file(file, link):
    res = set()
    with open(file, "r") as f:
        for line in f:
            res.add(line.replace('\n', ''))
    
    with open(file, "w") as f:
        for line in res:
            if line != link:
                f.write(line +'\n')

delete_from_file("data/added_friends.txt", "sasha")