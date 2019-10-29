NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names1 =[]
    for n in names:
        if n.title() not in names1:
          names1.append(n.title())
    return names1
    # return [n.title() for n in names if n.title() not in names1]
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names1 = []
    for n in names:
        x = n.split(" ")
        names1.append(x[1] + " " + x[0])
    return names1
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...

n1 = dedup_and_title_case_names(PY_CONTENT_CREATORS)

print(sorted(n1))

print(sorted(sort_by_surname_desc(NAMES),reverse=True))

