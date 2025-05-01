def readable_timedelta(days):
    '''
    Retorna uma string com o número de semanas e dias incluídos em days.
    
    Parâmetros:
    days - número de dias para conversão (int)

    Retorna:
    string do número de semanas e dias incluídos em days
    '''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)