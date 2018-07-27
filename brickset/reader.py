from bs4 import BeautifulSoup

sample = 'data/courselink-results/out10097.html'
with open(sample, 'r') as f:
    s = BeautifulSoup(f.read(), 'lxml')

for t in s.children:
    print(t.type)
