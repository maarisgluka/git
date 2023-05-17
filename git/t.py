with open('t.txt') as f:
    text = f.read()
    print(text)
    nevajadzigi = ".,!?;:()"
    for i in nevajadzigi:
        text = text.replace(i, "")
    text = text.split(' ')
    print(text)

    vardu_skaits = {}
    for vards in text:
        if len(vards) > 3:
            vardu_skaits[vards] = text.count(vards)
        
    print(vardu_skaits)



# with open("teksts.txt") as file:
#     persons = file.readlines()

#     for i in range(len(persons)):
#         persons[i] = persons[i].replace('\n', '')

#     print(persons)

#     persons.sort(reverse=True)

#     print(persons)