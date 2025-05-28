class FormulaError(ValueError):
    """FormulaError is raised if a formula is invalid."""
    pass

def parse_formula(formula, periodic_table=None):
    """
    Convert a chemical formula for a molecule into a compound list.

    Example: "H2O" → [["H", 2], ["O", 1]]
    """
    def parse_quant(formula, i):
        quant = 1
        if i < len(formula) and formula[i].isdigit():
            start = i
            while i < len(formula) and formula[i].isdigit():
                i += 1
            quant = int(formula[start:i])
        return quant, i

    def parse_recursive(formula, i, level):
        start_level = level
        symbol_quantity_list = []
        while i < len(formula):
            ch = formula[i]
            if ch == "(":
                group, i = parse_recursive(formula, i + 1, level + 1)
                quant, i = parse_quant(formula, i)
                for elem in group:
                    elem[1] *= quant
                symbol_quantity_list.extend(group)
            elif ch.isalpha():
                if ch.isupper():
                    symbol = ch
                    i += 1
                    if i < len(formula) and formula[i].islower():
                        symbol += formula[i]
                        i += 1
                    quant, i = parse_quant(formula, i)
                    symbol_quantity_list.append([symbol, quant])
                else:
                    raise FormulaError(f"Invalid formula at index {i}")
            elif ch == ")":
                if level == 0:
                    raise FormulaError("Unmatched closing parenthesis")
                level -= 1
                return symbol_quantity_list, i + 1
            else:
                raise FormulaError(f"Invalid character '{ch}' at index {i}")
        if level != 0:
            raise FormulaError("Unmatched opening parenthesis")
        return symbol_quantity_list, i

    parsed_formula, _ = parse_recursive(formula, 0, 0)
    return parsed_formula
