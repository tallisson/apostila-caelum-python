def teste_args_kwargs0(*args):
  c

def teste_args_kwargs1(**kwargs):
  for key, value in kwargs.items():
    print('{} = {}'.format(key, value))

args = ('um', 2, 3)
teste_args_kwargs0(args)

kwargs = {  'arg1': 'um', 'arg2': 2, 'arg3': 3, 'arg4': 4 }
teste_args_kwargs1(**kwargs)