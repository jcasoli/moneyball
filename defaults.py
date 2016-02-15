import results

# A list of all functions in results.py
F_FACTORS = [f for _, f in results.__dict__.iteritems() if callable(f)]

# A list of all tests between two teams in results.py
FACTORS = [f.func_name for f in F_FACTORS if f.func_name.startswith('test')]

#Create a weights dictionary using the function names as keys
#weights = dict(zip(keys, [1,2,3]))

#Call each function and apply weight to each function after they are called
#weighted_sum = [f(1,4) * weights[f.func_name] for f in tests if not f.func_name.startswith('_')]