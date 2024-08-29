from PlainTools import Seval as mateval

# Exemplos de uso:
if __name__ == "__main__":
    import math
    import builtins
    from PlainTools import Constant, Container

    class double(int):
        def __new__(cls, val):
            return int.__new__(cls, val * 2)

    print(mateval('5 + 5'))  # 10
    print(mateval('10+10'))  # 20
    print(mateval('math.e'))  # 2.718281828459045
    print(mateval('double(5) + 5'))  # 15
    print(mateval('Constant(5) + 5'))  # 5
    print(mateval("Container('5')"))  # {5: None}

    try:
        print(mateval('10 / 0'))  # ZeroDivisionError
    except BaseException as e:
        print(e)

    try:
        print(mateval('builtins.print(5)'))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("builtins.eval('print(5)')"))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("import decimal; decimal.Decimal(5.0)"))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("__import__('os').system('ls')"))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("x = 5"))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("y = lambda y: y + 5"))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("exec('globals()')"))  # UnsafeError
    except BaseException as e:
        print(e)

    try:
        print(mateval("compile(a,b,c)"))  # UnsafeError
    except BaseException as e:
        print(e)
    
import unittest
from unittest.mock import patch

"""
LLM Used: ChatGPT 4o - @Python - chatgpt.com/g/g-cKXjWStaE-python
"""

class TestMatevalSecurity(unittest.TestCase):

    def test_hidden_attributes(self):
        # Accessing special attributes
        with self.assertRaises(TypeError):
            mateval("__class__.__bases__")
        with self.assertRaises(TypeError):
            mateval("().__class__.__bases__")

    def test_disallowed_functions_indirect(self):
        # Indirect function calls
        with self.assertRaises(TypeError):
            mateval("getattr(__import__('builtins'), 'eval')('print(5)')")
        with self.assertRaises(TypeError):
            mateval("getattr(__import__('os'), 'system')('ls')")

    def test_callable_injection(self):
        # Callable objects performing unsafe operations
        with self.assertRaises(TypeError):
            mateval("f = lambda: __import__('os').system('ls'); f()")

    def test_complex_expressions(self):
        # Complex expressions to bypass restrictions
        with self.assertRaises(TypeError):
            mateval("[x for x in ().__class__.__bases__[0].__subclasses__() if x.__name__ == 'Popen'][0]('ls', shell=True)")

    def test_magic_methods_access(self):
        # Accessing magic methods
        with self.assertRaises(TypeError):
            mateval("().__init__")
        with self.assertRaises(TypeError):
            mateval("().__call__")

    def test_lambda_expressions(self):
        # Executing malicious code using lambda expressions
        with self.assertRaises(TypeError):
            mateval("(lambda: __import__('os').system('ls'))()")

    def test_accessing_properties(self):
        # Accessing properties that could be unsafe
        with self.assertRaises(TypeError):
            mateval("().__class__.__dict__['__init__']")

    def test_indirect_module_access(self):
        # Indirectly accessing disallowed modules
        with self.assertRaises(TypeError):
            mateval("open('/etc/passwd').read()")

    def test_comprehensions_generators(self):
        # Using comprehensions and generators to bypass restrictions
        with self.assertRaises(TypeError):
            mateval("(x for x in ().__class__.__bases__[0].__subclasses__() if x.__name__ == 'Popen').__next__()('ls', shell=True)")
        with self.assertRaises(TypeError):
            mateval("[x for x in ().__class__.__bases__[0].__subclasses__() if x.__name__ == 'Popen'][0]('ls', shell=True)")

    def test_base64_injection(self):
        # Tentar injetar código malicioso usando base64
        with self.assertRaises(TypeError):
            mateval("(__import__('base64').b64decode('cHJpbnQoMSk='))()")  # 'print(1)' codificado em base64

    def test_encoded_string_evaluation(self):
        # Avaliar string codificada que pode conter código malicioso
        with self.assertRaises(TypeError):
            mateval("eval('print(1)')")  # Avaliando uma string de código malicioso

    def test_hex_encoded_code_execution(self):
        # Injetar código malicioso usando codificação hexadecimal
        with self.assertRaises(TypeError):
            mateval("(lambda x: x.write('test'))(open('/dev/null', 'w'))")
            mateval("(__import__('codecs').decode('7072696e742831292e736572766963657329', 'hex'))()")  # 'print(1)' em hexadecimal

    def test_encoded_lambda_expression(self):
        # Tentar executar uma expressão lambda codificada
        with self.assertRaises(TypeError):
            mateval("(lambda x: x.system('ls'))(__import__('subprocess'))")
            mateval("eval('lambda: __import__(\"os\").system(\"ls\")')()")

    def test_malicious_encoded_expression(self):
        # Tentar executar uma expressão codificada maliciosa
        with self.assertRaises(TypeError):
            mateval("(__import__('os').popen('ls'))")
            mateval("eval('exec(\"__import__('os').system('ls')\")')")

    def test_encoded_string_access(self):
        # Tentar acessar uma função maliciosa através de uma string codificada
        with self.assertRaises(TypeError):
            mateval("(__import__('subprocess').check_output('ls', shell=True))")
            mateval("eval('getattr(__import__(\"builtins\"), \"eval\")(\"print(1)\")')")

    def test_insecure_base64_eval(self):
        # Tentar executar uma função insegura a partir de base64
        with self.assertRaises(TypeError):
            mateval("(__import__('subprocess').check_output('ls', shell=True)[0])")
        with self.assertRaises(TypeError):
            mateval("((lambda x: x.check_output('ls', shell=True))(__import__('subprocess')))[0]")
            mateval("exec(__import__('base64').b64decode('cHJp\n\n\n\n\n').decode('utf-8'))")

if __name__ == "__main__":
    unittest.main()
