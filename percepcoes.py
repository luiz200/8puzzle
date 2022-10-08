from typing import Tuple, Optional

from dataclasses import dataclass

@dataclass
class PercepcoesJogador():
    '''Coloque aqui atributos que descrevam as percepções possíveis de
    mundo por parte do agente jogador
    
    Vide documentação sobre dataclasses em python.
    '''
    tabuleiro: list()
    dimensoes: Tuple[int, int] = (3,3)
    mensagem_jogo: Optional[str] = None
    posicao_vazia: Tuple[int, int] = (None, None)
