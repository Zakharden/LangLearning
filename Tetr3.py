"Количество символов между s-ками"
"""str = "Hello, Selly! I love you so much!"
str_small = str.lower()
s = str_small[str_small.find('s') + 1 : str_small.rfind('s')]
print(len(s))"""

"""n = int(input())
for _ in range(n):
    s = input()
    if '[' in s:
        s = s[1:s.find('[')]+ s[s.rfind(']')+1:]
    print(s.rstrip())

n = int(input())
for _ in range(n):
    s = input()
    if '[' in s:"""

"""s = input()

    if '[' in s:
        s = s[:s.find('[')] + s[s.find(']') + 1:]
    else:
        print(s)

[Сейчас бы погладить [милого] ёжика] Это прекрасная [ну или не очень] строка"""

s=input()
otkr=0
t = str()
for i in s:
    if i =='[':
        otkr+=1
    elif i == ']':
        otkr-=1
    else:
        if otkr==0:
            t+=i
t.split()

print(*t.split())
