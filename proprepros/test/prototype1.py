
def find(array, target):
    for i in range(len(array)): 
        if array[i: i+len(target)] == target:
            yield i
    
def find_str_range(array, start_token="/*", end_token="*/"):
    for s, e in zip(find(array, start_token), find(array, end_token)):
        yield (s, e + len(end_token)), array[s + len(start_token): e]
    
def find_n_replace(string, *args, **kwargs):
    last_index = 0
    for (s, e), _str in find_str_range(string, *args, **kwargs): 
        yield string[last_index: s], _str
        last_index = e
    yield string[last_index:], None

def main():
    file_path = "proprepros/res/"
    with open(file_path + "test.ccc", "r") as file:
        read = file.read()
    
    exec_tokens = {"start_token": "/**", "end_token": "**/"}
    eval_tokens = {"start_token": "/*(", "end_token": ")*/"}

    process_f1 = ""
    for string, _exec in find_n_replace(read, **exec_tokens):
        process_f1 += string
        if _exec is not None: exec(_exec)

    process_f2 = ""
    for string, _eval in find_n_replace(process_f1, **eval_tokens):
        # process_f2 += string + eval(_eval)
        process_f2 += string
        if _eval is not None: process_f2 += eval(_eval)

    with open(file_path + "out.c", "w+") as file:
        file.write(process_f2)
    

if __name__ == "__main__":
    main()