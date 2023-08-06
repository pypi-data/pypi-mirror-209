def docstring(arguments = [('x', 'int'), ('y', 'int')], return_value = None):
    """
    Maakt een docstring format op de wijze van deze docstring

    Parameters:
    --------------------        
    arguments : list (default = [('x', 'int'), ('y', 'int')])
        Lijst met tuples die de argumenten van de functie voorstelt
        Elke tuple bevat twee elementen, de naam van het argument en het data type van het argument.
        
    return_value : str (default = None, for it to always generate a simple format)
        De naam van de return_value

    Returns:
    --------------------
    docstring : str 
        De docstring
    """
    
    doc = f'    """\n    Tekst die de functie samenvat\n\n'
    doc += '    Parameters:'
    doc += '\n    ' + '-' * 20 + '\n'
    for argument in arguments:
        doc += f'        {argument[0]} : {argument[1]}\n            Tekst die de {argument[0]} argument omschrijft.\n\n'
    doc += '    Returns:'
    doc += '\n    ' + '-' * 20 + '\n'
    doc += f'       {return_value}\n            Tekst die de return waarde omschrijft.\n'
    doc += '    """'

    return doc