import PlainToolsB as ptb
def test(k: float = 10e-2) -> None:
    c = 0
    w = 0
    x = ptb.psequence(k, ..., k * 20e3)
    y = []
    z = ''
    with ptb.Time:
        for i in x:
            if i == float('nan') or i is None:
                raise ArithmeticError(
                    "NaN | None is present in the sequence.")
            c += 1
            if len(str(i)) > 12:
                w += 1
                z = str(i)
                y.append(z)
                print(f'Float Imprecision @{i}')
            print(f'{i}\t\tFIO: {w}\t\t{z}')
            if w >= 10:
                print(f"Too many Imprecision Occurrences. Breaking...")
                print()
                break

    print(f'Float Imprecision Occurrences: {w}')
    ptb.printnl(*y[-10:])
    print(f'Iterations: {c}')
    print(f'Ratio: {ptb.pnumber(w / (c or 1))}')

def main() -> None:
    ptb.printc("[!-PNUMBER-&-PSEQUENCE-!]", fill="-")
    ip = ptb.evinput("\n[N]: ")
    
    with ptb.Try:
        test(ip or 10e-2)

ptb.Main()
