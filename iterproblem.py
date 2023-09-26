'''a simple iterable problem demonstration'''
class Sentence:
    '''entire sentence'''
    def __init__(self,sentence):
        '''initialization'''
        self.sentence=sentence
        self.index=0
        self.words=self.sentence.split()

    def __iter__(self):
        '''iter method'''
        return self

    def __next__(self):
        '''next method'''
        if self.index>=len(self.words):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]

s=Sentence('this is a trial sentence made for this program')
print(s.__next__())
print(next(s))
print(next(s))
print(next(s))
for i in range(1,11):
    tex=f'i want {i:04} apples'
    print(tex)
PI=3.141212121
print(f'i like the number {PI:.2f}')
