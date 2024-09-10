# from decimal import Decimal
# import copy

# def getformat(n):
    
#     n = str(n)
#     e = 0 # This will be useful later
#     if n.find('e') > 0: # where 'n' is the input of the function
#         e = int(n.split('e')[1])
#         n = format(float(n), f".{abs(e) + 15}f").rstrip('0')

#     return n

##################
# from PlainTools import *
# import itertools
# import re

# def infiter(*elements):
#     if len(elements) == 1 and isinstance(elements[0], (int, float)):
#         # Case: Single step argument, generate infinite sequence starting from 0
#         step = elements[0]
#         return itertools.count(start=step, step=step)
    
#     sequences = []
#     i = 0
#     while i < len(elements):
#         if elements[i] == ...:
#             if i == 0 or i == len(elements) - 1:
#                 raise ValueError("Ellipsis cannot be the first or the only element.")
            
#             start = elements[i-1]
#             if i < len(elements) - 1 and isinstance(elements[i+1], (int, float)):
#                 end = elements[i+1]
#                 step = (end - start) / (elements.count(...) + 1)
#                 sequences.append(itertools.islice(itertools.count(start, step), int((end - start) / step)))
#                 i += 1  # Skip the end element as it's handled
#             else:
#                 step = elements[i-1] - elements[i-2]
#                 sequences.append(itertools.count(start + step, step))
#         else:
#             if i == 0 or elements[i-1] != ...:
#                 sequences.append(itertools.repeat(elements[i], 1))
#         i += 1
    
#     return itertools.chain.from_iterable(sequences)


# def main() -> None:
#     c = 0
#     w = 0
#     x = infiter(0.001)
#     y = []
#     z = ''
#     for i in x:
#         if len(str(i)) > 9:
#             w += 1
#             z = str(i)
#             y.append(z)
#             print(f'Float Imprecision @{i}')
#         if i >= 1:
#             break
#         else:
#             print(f'{i}\t\tFIO: {w}\t\t{z}')
#             c += 1

#     print(f'Float Imprecision Occurrences: {w}')
#     printnl(*y[-10:])
#     print(f'Iterations: {c}')


# with Time:
#     main()

##################

# class Library(dict):
#     def __init__(self, *args):
#         super().__init__()
#         self._types = {}
#         for arg in args:
#             arg_type_name = arg.__class__.__name__
#             if arg_type_name not in self:
#                 self[arg_type_name] = []
#             self[arg_type_name].append(arg)
#         self._update_types()
    
#     def _update_types(self):
#         self._types = {key: key for key in self.keys()}

#     def shelf(self, item_type):
#         item_type_name = item_type.__name__
#         return self[item_type_name]

#     def genre(self, new_genres):
#         for genre, conditions in new_genres.items():
#             if isinstance(conditions, list):
#                 self[genre] = []
#                 for cond in conditions:
#                     cond_name = cond.__name__
#                     if cond_name in self:
#                         self[genre].extend(self[cond_name])
#                         del self[cond_name]
#             elif isinstance(conditions, str):
#                 condition_key, condition_value = conditions.split('<')
#                 condition_value = float(condition_value)
#                 genre_elements = []
#                 remaining_elements = []
#                 for item in self[condition_key]:
#                     if item < condition_value:
#                         genre_elements.append(item)
#                     else:
#                         remaining_elements.append(item)
#                 self[genre] = genre_elements
#                 self[condition_key] = remaining_elements

#     def sort(self, *args, **kwargs):
#         # Criar uma lista de tuplas (head, key)
#         heads_keys = [(v[0], k) for k, v in self.items() if v]
#         # Ordenar a lista por heads usando uma função de chave personalizada
#         heads_keys.sort(key=lambda x: (str(type(x[0])), x[0]), *args, **kwargs)
#         # Reorganizar o dicionário com base na nova ordem
#         sorted_dict = {k: self[k] for head, k in heads_keys}
#         # Atualizar self com o dicionário ordenado
#         self.clear()
#         self.update(sorted_dict)
#         # Atualizar tipos
#         self._update_types()

#     @property
#     def copy(self):
#         # Criar uma cópia profunda da biblioteca
#         new_copy = copy.deepcopy(self)
#         return Library(*sum(new_copy.values(), []))

# # Exemplo de uso:
# x = Library(1, 2, 3, 4.0, 5.0, 6.0, '7', '8', '9')

# print(x)  # {'int': [1, 2, 3], 'float': [4.0, 5.0, 6.0], 'str': ['7', '8', '9']}

# print(x.shelf(int))  # [1, 2, 3]

# y = x.shelf(float)
# print(y)  # [4.0, 5.0, 6.0]

