"""Módulo para utilizar o SAP com Python."""
from typing import List

import psutil
import PySimpleGUI as sg
import win32com.client


class Sap:
    """Classe para uso do SAP."""

    __sap_gui: win32com.client.CDispatch = None
    __scripting_engine: win32com.client.CDispatch = None
    __connection: win32com.client.CDispatch = None
    __active_connection: win32com.client.CDispatch = None
    __session: win32com.client.CDispatch = None
    __active_session: win32com.client.CDispatch = None
    __active_window: win32com.client.CDispatch = None
    sg.theme('DarkAmber')

    def __init__(self):
        """Método construtor para o objeto SAP."""
        self.__check_process()

    def __check_process(self) -> None:
        """Método para checar se o aplicativo SAP está aberto."""
        if "saplogon.exe" in (
            process.name() for process in psutil.process_iter()
        ):
            for process in psutil.process_iter(attrs=['name', 'connections']):
                if process.info['name'] == 'saplogon.exe':
                    number_connections: int = len(process.info['connections'])
            if number_connections > 0:
                self.__initialize_logged_in_process()
            else:
                sg.popup_ok(
                    'Workspaces e ambientes do SAP não foram selecionados!',
                    title='Atenção!'
                )
                raise ValueError('Aplicação encerrada!')
        else:
            sg.popup_ok(
                'O Sap Logon não está ativo!',
                title='Atenção!'
            )
            raise ValueError('Aplicação encerrada!')

    def __initialize_logged_in_process(self) -> None:
        """Método para inicializar com o SAP logado."""
        self.__get_object_sap_gui()
        self.__get_scripting_engine_sap_gui()
        self.__connection_sap_gui()
        self.__active_connection_sap_gui()
        self.__session_sap_gui()
        self.__active_session_sap_gui()
        self.__window_sap_gui()
        self.maximize()
        if self.check_logon_screen():
            sg.popup_ok(
                'O SAP não está logado!',
                title='Atenção!'
            )
            self.disconnect()
            raise ValueError('Aplicação encerrada!')
        if not self.check_session_manager():
            definition = sg.popup_yes_no(
                "O sistema está em uso, deseja continuar?",
                title="Atenção!"
            )
            if definition == "Yes":
                self.end_transaction()
            else:
                self.disconnect()
                raise ValueError('Aplicação encerrada!')

    def __get_object_sap_gui(self) -> None:
        """Método para criar o objeto SAPGUI."""
        self.__sap_gui = win32com.client.GetObject('SAPGUI')

    @property
    def sapgui(self) -> win32com.client.CDispatch:
        """Métodod para retornar o objeto SAPGUI."""
        return self.__sap_gui

    def __get_scripting_engine_sap_gui(self) -> None:
        """Método para criar o objeto SAPGUI habilitado para script."""
        self.__scripting_engine = self.__sap_gui.GetScriptingEngine

    @property
    def scripting(self):
        """Método para retornar o objeto SAPGUI habilitado para script."""
        return self.__scripting_engine

    def __connection_sap_gui(self) -> None:
        """Método para criar a conexao com o objeto SAPGUI."""
        self.__connection = self.__scripting_engine.Connections

    @property
    def connections(self):
        """Método para retornar a conexao com o SAPGUI."""
        return self.__connection

    def __active_connection_sap_gui(self) -> None:
        """Método para ativar a conexão do objeto SAPGUI."""
        self.__active_connection = self.__connection[
            self.__connection.Count - 1
        ]

    @property
    def connection(self):
        """Método para retornar o objeto SAPGUI com a conexão ativa."""
        return self.__active_connection

    def __session_sap_gui(self) -> None:
        """Método para criar a sessão do objeto SAPGUI."""
        self.__session = self.__active_connection.Sessions

    @property
    def sessions(self):
        """Método para retornar a sessão do objeto SAPGUI."""
        return self.__session

    def __active_session_sap_gui(self) -> None:
        """Método para ativar a sessão do objeto SAPGUI."""
        self.__active_session = self.__session[self.__session.Count - 1]

    @property
    def session(self):
        """Método para retornar o objeto SAPGUI com a sessão ativa."""
        return self.__active_session

    def __window_sap_gui(
        self,
        item_window: str = "0"
    ) -> None:
        """Método para ativar a janela do objeto SAPGUI.

        Args:
            item_window (str, optional): Item da janela utilizada.
                Defaults to "0".
        """
        self.__active_window = self.__active_session.findById(
            f"wnd[{item_window}]"
        )

    @property
    def window(self):
        """Método para retornar o objeto SAPGUI com a janela ativa."""
        return self.__active_window

    def get_session_info(self) -> dict:
        """Método para retornar informações da session."""
        IsLowSpeedConnection = self.__active_session.Info.IsLowSpeedConnection
        return {
            'is active': self.__active_session.IsActive,
            'is busy': self.__active_session.Busy,
            'connection index': self.__active_session.Parent.Id,
            'session index': self.__active_session.Id,
            'Application Server': self.__active_session.Info.ApplicationServer,
            'Code Page': self.__active_session.Info.Codepage,
            'Group': self.__active_session.Info.Group,
            'GuiCodepage': self.__active_session.Info.GuiCodepage,
            'IsLowSpeedConnection': IsLowSpeedConnection,
            'Language': self.__active_session.Info.Language,
            'MessageServer': self.__active_session.Info.MessageServer,
            'ResponseTime': self.__active_session.Info.ResponseTime,
            'ScreenNumber': self.__active_session.Info.ScreenNumber,
            'SessionNumber': self.__active_session.Info.SessionNumber,
            'SystemNumber': self.__active_session.Info.SystemNumber,
            'SystemSessionId': self.__active_session.Info.SystemSessionId,
            'System Name': self.__active_session.Info.SystemName,
            'Client': self.__active_session.Info.Client,
            'User ID': self.__active_session.Info.User,
            'Program': self.__active_session.Info.Program,
            'Transaction': self.__active_session.Info.Transaction
        }

    def find_object(
        self,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> win32com.client:
        """Método para localizar um objeto.

        Args:
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.

        Returns:
            win32com.client: Retorna o objeto localizado.
        """
        self.__window_sap_gui(item_window)
        return self.__active_window.FindAllByName(
            name_find_object,
            type_find_object
        ).Item(item_find_object)

    def get_text(
        self,
        name_get_text_object: str,
        type_get_text_object: str = "",
        item_get_text_object: int = 0,
        item_window: str = "0"
    ) -> str:
        """Método para retornar o texto de um objeto.

        Args:
            name_get_text_object (str): Informar o nome da área da tela.
            type_get_text_object (str, optional)): Informar o tipo do objeto.
                Defaults to "".
            item_get_text_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.

        Returns:
            str: Retorna o texto do objeto.
        """
        return self.find_object(
            name_get_text_object,
            type_get_text_object,
            item_get_text_object,
            item_window
        ).Text

    def set_text(
        self,
        text_set_text_object: str,
        name_set_text_object: str,
        type_set_text_object: str = "",
        item_set_text_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para inserir um texto em um objeto.

        Args:
            text_set_text_object (str): Informar o texto que deseja inserir.
            name_set_text_object (str): Informar o nome da área da tela.
            type_set_text_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_set_text_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.

        Returns:
            str: Insere o texto no objeto.
        """
        self.find_object(
            name_set_text_object,
            type_set_text_object,
            item_set_text_object,
            item_window
        ).Text = text_set_text_object

    def send_v_key(self, key_SendVKey: int) -> None:
        """Método para pressionar uma técla de atalho.

        Args:
            key_SendVKey (int): Inserir código da tecla de atalho.
        """
        self.__active_window.SendVKey(key_SendVKey)

    def start_transaction(self, transaction: str) -> None:
        """Método para inicair uma transação.

        Args:
            transaction (str): Informar código da transação.
        """
        self.__active_session.StartTransaction(transaction)

    def end_transaction(self) -> None:
        """Método para encerrar uma transação."""
        self.__active_session.EndTransaction()

    def check_logon_screen(self) -> bool:
        """Método para verificar se a tela é de logon.

        Returns:
            bool: Retornar verdadeiro ou falso.
        """
        if (
            self.get_session_info()["Transaction"] == "S000" and
            self.get_session_info()["Client"] == "000" and
            self.get_session_info()["User ID"] == ""
        ):
            return True
        return False

    def check_session_manager(self) -> bool:
        """Método para vewrificar se está na tela inicial.

        Returns:
            bool: Retorna verdadeiro ou falso.
        """
        if (
            self.get_session_info()["Transaction"] == "SESSION_MANAGER" or
            self.get_session_info()["Transaction"] == "SMEN"
        ):
            return True
        return False

    def disconnect(self) -> None:
        """Método para desconectar do SAP logon."""
        self.__active_window = None
        self.__active_session = None
        self.__session = None
        self.__active_connection = None
        self.__connection = None
        self.__scripting_engine = None
        self.__sap_gui = None

    def maximize(self) -> None:
        """Método para maximizar a tela principal."""
        self.__active_window.Maximize()

    def print_screen(self, path_and_name_imagem: str) -> None:
        """Método para printar a tela em uso.

        Args:
            path_and_name_imagem (str): Inserir caminho e nome do arquivo.
        """
        with open(f"{path_and_name_imagem}.bmp", "wb") as file:
            file.write(
                self.__active_window.HardCopyToMemory(0)
            )

    def press(
        self,
        name_press_object: str,
        type_press_object: str = "",
        item_press_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para pressionar um objeto.

        Args:
            name_press_object (str): Inserir nome do objeto.
            type_press_object (str, optional): Inserir tipo do objeto.
                Defaults to "".
            item_press_object (int, optional): Inserir item do objeto.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        self.find_object(
            name_press_object,
            type_press_object,
            item_press_object,
            item_window
        ).Press()

    def select(
        self,
        name_press_object: str,
        type_press_object: str = "",
        item_press_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para selecionar um objeto.

        Args:
            name_press_object (str): Inserir nome do objeto.
            type_press_object (str, optional): Inserir tipo do objeto.
                Defaults to "".
            item_press_object (int, optional): Inserir item do objeto.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        self.find_object(
            name_press_object,
            type_press_object,
            item_press_object,
            item_window
        ).Select()

    def find_object_id(
        self,
        id_find: str
    ) -> win32com.client:
        """Método para localizar um objeto pelo seu Id.

        Args:
            id_find (str): Informar o Id do objeto.
        """
        return self.__active_session.FindById(id_find)

    def tree_expand_node(
        self,
        id_find: str,
        node_key: str
    ) -> None:
        """Método para expandir o nó de uma árvore.

        Args:
            id_find (str): Informar o Id do objeto.
            node_key (str): Informar a chave do nó.
        """
        self.find_object_id(id_find).ExpandNode(node_key)

    def tree_select_node(
        self,
        id_find: str,
        node_key: str
    ) -> None:
        """Método para selecionar o nó de uma árvore.

        Args:
            id_find (str): Informar o Id do objeto.
            node_key (str): Informar a chave do nó.
        """
        self.find_object_id(id_find).SelectNode(node_key)

    def tree_doble_click_node(
        self,
        id_find: str,
        node_key: str
    ) -> None:
        """Método para efetuar o duplo clique em um nó de uma árvore.

        Args:
            id_find (str): Informar o Id do objeto.
            node_key (str): Informar a chave do nó.
        """
        self.find_object_id(id_find).DoubleClickNode(node_key)

    def tree_unselect_node(
        self,
        id_find: str,
        node_key: str
    ) -> None:
        """Método para deselecionar o nó de uma árvore.

        Args:
            id_find (str): Informar o Id do objeto.
            node_key (str): Informar a chave do nó.
        """
        self.find_object_id(id_find).UnselectNode(node_key)

    def insert_dynamic_selection(
        self,
        id_find: str,
        node_key_expand: str,
        node_key_select: str
    ) -> None:
        """Método para inserir um item de seleção dinamica.

        Args:
            id_find (str): Informar o Id do objeto.
            node_key (str): Informar a chave do nó.
        """
        self.tree_expand_node(id_find, node_key_expand)
        self.tree_select_node(id_find, node_key_select)
        self.tree_doble_click_node(id_find, node_key_select)
        self.tree_unselect_node(id_find, node_key_select)

    def show_context_menu(
        self,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para mostar o menu de contexto de um objeto.

        Args:
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        self.find_object(
            name_find_object,
            type_find_object,
            item_find_object,
            item_window
        ).ShowContextMenu()

    def select_context_menu(
        self,
        select_context: str
    ) -> None:
        """Método para selecionar o contexto.

        Args:
            select_context (str): Inserir nome do contexto.
        """
        self.find_object("usr").SelectContextMenuItem(select_context)

    def apply_context(
        self,
        select_context: str,
        list_apply_context: list,
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para aplicar um contexto do menu.

        Args:
            select_context (str): Inserir nome do contexto.
            list_apply_context: Lista com nomes e tipos dos objetos.
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        for name_context, type_context in list_apply_context:
            self.show_context_menu(
                name_context,
                type_context,
                item_find_object,
                item_window
            )
            self.select_context_menu(select_context)

    def set_text_cell(
        self,
        list_itens: list,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0",
        column_itens: int = 1
    ) -> None:
        """Método para inserir um texto em uma célula.

        Args:
            list_itens (list): Informar a lista de itens a serem inseridos.
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
            column_itens (int, optional): Qual coluna deseja utilizar.
                Defaults to 1.
        """
        for index, login in enumerate(list_itens, start=1):
            table_control = self.find_object(
                name_find_object,
                type_find_object,
                item_find_object,
                item_window
            )
            if index == 1:
                table_control.GetCell(0, column_itens).Text = login
            else:
                table_control.GetCell(1, column_itens).Text = login
                table_control.VerticalScrollbar.Position = index

    def press_cell(
        self,
        row_cell: int,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0",
        column_cell: int = 0,
    ) -> None:
        """Método para pressionar uma célula.

        Args:
            row_cell (int): Informar a linha da célula.
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
            column_cell (int, optional): Informar a coluna da célula.
                Defaults to 0.
        """
        self.find_object(
            name_find_object,
            type_find_object,
            item_find_object,
            item_window
        ).GetCell(row_cell, column_cell).Press()

    def double_click_shell(
        self,
        row_shell: int,
        column_shell: str,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para efetuar um duplo click em uma shell.

        Args:
            row_cell (int): Informar a linha da célula.
            column_shell (str): Informar o nome da coluna.
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        table_control = self.find_object(
            name_find_object,
            type_find_object,
            item_find_object,
            item_window
        )
        table_control.ClearSelection()
        table_control.DoubleClick(row_shell, column_shell)

    def selected(
        self,
        type_selection: bool,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para selecionar ou descelecionar uma checkbox.

        Args:
            type_selection (bool): Informar tipo da seleção.
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        self.find_object(
            name_find_object,
            type_find_object,
            item_find_object,
            item_window
        ).Selected = type_selection

    def layout(
        self,
        name_layout: str,
        column_shell: str,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para selecionar um layout.

        Args:
            name_layout (str): Informar a nome do layout.
            column_shell (str): Informar o nome da coluna.
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        table_control = self.find_object(
            name_find_object,
            type_find_object,
            item_find_object,
            item_window
        )
        table_control.ClearSelection()
        for row_table in range(table_control.RowCount):
            table_control.FirstVisibleRow = row_table
            if table_control.GetCellValue(
                row_table,
                column_shell
            ) == name_layout:
                table_control.SelectedRows = str(row_table)
                self.double_click_shell(
                    row_table,
                    column_shell,
                    name_find_object,
                    type_find_object,
                    item_find_object,
                    item_window
                )
                break

    def select_radio_button(
        self,
        item_radio_button: int,
        name_find_object: str,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> None:
        """Método para selecionar um radio button.

        Args:
            item_radio_button (int): Informar o item do rádio button.
            name_find_object (str): Informar o nome da área da tela.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to 0.
        """
        self.find_object(
            name_find_object,
            type_find_object,
            item_find_object,
            item_window
        ).GroupMembers.Item(item_radio_button).Select()

    def message(self) -> None:
        """Método para verificar se a mensagem é de erro.

        Raises:
            Exception: Retorna a informação sobre o erro.
        """
        message = self.find_object(
            "sbar",
            "GuiStatusbar"
        )
        if message.MessageType in [
            "E",
            "A"
        ]:
            raise ValueError(
                message.MessageParameter
            )

    def __return_items(
        self,
        objetc: win32com.client.CDispatch,
        index: int
    ) -> List[str]:
        """Método para retornar o modelo do layout de retorno.

        Args:
            objetc (win32com.client.CDispatch): Informar o objeto a ser
                tratado.
            index (int): Informar o tipo de retorno desejado.

        Returns:
            List[str]: Retorna uma lista com os objetos que se deseja
                visualizar.
        """
        if index == 0:
            return [
                objetc.Name,
                objetc.Type,
                objetc.Tooltip,
                objetc.Text,
                objetc.Parent.Parent.Name
            ]
        elif index == 1:
            return [
                objetc.Name,
                objetc.Type
            ]

    def list_items(
        self,
        name_find_object: str,
        return_type: int = 0,
        search_field: str = 'all',
        search_text: str = None,
        type_find_object: str = "",
        item_find_object: int = 0,
        item_window: str = "0"
    ) -> List[str]:
        """Método para retornar uma lista com as informações desejadas.

        Args:
            name_find_object (str): Informar nome do objeto que se deseja
                visualizar.
            return_type (int, optional): Tipo de retorno que se deseja
                retornar. Defaults to 0.
            search_field (str, optional): Escolher o tipo de visualização
                desejada, são elas:
                all - onde não de faz filtro,
                text - onde o filtro se baseia no texto da célula e
                type onde o filtro se baseio no tipo do objeto.
                Defaults to 'all'.
            search_text (str, optional): Texto a ser localizado.
                Defaults to None.
            type_find_object (str, optional): Informar o tipo do objeto.
                Defaults to "".
            item_find_object (int, optional): Qual objeto deseja retornar.
                Defaults to 0.
            item_window (str, optional): Qual janela deseja utilizar.
                Defaults to "0".

        Returns:
            List[str]: Retorna uma lista com as informações desejadas.
        """
        list_items: List[str] = []
        for item in self.find_object(
            name_find_object=name_find_object,
            type_find_object=type_find_object,
            item_find_object=item_find_object,
            item_window=item_window
        ).Children:
            if search_field == 'all':
                list_items.append(
                    self.__return_items(item, return_type)
                )
            elif search_field == 'text':
                if item.Text == search_text:
                    list_items.append(
                        self.__return_items(item, return_type)
                    )
            elif search_field == 'type':
                if item.Type == search_text:
                    list_items.append(
                        self.__return_items(item, return_type)
                    )
        return list_items
