"""some basic exception handling"""
try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception #an alternate method to raise Exception in statement itself.
except IOError as e:
    print('First!')
except Exception as e:
    print('Second') #commenting first exception will run this exception first
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
