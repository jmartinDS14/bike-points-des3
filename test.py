import os

file = [f for f in os.listdir('data') if f.endswith('.json')]
print(file)
filename = 'data/'+file
print(filename)
