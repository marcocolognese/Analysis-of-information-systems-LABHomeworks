import sys


def irpef_calculation(income):
    if (income >= 15000):
        irpef = 3450
        if (income >= 28000):
            irpef = irpef + 3510
            if (income >= 55000):
                irpef = irpef + 10260
                if (income >= 75000):
                    irpef = irpef + 8200
                    irpef = (income - 75000) * 0.43 + irpef
                else:
                    irpef = (income - 55000) * 0.41 + irpef
            else:
                irpef = (income - 28000) * 0.38 + irpef
        else:
            irpef = (income - 15000) * 0.27 + irpef
    else:
        irpef = (income) * 0.23

    return irpef


def main(income):  # pragma: no cover
    print("\n#####################################")
    print("####      IRPEF CALCULATION      ####")
    print("#####################################\n")

    print("IRPEF: \x80{:.2f}\n".format(irpef_calculation(income))).decode("windows-1252")


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) > 1:
        if float(sys.argv[1]) >= 0:
            main(float(sys.argv[1]))
        else:
            print("Income must be greater than 0\n")
    else:
        print("Missing income\n")