# y.extend([4.5, 5.5, 6.5])
# print(y)  # [4.0, 5.0, 6.0, 4.5, 5.5, 6.5]
# print(x)  # {'int': [1, 2, 3], 'float': [4.0, 5.0, 6.0, 4.5, 5.5, 6.5], 'str': ['7', '8', '9']}

# x.genre({'num': [int, float, Decimal]})
# print(x)  # {'str': ['7', '8', '9'], 'num': [1, 2, 3, 4.0, 5.0, 6.0, 4.5, 5.5, 6.5]}

# x.genre({'smallnum': 'num<5'})
# print(x)  # {'str': ['7', '8', '9'], 'num': [5.0, 5.5, 6.0, 6.5], 'smallnum': [1, 2, 3, 4.0, 4.5]}

# # Testando o método sort
# x.sort()
# print(x)  # {'smallnum': [1, 2, 3, 4.0, 4.5], 'num': [5.0, 5.5, 6.0, 6.5], 'str': ['7', '8', '9']}

# # Testando a propriedade copy
# y = x.copy.shelf(float)
# print(y)  # [5.0, 5.5, 6.0, 6.5]

# y.extend([4.5, 5.5, 6.5])
# print(y)  # [5.0, 5.5, 6.0, 6.5, 4.5, 5.5, 6.5]
# print(x)  # {'smallnum': [1, 2, 3, 4.0, 4.5], 'num': [5.0, 5.5, 6.0, 6.5], 'str': ['7', '8', '9']}  # Note que modificar 'y' não modifica 'x'
# print(type(x))  # <class '__main__.Library'>
# print(type(y))  # <class 'list'>




# #===========================================================================================================

# from PlainTools import Seval as mateval

# # Exemplos de uso:
# if __name__ == "__main__":
#     import math
#     import builtins
#     from PlainTools import Constant, Container

#     class double(int):
#         def __new__(cls, val):
#             return int.__new__(cls, val * 2)

#     print(mateval('5 + 5'))  # 10
#     print(mateval('10+10'))  # 20
#     print(mateval('math.e'))  # 2.718281828459045
#     print(mateval('double(5) + 5'))  # 15
#     print(mateval('Constant(5) + 5'))  # 5
#     print(mateval('Container(5)'))  # {5: None}

#     try:
#         print(mateval('10 / 0'))  # ZeroDivisionError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval('builtins.print(5)'))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("builtins.eval('print(5)')"))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("import decimal; decimal.Decimal(5.0)"))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("__import__('os').system('ls')"))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("x = 5"))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("y = lambda y: y + 5"))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("exec('globals()')"))  # UnsafeError
#     except BaseException as e:
#         print(e)

#     try:
#         print(mateval("compile(a,b,c)"))  # UnsafeError
#     except BaseException as e:
#         print(e)
    
# import unittest
# from unittest.mock import patch

# class TestMatevalSecurity(unittest.TestCase):

#     def test_hidden_attributes(self):
#         # Accessing special attributes
#         with self.assertRaises(TypeError):
#             mateval("__class__.__bases__")
#         with self.assertRaises(TypeError):
#             mateval("().__class__.__bases__")

#     def test_disallowed_functions_indirect(self):
#         # Indirect function calls
#         with self.assertRaises(TypeError):
#             mateval("getattr(__import__('builtins'), 'eval')('print(5)')")
#         with self.assertRaises(TypeError):
#             mateval("getattr(__import__('os'), 'system')('ls')")

#     def test_callable_injection(self):
#         # Callable objects performing unsafe operations
#         with self.assertRaises(TypeError):
#             mateval("f = lambda: __import__('os').system('ls'); f()")

#     def test_complex_expressions(self):
#         # Complex expressions to bypass restrictions
#         with self.assertRaises(TypeError):
#             mateval("[x for x in ().__class__.__bases__[0].__subclasses__() if x.__name__ == 'Popen'][0]('ls', shell=True)")

#     def test_magic_methods_access(self):
#         # Accessing magic methods
#         with self.assertRaises(TypeError):
#             mateval("().__init__")
#         with self.assertRaises(TypeError):
#             mateval("().__call__")

#     def test_lambda_expressions(self):
#         # Executing malicious code using lambda expressions
#         with self.assertRaises(TypeError):
#             mateval("(lambda: __import__('os').system('ls'))()")

#     def test_accessing_properties(self):
#         # Accessing properties that could be unsafe
#         with self.assertRaises(TypeError):
#             mateval("().__class__.__dict__['__init__']")

#     def test_indirect_module_access(self):
#         # Indirectly accessing disallowed modules
#         with self.assertRaises(TypeError):
#             mateval("open('/etc/passwd').read()")

#     def test_comprehensions_generators(self):
#         # Using comprehensions and generators to bypass restrictions
#         with self.assertRaises(TypeError):
#             mateval("(x for x in ().__class__.__bases__[0].__subclasses__() if x.__name__ == 'Popen').__next__()('ls', shell=True)")
#         with self.assertRaises(TypeError):
#             mateval("[x for x in ().__class__.__bases__[0].__subclasses__() if x.__name__ == 'Popen'][0]('ls', shell=True)")

