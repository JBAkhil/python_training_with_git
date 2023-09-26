'''iterable demonstration'''
class MyRange:
    '''defining range'''
    def __init__(self,start,stop):
        '''initialization'''
        self.value=start
        self.end=stop

    def __iter__(self):
        '''iter method'''
        return self

    def __next__(self):
        '''next method'''
        if self.value<=self.end:
            current=self.value
            self.value+=1
            return current
        raise StopIteration

def my_range(start,stop):
    '''my_range usage directly as a method'''
    current=start
    while current<=stop:
        yield current
        current+=1

for num in MyRange(1,10):
    print(num)

for num in my_range(1,10):
    print(num)
