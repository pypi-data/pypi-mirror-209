from datetime import datetime

import pandas as pd

from tipologias.core.base import Tipologia
from tipologias.queries.socios import Q_LIST_SOCIO_CNPJ


class SociosComum(Tipologia):
    """Classe que implementa a tipologia SociosComum para analisar a ocorrência de sócios em comum entre cnpjs.

    Args:
        lista_cnpjs (tuple): Uma lista de cnpjs para analisar.

    Attributes:
        lista_cnpjs (tuple): Uma lista de cnpjs para analisar.
        df (pandas.DataFrame): O resultado da análise, armazenado em um DataFrame do pandas.

    Methods:
        input_data(): Extrai os dados necessários do banco de dados "big_data_cieg".
        processor(): Processa os dados extraídos e armazena o resultado em um DataFrame.
        output_data(): Escreve o resultado da análise na tabela "trilhas_resposta_socios_comum" do banco de dados "default".
        execute(): Executa a análise completa.
    """

    def __init__(self, engine, lista_cnpjs: list, data_entrada=None, data_saida=None) -> None:
        """Inicializa a classe SociosComum com os parâmetros necessários.

        Args:
            crtl_analise_pregao_id (int): O ID da análise de pregão associada a essa tipologia.
            lista_pregoes (tuple): Uma lista de números de pregão para analisar.
        """
        self.engine = engine
        self.lista_cnpjs = lista_cnpjs
        self.data_entrada = data_entrada if data_entrada else datetime.now().date()
        self.data_saida = data_saida if data_saida else datetime.now().date()
        self.df = None
        self.processed_data = None
        self.socios_comum = None
        self.output_table = "trilhas_resposta_socios_comum"


    def input_data(self):
        query = Q_LIST_SOCIO_CNPJ.format(
            lista_cnpjs="','".join(self.lista_cnpjs),
            data_entrada=self.data_entrada,
            data_saida=self.data_saida
        )
        self.df = pd.read_sql_query(
            query,
            self.engine
        )

    def processor(self):
        self.socios_comum = pd.DataFrame()
        for row in self.df.itertuples(name="Socio"):
            df = self.df.query(
                f'NUM_CNPJ_EMPRESA != "{row.NUM_CNPJ_EMPRESA}" and (NUM_CPF == "{row.NUM_CPF}" or NUM_CNPJ == "{row.NUM_CNPJ}")'
            )
            self.socios_comum = pd.concat([self.socios_comum, df], ignore_index=True)

        self.df = self.socios_comum

    def output_data(self):
        return self.df

    def execute(self):
        self.input_data()
        self.processor()
        return self.output_data()
