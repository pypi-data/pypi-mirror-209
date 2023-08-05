#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: HsPyLib
   @package: clitt.core.tui.minput
      @file: input_validator.py
   @created: Thu, 20 May 2021
    @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior"
      @site: https://github.com/yorevs/hspylib
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2023, HsPyLib team
"""

from hspylib.core.enums.enumeration import Enumeration
from hspylib.core.tools.validator import Validator

import re


class InputValidator(Validator):
    """MenuInput 'input' validator."""

    class PatternType(Enumeration):
        # fmt: off
        LETTERS     = r"^[a-zA-Z]{%min%,%max%}$"
        WORDS       = r"^[a-zA-Z0-9 _]{%min%,%max%}$"
        NUMBERS     = r"^[0-9\.\,]{%min%,%max%}$"
        MASKED      = r".*\|.{2,}"
        ANYTHING    = r".{%min%,%max%}"
        CUSTOM      = r''
        # fmt: on

    @classmethod
    def custom(cls, pattern: str, min_length: int = 1, max_length: int = 30) -> "InputValidator":
        """Return a custom validator that allows customize the input rules.
        :param pattern: the custom validator pattern.
        :param min_length: the minimum length required.
        :param max_length: the maximum length allowed.
        """
        pattern_type = cls.PatternType.CUSTOM
        validator = InputValidator(min_length, max_length, pattern_type=pattern_type)
        validator.pattern = pattern
        return validator

    @classmethod
    def letters(cls, min_length: int = 1, max_length: int = 30) -> "InputValidator":
        """Return a validator that allows only letters.
        :param min_length: the minimum length required.
        :param max_length: the maximum length allowed.
        """
        return InputValidator(min_length, max_length, cls.PatternType.LETTERS)

    @classmethod
    def numbers(cls, min_length: int = 1, max_length: int = 30) -> "InputValidator":
        """Return a validator that allows only numbers.
        :param min_length: the minimum length required.
        :param max_length: the maximum length allowed.
        """
        return InputValidator(min_length, max_length, cls.PatternType.NUMBERS)

    @classmethod
    def words(cls, min_length: int = 1, max_length: int = 30) -> "InputValidator":
        """Return a validator that allows only words (space, numbers or letters).
        :param min_length: the minimum length required.
        :param max_length: the maximum length allowed.
        """
        return InputValidator(min_length, max_length, cls.PatternType.WORDS)

    @classmethod
    def anything(cls, min_length: int = 1, max_length: int = 30) -> "InputValidator":
        """Return a validator that allows any input value.
        :param min_length: the minimum length required.
        :param max_length: the maximum length allowed.
        """
        return InputValidator(min_length, max_length, cls.PatternType.ANYTHING)

    def __init__(self, min_length: int = 1, max_length: int = 30, pattern_type: PatternType = PatternType.ANYTHING):
        self._min_length = min_length
        self._max_length = max_length
        self._pattern_type = pattern_type
        self._pattern = pattern_type.value

    def __str__(self) -> str:
        return (
            f'r"{self.pattern}"' if InputValidator.pattern_type == self.PatternType.CUSTOM else self.pattern_type.name
        )

    def __repr__(self):
        return str(self)

    def __call__(self, *args, **kwargs) -> bool:
        return all(self.validate(value) for value in args)

    def validate(self, value: str) -> bool:
        """Validate the value against the validator rules."""
        return bool(re.match(self.pattern, value))

    @property
    def pattern(self) -> str:
        return (
            str(self._pattern)
            .replace("%min%", str(self._min_length or 1))
            .replace("%max%", str(self._max_length or 30))
        )

    @pattern.setter
    def pattern(self, pattern: str) -> None:
        self._pattern = rf"{pattern}"

    @property
    def pattern_type(self) -> PatternType:
        return self._pattern_type
