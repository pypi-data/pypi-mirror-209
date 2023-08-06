from Modelo_de_Dados_Lusitania.src.modelo_de_dados.base._modules.magicroot.db import CompleteTable
from Modelo_de_Dados_Lusitania.src.modelo_de_dados.base._modules.magicroot.cp import Settings
from Modelo_de_Dados_Lusitania.src.modelo_de_dados.base._modules.magicroot.os import home


class SnapShots(CompleteTable):
    i = {
        'snap': {'file_name': 'Team Leader Snapshots Report 20230306_052913.csv', 'delimiter': ','}
    }
    default_extension = '.xlsx'

    def create(self, snap):
        return snap


def clean_snap_shots():
    s = Settings('pmo', 'configs')
    folder = home[s['folder']]
    SnapShots().build(input=folder, output=folder)


