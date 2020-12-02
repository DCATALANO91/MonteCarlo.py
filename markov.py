import random
import pandas as pd

results = []
my_dict = {}
markov_dict = {1:[2,4],2:[1,3,5],3:[2,6],4:[1,5,7],5:[2,4,6,8],6:[3,5,9],7:[4,8],8:[5,7,9],9:[6,8]}


for sim in range(0,100000):
    x = random.randint(1,9)
    for step in range(0,1000):
        x = random.choice(markov_dict[x])
    results.append(x)

for rec in range(1,10):
    my_dict[rec] = results.count(rec)/100000

df = pd.DataFrame([my_dict])
df.to_csv(r'F:\PythonProjects\steps.csv', index=False)
