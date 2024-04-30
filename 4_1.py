class Factory:
    @staticmethod
    def build_sequence():
        lst = []
        return lst
    @staticmethod
    def build_number(string):
        s = ''
        otr = False
        for i in string:
            if i == '-':
                otr = True
            if i != ' ' and i!= '-':
                s += i
        if otr:
            s = int(s)*-1
        else:
            s = int(s)
        otr = False
        return s
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq

if __name__ == '__main__':
    factory = Factory()
    loader = Loader()
    red = Loader.parse_format("1, 2, 3, -5, 10", factory)
    print(red)