"""list comprehension and a bit of dictionary comprehension"""
nums = [1,2,3,4,5,6,7,8,9,10]
print("'2n' for each 'n' in nums",end=" ")
print ([n*2 for n in nums])

print("'n*n' for each 'n' in nums using a map + lambda",end=" ")
my_list = list(map(lambda n: n*n, nums))
print (my_list)

print("'n' for each 'n' in nums if 'n' is even using a filter + lambda",end=" ")
my_list = list(filter(lambda n: n%2 == 0, nums))
print (my_list)

print("Dictionary Comprehensions",end=" ")
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)

print("converting list to set to remove duplicates",end=" ")
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print (my_set)
nums = [1,2,3,4,5,6,7,8,9,10]

print("n*n using function",end=" ")
def gen_func(numbers):
    """n*n for each n in nums"""
    for num in numbers:
        yield num*num
my_gen = gen_func(nums)

for i in my_gen:
    print(i,end=" ")
