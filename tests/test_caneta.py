import pytest
from caneta import Caneta


def test_instancia_caneta():
    _COR_CANETA = "Azul"
    caneta = Caneta(cor="Azul")
    assert _COR_CANETA == caneta.cor


def test_instancia_caneta_invalida():
    with pytest.raises(ValueError):
        Caneta(cor="")
