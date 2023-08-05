from enum import Enum
from raya.controllers.base_pseudo_controller import BasePseudoController
from raya.constants import *
from raya.exceptions import *
from raya.enumerations import *


class UIController(BasePseudoController):

    def __init__(self, name: str, interface):
        pass

    async def display_split_screen(self,
                                   title: str = None,
                                   theme: THEME_TYPE = THEME_TYPE.DARK,
                                   first_component_type: SPLIT_TYPE = None,
                                   first_component_data: dict = None,
                                   second_component_type: SPLIT_TYPE = None,
                                   second_component_data: dict = None,
                                   show_icon: bool = True,
                                   back_button: bool = False,
                                   button_size: int = 1,
                                   custom_style: dict = None,
                                   languages: list = None,
                                   chosen_language: str = None,
                                   wait: bool = False):
        return

    async def display_modal(self,
                            subtitle: str,
                            content: str = None,
                            title: str = None,
                            modal_type: MODAL_TYPE = MODAL_TYPE.INFO,
                            submit_text: str = 'Yes',
                            cancel_text: str = 'No',
                            show_icon: bool = True,
                            theme: THEME_TYPE = THEME_TYPE.DARK,
                            modal_size: MODAL_SIZE = MODAL_SIZE.NORMAL,
                            wait: bool = True,
                            callback: callable = None,
                            custom_style: dict = None) -> Enum:
        pass

    async def display_screen(self,
                             title: str,
                             subtitle: str = None,
                             languages: list = None,
                             chosen_language=None,
                             show_loader: bool = True,
                             theme: THEME_TYPE = THEME_TYPE.DARK,
                             custom_style: dict = None) -> Enum:
        return

    async def display_interactive_map(self,
                                      title: str,
                                      subtitle: str = None,
                                      languages: list = None,
                                      chosen_language=None,
                                      map_name: str = None,
                                      show_robot_position: bool = True,
                                      view_only: bool = False,
                                      theme: THEME_TYPE = THEME_TYPE.DARK,
                                      wait: bool = True,
                                      callback: callable = None,
                                      show_back_button: bool = True,
                                      custom_style: dict = None) -> Enum:
        pass

    async def display_action_screen(self,
                                    title: str,
                                    button_text: str,
                                    languages: list = None,
                                    chosen_language=None,
                                    subtitle: str = None,
                                    button_size: str = None,
                                    theme: THEME_TYPE = THEME_TYPE.DARK,
                                    wait: bool = True,
                                    callback: callable = None,
                                    custom_style: dict = None) -> Enum:
        pass

    async def display_input_modal(self,
                                  subtitle: str,
                                  title: str,
                                  submit_text: str,
                                  cancel_text: str,
                                  placeholder: str = None,
                                  input_type: INPUT_TYPE = INPUT_TYPE.TEXT,
                                  theme: THEME_TYPE = THEME_TYPE.DARK,
                                  wait: bool = True,
                                  callback: callable = None,
                                  custom_style: dict = None) -> Enum:
        pass

    async def display_choice_selector(
            self,
            data: list,
            max_items_shown: int = None,
            scroll_arrow_buttom_text: str = None,
            scroll_arrow_upper_text: str = None,
            languages: list = None,
            chosen_language=None,
            custom_style: dict = None,
            title: str = None,
            theme: THEME_TYPE = THEME_TYPE.DARK,
            show_back_button: bool = False,
            wait: bool = True,
            callback: callable = None,
            back_button: str = 'back',
            title_size: TITLE_SIZE = TITLE_SIZE.MEDIUM) -> Enum:
        pass

    async def display_animation(self,
                                title: str = None,
                                subtitle: str = None,
                                languages: list = None,
                                chosen_language: str = None,
                                content=None,
                                back_button: str = 'back',
                                show_loader: bool = False,
                                format: ANIMATION_TYPE = None,
                                theme: THEME_TYPE = THEME_TYPE.DARK,
                                costum_style: dict = None) -> Enum:
        return

    async def open_link(self,
                        url: str,
                        title: str = None,
                        languages: list = None,
                        chosen_language=None,
                        back_button: str = None,
                        theme: THEME_TYPE = THEME_TYPE.DARK,
                        custom_style: dict = None) -> Enum:
        return

    async def open_conference(self,
                              client: str = None,
                              call_on_join: bool = False,
                              languages: list = None,
                              title: str = None,
                              subtitle: str = None,
                              button_text: str = 'Make a Call',
                              loading_subtitle: str = 'Loading ...',
                              chosen_language=None,
                              back_button: str = 'Back',
                              show_back_button: bool = True,
                              wait: bool = True,
                              callback: callable = None,
                              custom_style: dict = None,
                              theme: THEME_TYPE = THEME_TYPE.DARK) -> Enum:
        pass
