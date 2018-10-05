import urllib.request
import os.path

print('What is the url you are looking to retrieve from, young lad?')
req = input()
print('What is the destination we wish to save this to?')
dest = input()
print('And lastly, the name of your file?')
filename = input()

full_name = os.path.join(dest, filename)

urllib.request.urlretrieve(req, full_name)






