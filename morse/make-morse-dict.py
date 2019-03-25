#create a morse alphabet
import json

morse_a = {}
with open("morse-code.txt") as fh:
    for line in fh:
        letter, code = line.strip().split(' ',1)
        morse_a[letter] = code.strip()

fw = open("MorseDict.py",'w')
#fw.write(f"morse_a = {str(morse_a)}")
fw.write(f"morse_a = {json.dumps(morse_a)}")
#`print(morse_a)

#s = "STRING"

#for c in s:
#    print(f"{c} {morse_a[c]}")

print(json.dumps(morse_a))

fh.close()
fw.close()
