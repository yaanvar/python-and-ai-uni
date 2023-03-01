def main(x):
    match x[3]:
        case "LSL":
            match x[2]:
                case 'RDOC':
                    return 6
                case 'TEA':
                    return 7
        case "PAN":
            match x[2]:
                case 'RDOC':
                    return 8
                case 'TEA':
                    return 9
        case "DART":
            match x[0]:
                case "HAXE":
                    match x[4]:
                        case 'XC':
                            return 2
                        case 'GLYPH':
                            match x[1]:
                                case 'APL':
                                    return 0
                                case 'MAX':
                                    return 1
                case "BLADE":
                    return 3
                case "ELM":
                    match x[2]:
                        case 'RDOC':
                            return 4
                        case 'TEA':
                            return 5
        case _:
            return




print(main(['ELM', 'APL', 'RDOC', 'DART', 'XC'])) # 4
print(main(['BLADE', 'APL', 'TEA', 'DART', 'GLYPH'])) # 3
print(main(['ELM', 'APL', 'TEA', 'PAN', 'GLYPH'])) # 9
print(main(['HAXE', 'MAX', 'TEA', 'LSL', 'GLYPH'])) # 7
print(main(['BLADE', 'MAX', 'RDOC', 'PAN', 'XC'])) # 8