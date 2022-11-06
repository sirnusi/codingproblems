# def caeser_cipher(string, offset):
        
string1 = input('Enter string: ')
offset = int(input('Number: '))
plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'xyzabcdefghijklmnopqrstuvw'

new_list = []

for i in string1:
    if i in plain:
        addition = plain.index(i)
        new_list.append(cipher[addition + offset])

print(new_list)