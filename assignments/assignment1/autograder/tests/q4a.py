test = {   'name': 'q4a',
    'points': 5,
    'suites': [   {   'cases': [   {'code': ">>> \n>>> print(type(fraction_outcome))\n<class 'pandas.core.frame.DataFrame'>\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> \n>>> len(fraction_outcome)\n19', 'hidden': False, 'locked': False},
                                   {'code': '>>> \n>>> fraction_outcome.iloc[0] < fraction_outcome.iloc[-1]\nprobwin_outcome    True\ndtype: bool', 'hidden': False, 'locked': False},
                                   {'code': '>>> \n>>> np.round(fraction_outcome.sum(), 3)\nprobwin_outcome    9.5\ndtype: float64', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
