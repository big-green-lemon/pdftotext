from io import BufferedReader
from typing import Generator

class PDF:
    """A helper that interfaces the `poppler` library."""
    def __init__(
        self,
        pdf_file: BufferedReader,
        password: str = '',
        physical: bool=False,
        raw: bool=False
    ):
        """
        Args:
            pdf_file (str): A file opened for reading in binary mode.
            password (str): Unlocks the document, if required. Either the owner of password or the user password works.
            raw (bool): If True, page text is output in the order it appears in the content stream.
            physical (bool): If True, page text is output in the order it appears on the page, regardless of columns or other layout features.

            Usually, the most readable output is achieved by using the default
            mode, rather than raw or physical.

            Example:
            ```python
            with open("doc.pdf", "rb") as f:
                pdf = PDF(f)
            for page in pdf:
                print(page)
            ```
        """
        ...
    def __iter__(self) -> Generator[str, None, None]:
        """Returns the output of `pdftotext` for the current page through a generator."""
        ...