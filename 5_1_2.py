import random

def main():
    psw = p(5, 20, 'qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*')
    return psw.password
class RandomPassword:
    def __init__(self, min_length, max_length, psw_chars):
        self.min_length = 5
        self.max_length = 20
        self.psw_chars = psw_chars
        self.password = ''.join(random.choice(psw_chars) for i in range(min_length, max_length))
rnd = RandomPassword(5, 20, 'qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*')
p = rnd.__class__
psw = p(5, 20, 'qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*')
lst_pass = [main() for i in range(3)]
print(lst_pass)
