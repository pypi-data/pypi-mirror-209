from bx_py_utils.environ import OverrideEnviron
from bx_py_utils.test_utils.context_managers import MassContextManager
from rich import get_console


FIX_TERM_DICT = dict(
    PYTHONUNBUFFERED='1',
    COLUMNS='120',
    TERM='dump',
    NO_COLOR='1',
)


class NoColors(MassContextManager):
    """
    Context manager to deactivate terminal colors and fix the terminal width.
    """

    def __init__(self):
        self.mocks = (
            OverrideEnviron(
                **FIX_TERM_DICT,
            ),
        )

    def __enter__(self):
        super().__enter__()

        console = get_console()  # global console instance
        console._highlight = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        if exc_type:
            return False
