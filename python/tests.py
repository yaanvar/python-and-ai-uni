def x_2(x):
    match x[2]:
        case 1979:
            match x[3]:
                case 'XSLT':
                    match x[0]:
                        case 'ASP':
                            return 0
                        case 'P4':
                            return 1
                        case 'ABAP':
                            return 2
                case 'SASS':
                    match x[1]:
                        case 1987:
                            return 3
                        case 1993:
                            return 4
                case 'COOL':
                    return 5
        case 1988:
            match x[0]:
                case 'ASP':
                    match x[1]:
                        case 1987:
                            return 6
                        case 1993:
                            return 7
                case 'P4':
                    return 8
                case 'ABAP':
                    return 9
        case 2005:
            return 10
        case _:
            return


def main(x):
    res = x_2(x)
    print(res)


main(['ASP', 1987, 1979, 'COOL'])