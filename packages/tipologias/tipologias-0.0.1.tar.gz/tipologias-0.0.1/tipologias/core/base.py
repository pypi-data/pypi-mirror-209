from abc import ABC, abstractmethod


class Tipologia(ABC):
    """Classe abstrata que define a estrutura básica de uma tipologia para análise de dados.

    As classes que herdam dessa classe devem implementar os métodos "input_data", "processor", "output_data" e "execute".

    Attributes:
        Nenhum atributo é definido nessa classe.

    Methods:
        input_data(): Extrai os dados necessários do banco de dados e armazena em um DataFrame.
        processor(): Processa os dados extraídos e armazena o resultado em um DataFrame.
        output_data(): Escreve o resultado da análise na tabela resposta do banco de dados.
        execute(): Executa a análise completa.
    """

    @abstractmethod
    def input_data(self):
        """Extrai os dados necessários do banco de dados e armazena em um DataFrame."""
        pass

    @abstractmethod
    def processor(self):
        """Processa os dados extraídos e armazena o resultado em um DataFrame."""
        pass

    @abstractmethod
    def output_data(self):
        """Escreve o resultado da análise na tabela resposta do banco de dados."""
        pass

    @abstractmethod
    def execute(self):
        """Executa a análise completa."""
        pass
