def random_tests(amount, start_object):
    from copy import deepcopy
    from working_directory.inputs import make_input
    model = start_object
    inputs = start_object.input_info()
    graph = {}
    for test in range(amount):
        hs = model.hyperstate()
        if hs not in graph.keys():
            graph[hs] = []
        while True:
            copy = deepcopy(model)
            make_input(copy)
            if copy.possible():
                break
        new_hs = copy.hyperstate()
        if new_hs not in graph[hs]:
            graph[hs].append(new_hs)
        model = copy
    return graph


