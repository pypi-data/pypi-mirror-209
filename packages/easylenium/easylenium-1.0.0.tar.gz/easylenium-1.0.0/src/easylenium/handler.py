import functools
from typing import Callable, Optional, TypeVar
from .utils import setup_logger

logger = setup_logger("handler")
R = TypeVar('R')


def handle(exception: Exception) -> Callable[[Callable[..., R]], 
                                             Callable[..., Optional[R]]]:
    """
    A decorator that handles a specific exception raised by a function.

    Args:
        exception (Exception): The exception to be caught and handled.

    Returns:
        Callable[[Callable[..., R]], Callable[..., Optional[R]]]: 
            A decorator function.

    Example:
        >>> @handle(ValueError)
        ... def divide(a, b):
        ...     return a / b
        ...
        >>> result = divide(5, 0)
        >>> print(result)
        None
    """
    def handle_error(func: Callable[..., R]) -> Callable[..., Optional[R]]:
        """
        Decorator function that wraps the original function and handles 
            the specified exception.

        Args:
            func (Callable[..., R]): The function to be decorated.

        Returns:
            Callable[..., Optional[R]]: The wrapped function that handles 
                the exception.

        Example:
            >>> @handle_error
            ... def divide(a, b):
            ...     return a / b
            ...
            >>> result = divide(5, 0)
            >>> print(result)
            None
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Optional[R]:
            """
            Wrapper function that executes the wrapped function and handles 
                the exception.

            Args:
                *args: Variable-length argument list.
                **kwargs: Arbitrary keyword arguments.

            Returns:
                Optional[R]: The return value of the wrapped function or None 
                    if the exception is caught.

            Example:
                >>> @handle_error
                ... def divide(a, b):
                ...     return a / b
                ...
                >>> result = divide(5, 0)
                >>> print(result)
                None
            """
            try:
                return func(*args, **kwargs)
            except exception:
                logger.info(f"function '{func.__name__}' threw "
                            f"an Exception ({exception})")
                return None

        return wrapper

    return handle_error
