#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: HsPyLib
   @package: clitt.core.tui.minput
      @file: minput.py
   @created: Tue, 4 May 2021
    @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior"
      @site: https://github.com/yorevs/hspylib
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2023, HsPyLib team
"""
import os
from typing import List, Optional

from hspylib.core.namespace import Namespace
from hspylib.core.preconditions import check_argument
from hspylib.core.tools.text_tools import quote, snakecase

from clitt.core.tui.minput.form_field import FormField
from clitt.core.tui.minput.menu_input import MenuInput


def minput(
    form_fields: List[FormField],
    title: str = "Please fill all fields of the form fields below",
    output: str = None
    ) -> Optional[Namespace]:
    """
    Terminal UI menu form input method.
    :param form_fields: the provided form items to input from.
    :param title: the title to be displayed before the form.
    :param output: optional output file containing the marked items.
    :return: a namespace containing all form values.
    """
    check_argument(len(form_fields) > 0, 'Must provide at least one form field!')
    result = MenuInput(title, form_fields).execute()

    if result and output:
        with open(output, 'w') as f_out:
            for name, value in zip(result.attributes, result.values):
                f_out.write(f"{snakecase(name, screaming=True)}={quote(value)}" + os.linesep)

    return result


if __name__ == '__main__':
    it = [
        'Age || numbers | 1 / 3 ||',
        'Password | password || 8 ||',
        'Access ||| 5 | r | Admin',
        'Role | select || 3 / 5 || <one>,two,three ',
        'Phone | masked | masked | 5 / 50 || ;(##) #####-#### ',
        'Accept Conditions | checkbox ||||'
    ]
    form_fields = MenuInput.builder() \
        .from_tokenized(it) \
        .build()
    minput(form_fields, "Fill the form below", "/tmp/out.txt")
