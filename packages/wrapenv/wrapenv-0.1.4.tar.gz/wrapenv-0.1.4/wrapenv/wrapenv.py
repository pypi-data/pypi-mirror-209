#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        wrapenv.py
# Purpose:     A module to wrap functions in an environment with pre- and post-processing functions.
# Project:     WrapEnv
#
# Author:      Anton G. Mueckl (amueckl@chartup.de)
#
# Created:     22.05.2023
# Copyright:   (c) Anton G. Mueckl (amueckl@chartup.de) 2023
# Licence:     MIT
# -------------------------------------------------------------------------------

import functools
import typing
import dataclasses

@dataclasses.dataclass
class Function:
    """
    A class that represents a callable function along with pre- and post-processing functions and environment.

    Attributes:
    - call (typing.Callable): The main function to be called.
    - args (typing.List): List of positional arguments to be passed to the function (default: empty list).
    - kwargs (typing.Dict): Dictionary of keyword arguments to be passed to the function (default: empty dictionary).
    - result (typing.Any): The result of the function call (default: None).
    - preprocessing (typing.Callable): Function to be executed before calling the main function (default: None).
    - postprocessing (typing.Callable): Function to be executed after calling the main function (default: None).
    - check (typing.Callable): Function for result validation or condition checking (default: None).
    - modify (typing.Callable): Function to modify the result before returning (default: None).
    - _name (str): Internal attribute to store the name of the function (default: None).
    - _local_env (typing.Dict): Internal attribute to store the local environment variables (default: empty dictionary).
    """
    call: typing.Callable = None
    args: typing.List = dataclasses.field(default_factory=list)
    kwargs: typing.Dict = dataclasses.field(default_factory=dict)
    result: typing.Any = None
    preprocessing: typing.Callable = None
    postprocessing: typing.Callable = None
    check: typing.Callable = None
    modify: typing.Callable = None
    _name: str = None
    _local_env: typing.Dict = dataclasses.field(default_factory=dict)


