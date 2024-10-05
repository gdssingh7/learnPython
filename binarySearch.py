tests = [{'inputs':{'cards':[10,9,8,7,6,5,4,3,2],'query':7},'position':3}]

def locate_cards(cards,query):
    pos = 0
    if len(cards)==0:
        return []
    while pos<len(cards):
        if query==cards[pos]:
            return pos
        pos+=1

assert(locate_cards(**tests[0]['inputs'])==tests[0]['position'])
print('done')