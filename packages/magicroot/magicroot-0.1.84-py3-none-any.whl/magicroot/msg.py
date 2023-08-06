
def rename(rename_dic, prefix='\t\t'):
    if len(rename_dic) > 0:
        msg = prefix + 'Renaming columns: '
        for key, value in rename_dic.items():
            msg += f'\n\t' + prefix + f'\t\t{value} -> \'{key}\''
        return msg
    return ''