class ENVIRONMENT(dict):
    """
        A class that manages several functions within an environment.

        It provides methods to register functions, add arguments to functions, and retrieve arguments.

        Inherited from `dict`, allowing access to functions using dictionary-like syntax.

        Methods:
        - __resolve_fn_name__(API_fn_or_name: typing.Union[str, typing.Callable]) -> str:
            Resolves the function name from a given API function or name.
            Returns the resolved function name.

        - register_function(function: typing.Callable) -> None:
            Registers a function in the environment.
            Raises a TypeError if the function is not callable.

        - add_argument(API_fn_or_name: typing.Union[str, typing.Callable], argument: typing.Any) -> None:
            Adds an argument to the specified function.
            Resolves the function name if necessary.

        - add_kwargument(API_fn_or_name: typing.Union[str, typing.Callable], keyword: str, argument: typing.Any) -> None:
            Adds a keyword argument to the specified function.
            Resolves the function name if necessary.

        - get_arguments(API_fn_or_name: typing.Union[str, typing.Callable]) -> typing.Tuple[typing.List, typing.Dict]:
            Retrieves the arguments and keyword arguments of the specified function.
            Resolves the function name if necessary.
            Returns a tuple containing the list of arguments and a dictionary of keyword arguments.
        """
    def __init__(self):
        super(ENVIRONMENT, self).__init__()
        pass

    def __resolve_fn_name__(self, API_fn_or_name: typing.Union[str, typing.Callable]) -> str:
        """
        Resolves the function name from a given API function or name.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.

        Returns:
        - str: The resolved function name.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        if isinstance(API_fn_or_name, str):
            API_name =  API_fn_or_name
        elif callable(API_fn_or_name):
            API_name =  API_fn_or_name.__name__
        else:
            raise TypeError(f'API function or name {API_fn_or_name} is neither a string nor a callable.')
        if not API_name in self.keys():
            self[API_name] = Function(_name=API_name)
        return API_name

    def register_function(self, function: typing.Callable) -> None:
        """
        Registers a function in the environment.

        Args:
        - function (typing.Callable): The function to register.

        Raises:
        - TypeError: If the function is not callable.
        """
        if not callable(function):
            raise TypeError(f'Function {function} is not callable.')
        name = function.__name__
        if name not in self.keys():
            self[name] = Function(call=function, _name=name)
            pass
        else:
            self[name].call = function
            pass
        setattr(self, name, functools.partial(self.run_API_cmd, name))
        pass

    def add_argument(self, API_fn_or_name: typing.Union[str, typing.Callable], argument: typing.Any) -> None:
        """
        Adds an argument to the specified function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - argument (typing.Any): The argument to add.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].args.append(argument)
        pass

    def add_kwargument(self, API_fn_or_name: typing.Union[str, typing.Callable], keyword: str, argument: typing.Any) -> None:
        """
        Adds a keyword argument to the specified function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - keyword (str): The keyword for the argument.
        - argument (typing.Any): The argument to add.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].kwargs[keyword] = argument
        pass

    def get_arguments(self, API_fn_or_name: typing.Union[str, typing.Callable]) -> typing.Tuple[typing.List, typing.Dict]:
        """
        Retrieves the arguments and keyword arguments of the specified function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.

        Returns:
        - typing.Tuple[typing.List, typing.Dict]: A tuple containing the list of arguments and a dictionary of keyword arguments.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        return self[API_name].args, self[API_name].kwargs

    def clear_arguments(self, API_fn_or_name: typing.Union[str, typing.Callable]) -> None:
        """
        Clears the arguments and keyword arguments of the specified function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].args.clear()
        self[API_name].kwargs.clear()
        pass

    def register_arguments(self, API_fn_or_name: typing.Union[str, typing.Callable], *args, **kwargs) -> None:
        """
        Registers arguments and keyword arguments for the specified API function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - *args: Variable length arguments to register.
        - **kwargs: Keyword arguments to register.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        for argument in args:
            self.add_argument(API_name, argument)
            pass
        for kw, argument in kwargs.items():
            self.add_kwargument(API_name, kw, argument)
            pass

    def register_preprocessing(self, API_fn_or_name: typing.Union[str, typing.Callable], preprocessing: typing.Callable) -> None:
        """
        Registers a preprocessing function for the specified API function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - preprocessing (typing.Callable): The preprocessing function to register.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].preprocessing = preprocessing
        pass

    def register_postprocessing(self, API_fn_or_name: typing.Union[str, typing.Callable], postprocessing: typing.Callable) -> None:
        """
        Registers a postprocessing function for the specified API function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - postprocessing (typing.Callable): The postprocessing function to register.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].postprocessing = postprocessing
        pass

    def register_check(self, API_fn_or_name: typing.Union[str, typing.Callable], check: typing.Callable) -> None:
        """
        Registers a check function for the specified API function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - check (typing.Callable): The check function to register.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].check = check
        pass

    def register_modify(self, API_fn_or_name: typing.Union[str, typing.Callable], modify: typing.Callable) -> None:
        """
        Registers a modify function for the specified API function.

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.
        - modify (typing.Callable): The modify function to register.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        self[API_name].modify = modify
        pass

    def run_API_cmd(self, API_fn_or_name: typing.Union[str, typing.Callable], *args, **kwargs) -> typing.Any:
        """
        Executes the steps defined for the API command associated with the specified function:
        - Preprocessing
        - API call
        - Check
        - Modify and rerun (if check fails)
        - Postprocessing

        Args:
        - API_fn_or_name (typing.Union[str, typing.Callable]): The API function or name.

        Returns:
        - typing.Any: The result of the API command.

        Raises:
        - TypeError: If the API function or name is neither a string nor a callable.
        - KeyError: If the API function or name is not registered in the environment.

        Notes:
        - The API function must be registered in the environment using the `register_function` method.
        - The check function, if defined, should be a callable that takes the environment (`self`) and the function object (`fn`) as arguments.
        - The check function should return a boolean value indicating whether the API function execution should continue or not.
          If check returns False, the modify function will be called (if defined) and the API function will be executed again.
        - The modify function, if defined, should be a callable that takes the environment (`self`) and the function object (`fn`) as arguments.
        - The modify function can be used to modify the environment or function object during each iteration of the check loop.
        - The preprocessing function, if defined, should be a callable that takes the environment (`self`) and the function object (`fn`) as arguments.
        - The preprocessing function can be used to perform any necessary setup or transformations before executing the API function.
        - The postprocessing function, if defined, should be a callable that takes the environment (`self`) and the function object (`fn`) as arguments.
        - The postprocessing function can be used to perform any necessary cleanup or finalization steps after executing the API function.
        """
        API_name = self.__resolve_fn_name__(API_fn_or_name)
        if not API_name in self.keys():
            raise KeyError(f'API entry point {API_name} not registered for PyInstaller_SPEC_ADDON.')
        self.register_arguments(API_name, *args, **kwargs)
        fn = self[API_name]
        fn_call = fn.call
        if isinstance(fn_call, tuple):      # If the API function is a tuple, it is assumed to be a (function, args, kwargs) tuple.
            fn_call = fn_call[0]
            pass
        if not callable(fn_call):
            raise KeyError(f'API entry point {API_name} not callable for PyInstaller_SPEC_ADDON.')

        if fn.preprocessing is not None:
            fn.preprocessing(self, fn)
            pass

        fn.result = fn_call(*fn.args, **fn.kwargs)

        if fn.check is not None:
            while not fn.check(self, fn):
                fn.result = fn_call(*fn.args, **fn.kwargs)
                if fn.modify is not None:
                    fn.modify(self, fn)
                    pass
                pass
            pass

        if fn.postprocessing is not None:
            fn.postprocessing(self, fn)
            pass
        return fn.result

# The global environment object. This is the object that is used to register API functions and arguments.
# Using this global object, the API functions can be called from anywhere in the code and even from within
# multiple modules.

environment = ENVIRONMENT()
