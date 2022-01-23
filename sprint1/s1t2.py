def filterBible(scripture, book, chapter):
    bookchapter=book + chapter
    found_list = []
    for i in scripture:
        if i[:5] == bookchapter:
            found_list.append(i)
    return found_list    
