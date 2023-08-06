

def docdb_to_jpoapp(case_number):
    return case_number.split(".")[1]


def jpoapp_to_docbd(case_number):
    return "JP.%s.A" % case_number


def jpopub_to_docbd(case_number):
    return "JP.%s.A" % case_number


def jpwopub_to_docbd(case_number):
    return "JP.WO%s.A1" % case_number


def repub_to_docbd(case_number):
    return "JP.WO%s.A5" % case_number


def jpopat_to_docbd(case_number, last="B2"):
    return "JP.%s.%s" % (case_number, last)

def jpo_to_docdb(case_number, last="B2", wo=False, repub=False):
    '''
    日本特許庁における出願番号をDOCDB形式に変換する関数

    Parameters
    ----------
    case_number: str
        6桁(登録番号)又は8-12桁(出願番号/公開番号)
    last: str
        登録番号場合の末尾につける文字列
    wo: boolean
        PCT出願であるかどうか
    repub: boolean
        再公表番号であるかどうか

    Returns
    -------
    str
        DOCDB形式の出願番号又は公開番号

    Examples
    --------
    # 10桁の場合には、出願番号又は公開番号(A)が返される。
    >>> jpo_to_docdb("2022012345")
    'JP.2022012345.A'

    # 6桁の場合には特許番号(B2)が返される
    >>> jpo_to_docdb("1202345")
    'JP.1202345.B2'

    # 引数でB1を指定するとB1となる
    >>> jpo_to_docdb("1202345", last="B1")
    'JP.1202345.B1'

    # wo=Trueの場合、A1が返される。
    >>> jpo_to_docdb("2022012345", wo=True)
    'JP.WO2022012345.A1'

    # repub=Trueの場合、A5が返される。
    >>> jpo_to_docdb("2022012345", repub=True)
    'JP.WO2022012345.A5'
    '''
    if len(case_number) == 7:
        return jpopat_to_docbd(case_number, last)
    if repub:
           return repub_to_docbd(case_number)
    elif wo:
           return jpwopub_to_docbd(case_number)
    else:
        return jpoapp_to_docbd(case_number)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
