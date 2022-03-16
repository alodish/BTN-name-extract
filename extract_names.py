import pandas as pd

all_lines = []
k = 0

with open('btn_givennames_synonyms.txt', 'r', encoding='utf8') as txt:
    for line in txt:
        if k >= 8:
            temp_line = line.strip('\n')
            temp_line = temp_line.split('\t')
            all_lines.append([temp_line[0], temp_line[2]])
        else:
            k += 1

columns = ['Name', 'Nicknames']
df = pd.DataFrame(all_lines, columns=columns)
print(df.head())
df.to_csv('names-nicknames.csv')
