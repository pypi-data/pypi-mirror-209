from tests.db import ConnectionHandler
from tipologias.core.socios_comum import SociosComum


def test_socio_comum():
    db = ConnectionHandler()
    cnpjs = ["27600270000190","08778201000126"]
    tp_socios_comum = SociosComum(engine=db.engine, lista_cnpjs=cnpjs, data_entrada='2021-02-22', data_saida='2021-02-22')
    assert len(tp_socios_comum.execute()) == 2