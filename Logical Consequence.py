def f1(P, Q, R):
    return (P or R) and (not Q or R)

def f2(Q, R):
    return (not Q or R)

import inspect
# Returns true if F2 is a lofical consequence of F1
# IE (F1 |= F2)
from itertools import product
def check_consequence(F1, F2):
    F1_params = list(inspect.signature(F1).parameters)
    F2_params = list(inspect.signature(F2).parameters)
    
    for args in product([True, False], repeat=len(F1_params)):
        args_dict = {}
        for arg, param_name in zip(args, F1_params):
            args_dict[param_name] = arg
        F1_bool = f1(**args_dict)
        F2_bool = f2(*[args_dict[param_name] for param_name in F2_params])
        if F1_bool and (F1_bool != F2_bool):
            print(args_dict)
            print(f"F1 is {F1_bool}")
            print(f"F2 is {F2_bool}")
            return False
    return True

if __name__ == "__main__":
    print(f"f1 and f2 are {'' if check_consequence(f1, f2) else 'not'}logically equivalent")
