import data

us_state_abbrev = data.us_state_abbrev
states = data.states
# print(us_state_abbrev)
# print(states)

NOT_FOUND = 'N/A'



def get_every_nth_state(states=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""

    nthState = []
    index = n - 1
    while index < len(states):
        nthState.append(states[index])
        index += n
    print(nthState)
    return nthState
    pass


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    try:
        return us_state_abbrev[state_name]
    except KeyError:
        return NOT_FOUND
    pass


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    if isinstance(data, list):
        states_dict = {len(state) : state for state in data}
        return states_dict[max(states_dict.keys())]
    else:
        states_dict = {len(state): state for state in data.keys()}
        return states_dict[max(states_dict.keys())]
    pass


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list without losing
       alphabetical order"""
    newList = []
    i = 0
    for state in sorted(us_state_abbrev.keys()):
      newList.append(us_state_abbrev[state])
      i += 1
      if i >= 10:
        break
    return sorted(newList) + sorted(states)[(len(states) - 10) :]
    pass

#
# get_every_nth_state(states=states, n=10)
# print(get_longest_state(us_state_abbrev))
print(combine_state_names_and_abbreviations())