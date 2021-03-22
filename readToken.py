

def read_token(path, token_nr):
    with open(path) as file:
        token = file.read().split('\n')
    print(token[token_nr])
    return token[token_nr]
