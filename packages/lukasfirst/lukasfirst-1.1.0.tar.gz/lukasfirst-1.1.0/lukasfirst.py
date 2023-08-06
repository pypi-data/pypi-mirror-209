
#lista = ['Kamil', 'Ziomek', 'Bartek', 'Anna', 'Paulina', 'Gosia', ['Pies', 'Kot', 'Kogut', ['Tulipan', 'Roza', 'Mak']]]

'''for x in lista:
    if isinstance(x, list):
        for nested_x in x:
            if isinstance(nested_x, list):
                for nested_nested_x in nested_x:
                    if isinstance(nested_nested_x, list):
                        print(nested_nested_x)
                    else:
                        print(nested_nested_x)
            else:
                print(nested_x)
    else:
        print(x)'''

def lista_funkcja(lista, level):
    """This function takes a positional argument called "lista", which is any Python list
    (of - possibly - nested lists). Each data item in the provided list is(recursively) printed
    to the screen on it's own line. A second argument called"level" is used to insert tab-stops
    when a nested list is encountered"""
    for each_item in lista:
        if isinstance(each_item, list):
            lista_funkcja(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)

#print(lista_funkcja(lista))
#lista2=['Polska', 'Niemcy', 'Niderlandy',['Kenya', 'Senegal', 'Egipt', ['Japonia', 'Tajlandia', 'Chiny']]]

#print(lista_funkcja(lista2))
