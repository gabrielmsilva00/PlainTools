from PlainToolsB import *

def test(k: Float = 10e-2) -> None:
    c = 0
    w = 0
    #x = psequence(pnumber(k),...,pnumber(k * 20e3))
    x = psequence(Number(k), ..., Number(k * 20e3))
    y = []
    z = ''
    with Time:
        for i in x:
            if i is None:
                raise ArithmeticError(
                    "NaN | None is present in the sequence.")
            c += 1
            if len(str(i)) > 10:
                w += 1
                z = str(i)
                y.append(z)
                print(f'Float Imprecision @{i}')
            print(f'{i}\t\tFIO: {w}\t\t{z}')

    print(f'Float Imprecision Occurrences: {w}')
    printnl(*y[-10:])
    print(f'Iterations: {c}')
    print(f'Ratio: {pnumber(w / (c or 1))}')
    print(f'Type: {type(x)}')

def main() -> None:
    printc("[!-PNUMBER-&-PSEQUENCE-!]", fill="-")
    #ip = evinput("\n[N]: ")
    ip = None
    
    with Try:
        if ip:
            test(ip)
        else:
            test()

Main()
