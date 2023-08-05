#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: HsPyLib
   @package: clitt.core.tui.mselect
      @file: mselect.py
   @created: Tue, 4 May 2021
    @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior"
      @site: https://github.com/yorevs/hspylib
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2023, HsPyLib team
"""

from typing import List, Optional, TypeVar

from clitt.core.tui.mselect.mselect.menu_select import MenuSelect

T = TypeVar("T")


def mselect(
    items: List[T],
    title: str = "Please select one",
    output: str = None
    ) -> Optional[T]:
    """
    Terminal UI menu select input method.
    :param items: the provided items to select from.
    :param title: the title to be displayed before the options.
    :param output: optional output file containing the selected item.
    :return: the selected item.
    """
    result = MenuSelect(title, items).execute()

    if output:
        with open(output, 'w') as f_out:
            f_out.write(result)

    return result
