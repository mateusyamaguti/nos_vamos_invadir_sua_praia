# -*- coding: utf-8 -*-
from Agendamento import Agendamento, PraiaError
import pytest


class TestAgendamento:
    def test_class_declared(self):
        objeto = Agendamento()
        assert isinstance(objeto, Agendamento)
        assert isinstance(objeto.agendamentos, list)

    def test_str_repr(self):
        objeto = Agendamento()
        assert 'Agendamento' == str(objeto)
        assert 'Agendamento' == repr(objeto)

    def test_agendamento_segunda_feira_invalidos_1(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Segunda-feira não possui agendamentos"):
            agenda.agendar('Cliente1',0 ,11 ,1 )

    def test_agendamento_segunda_feira_invalidos_2(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Segunda-feira não possui agendamentos"):
            agenda.agendar('Cliente1' ,0 ,14 , 3 )

    def test_agendamento_segunda_feira_invalidos_3(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Segunda-feira não possui agendamentos"):
            agenda.agendar('Cliente1' ,0 ,20 ,3 )

    def test_agendamento_terca_feira_validos(self):
        agenda = Agendamento()
        assert len(agenda.agendamentos) == 0
        agenda.agendar('Cliente1' ,1 ,11 ,1 )
        assert len(agenda.agendamentos) == 1
        agenda.agendar('Cliente1' ,1 ,14 , 3 )
        assert len(agenda.agendamentos) == 2
        agenda.agendar('Cliente1' ,1 ,20 , 1 )
        assert len(agenda.agendamentos) == 3

    def test_agendamento_terca_feira_invalidos(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Agendamento inválido para terça-feira"):
            agenda.agendar('Cliente1' ,1 ,20 ,3 )

    def test_agendamento_quarta_feira_validos(self):
        agenda = Agendamento()
        assert len(agenda.agendamentos) == 0
        agenda.agendar('Cliente1' ,2 ,11 ,1 )
        assert len(agenda.agendamentos) == 1
        agenda.agendar('Cliente1' ,2 ,14 , 3 )
        assert len(agenda.agendamentos) == 2
        agenda.agendar('Cliente1' ,2 ,20 , 1 )
        assert len(agenda.agendamentos) == 3

    def test_agendamento_quarta_feira_invalidos(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Agendamento inválido para quarta-feira"):
            agenda.agendar('Cliente1' ,2 ,20 ,3 )

    def test_agendamento_quinta_feira_validos(self):
        agenda = Agendamento()
        assert len(agenda.agendamentos) == 0
        agenda.agendar('Cliente1' ,3 ,11 ,1 )
        assert len(agenda.agendamentos) == 1
        agenda.agendar('Cliente1' ,3 ,14 , 3 )
        assert len(agenda.agendamentos) == 2
        agenda.agendar('Cliente1' ,3 ,20 , 1 )
        assert len(agenda.agendamentos) == 3

    def test_agendamento_quinta_feira_invalidos(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Agendamento inválido para quinta-feira"):
            agenda.agendar('Cliente1' ,3 ,20 ,3 )

    def test_agendamento_sexta_feira_validos(self):
        agenda = Agendamento()
        assert len(agenda.agendamentos) == 0
        agenda.agendar('Cliente1' ,4 ,11 ,1 )
        assert len(agenda.agendamentos) == 1
        agenda.agendar('Cliente1' ,4 ,14 , 3 )
        assert len(agenda.agendamentos) == 2
        agenda.agendar('Cliente1' ,4 ,20 , 1 )
        assert len(agenda.agendamentos) == 3

    def test_agendamento_sexta_feira_invalidos(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Agendamento inválido para sexta-feira"):
            agenda.agendar('Cliente1' ,4 ,20 ,3 )

    def test_agendamento_sabado_validos(self):
        agenda = Agendamento()
        assert len(agenda.agendamentos) == 0
        agenda.agendar('Cliente1' ,5 ,11 ,1 )
        assert len(agenda.agendamentos) == 1
        agenda.agendar('Cliente1' ,5 ,14 , 3 )
        assert len(agenda.agendamentos) == 2
        agenda.agendar('Cliente1' ,5 ,20 , 1 )
        assert len(agenda.agendamentos) == 3

    def test_agendamento_sabado_invalidos(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Agendamento inválido para sábado"):
            agenda.agendar('Cliente1' ,5 ,20 ,3 )

    def test_agendamento_domingo_validos(self):
        agenda = Agendamento()
        assert len(agenda.agendamentos) == 0
        agenda.agendar('Cliente1' ,6 ,11 ,1 )
        assert len(agenda.agendamentos) == 1
        agenda.agendar('Cliente1' ,6 ,14 , 3 )
        assert len(agenda.agendamentos) == 2
        agenda.agendar('Cliente1' ,6 ,17 , 1 )
        assert len(agenda.agendamentos) == 3

    def test_agendamento_domingo_invalidos(self):
        agenda = Agendamento()
        with pytest.raises(PraiaError, match="Agendamento inválido para domingo"):
            agenda.agendar('Cliente1' ,6 ,20 ,3 )