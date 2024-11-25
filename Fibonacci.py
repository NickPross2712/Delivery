def obfuscator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        name = result['name']
        password = result['password']
        obfuscated_name = name[0] + '*' * (len(name) - 2) + name[-1]
        obfuscated_password = '*' * len(password)
        result['name'] = obfuscated_name
        result['password'] = obfuscated_password
        return result
    return wrapper

@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }

print(get_credentials())