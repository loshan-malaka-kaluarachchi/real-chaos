def data(*words):
    copy = list(words)
    copy.append(type(words))
    copy.append(words.count)
    return copy    
    
print(data('a','b','c'))