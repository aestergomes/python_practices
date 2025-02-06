# determine length, index of first occurrence of 'and', index of last occurrence of 'you', and count of 'you' in the verse string.

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

print("comprimento da lista:", len(verse))
print("primeira ocorrencia de 'and:'", verse.find('and'))
print("última ocorrencia de 'you:'", verse.rfind('you'))
print("quantidade de 'you:'", verse.count('you'))