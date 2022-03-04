def composing_str_old(document):
    letter = ''
    for i in document:
        if i.isalpha():
            letter += i
    return letter


def composing_str_faster(document):
    temp =[]
    for i in document:
        if i.isalpha():
            temp.append(i)
    return ''.join(temp)

def evenmorefaster_composing(document):
    return ''.join([c for c in document if c.isalpha()])


def evenmorefaster_withoutlist_composing(document):
    return ''.join(c for c in document if c.isalpha())

document = 'this is for'

print(composing_str_old(document))
print(composing_str_faster(document))
print(evenmorefaster_composing(document))
print(evenmorefaster_withoutlist_composing(document))