#     def test_base64_injection(self):
#         # Tentar injetar código malicioso usando base64
#         with self.assertRaises(TypeError):
#             mateval("(__import__('base64').b64decode('cHJpbnQoMSk='))()")  # 'print(1)' codificado em base64

#     def test_encoded_string_evaluation(self):
#         # Avaliar string codificada que pode conter código malicioso
#         with self.assertRaises(TypeError):
#             mateval("eval('print(1)')")  # Avaliando uma string de código malicioso

#     def test_hex_encoded_code_execution(self):
#         # Injetar código malicioso usando codificação hexadecimal
#         with self.assertRaises(TypeError):
#             mateval("(lambda x: x.write('test'))(open('/dev/null', 'w'))")
#             mateval("(__import__('codecs').decode('7072696e742831292e736572766963657329', 'hex'))()")  # 'print(1)' em hexadecimal

#     def test_encoded_lambda_expression(self):
#         # Tentar executar uma expressão lambda codificada
#         with self.assertRaises(TypeError):
#             mateval("(lambda x: x.system('ls'))(__import__('subprocess'))")
#             mateval("eval('lambda: __import__(\"os\").system(\"ls\")')()")

#     def test_malicious_encoded_expression(self):
#         # Tentar executar uma expressão codificada maliciosa
#         with self.assertRaises(TypeError):
#             mateval("(__import__('os').popen('ls'))")
#             mateval("eval('exec(\"__import__('os').system('ls')\")')")

#     def test_encoded_string_access(self):
#         # Tentar acessar uma função maliciosa através de uma string codificada
#         with self.assertRaises(TypeError):
#             mateval("(__import__('subprocess').check_output('ls', shell=True))")
#             mateval("eval('getattr(__import__(\"builtins\"), \"eval\")(\"print(1)\")')")

#     def test_insecure_base64_eval(self):
#         # Tentar executar uma função insegura a partir de base64
#         with self.assertRaises(TypeError):
#             mateval("(__import__('subprocess').check_output('ls', shell=True)[0])")
#         with self.assertRaises(TypeError):
#             mateval("((lambda x: x.check_output('ls', shell=True))(__import__('subprocess')))[0]")
#             mateval("exec(__import__('base64').b64decode('cHJp\n\n\n\n\n').decode('utf-8'))")

# if __name__ == "__main__":
#     unittest.main()

# import PlainToolsB as pt

# def float_imprecision_test(fn, test=('',)):
    
#     for test in tests:
#         try:
#             print(f'{fn.__name__}({test}) == {fn(test)}')
#         except BaseException as e:
#             print(f'{fn.__name__}({test}) == {e}')
#             print('ERROR')
#         finally:
#             print(f'eval({test}) == {pt.Seval(test)}')
#             print()

# tests = (
#     "0.1 * 3",  # Classic example
#     "0.1 * 7",
#     "5/3",
#     "0.1 + 0.2",  # Another classic example
#     "0.3 - 0.1",
#     "1.2 - 1.0",
#     "0.1 + 0.1 + 0.1 - 0.3",
#     "1e-8 + 1 - 1",  # Small number addition
#     "1e100 + 1 - 1e100",  # Large number addition
#     "0.1234567890123456 + 1e-16",  # Precision loss
#     "1 / 3 * 3",
#     "0.1 ** 3",  # Powers
#     "355 / 113",  # Approximation of pi
#     "2 ** 53 + 1 - 2 ** 53",  # Beyond integer precision
#     "0.1 * 10 ** 16 - 10 ** 15",
#     "0.3333333333333333 * 3",
#     "1e-16 * 1e16 - 1",
#     "1e16 + 1 - 1e16",
#     "0.1 * 0.1",
#     "0.000000000000001 + 1 - 1",
#     "9999999999999999 + 0.00000000000001 - 9999999999999999",
#     "0.2 * 0.2",
#     "0.5 - 0.4 - 0.1",
#     "1e-323 + 1e-323",  # Near smallest representable double
#     "1.7976931348623157e+308 + 1 - 1.7976931348623157e+308",  # Near largest representable double
#     "1 / 10 + 1 / 100 + 1 / 1000",
#     "0.1 + 0.01 + 0.001 + 0.0001 + 0.00001",
#     "math.sin(math.pi/2)",  # Trigonometric functions (assuming math.sin and math.pi are imported)
#     "math.log(math.exp(1))",  # Logarithmic and exponential functions (assuming math.log and math.exp are imported)
#     "math.sqrt(2) ** 2 - 2",  # Square root (assuming math.sqrt is imported)
# )

# float_imprecision_test(pt.number, tests)