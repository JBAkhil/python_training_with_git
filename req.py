import requests
r_for_content=requests.get('https://httpbin.org/basic-auth/something/prx',auth=('something','prx'))
r_for_image=requests.get('https://picsum.photos/200/300')
#print(r_for_content.text) for site text
#print(r_for_content.status_code) for status_code ex:200 for active
# print(r_for_content.ok) prints true if status_code<400
# print(r_for_content.headers) prints some information 
with open('random_image.png', 'wb') as f:
    f.write(r_for_image.content)
print(r_for_content.text)
payload={'username':'something', 'password':'prx'} 
r_post=requests.post("http://httpbin.org/post",data=payload)
#print(r_post.text)
#or
r_dict=r_post.json()
print(r_dict['form'])
#print(r_for_content.url) to print the url 