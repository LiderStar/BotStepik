import re
num = {}
result = []
st = "fjghfjklh g8/ 89 47 fjdafio fiooii3245 jhjkfghf90gak k98,343.989"
for i in re.split("\D", st.strip()):
    if i.isdigit():
        result.append(int(i))
num["result"] = result        
print(num)
