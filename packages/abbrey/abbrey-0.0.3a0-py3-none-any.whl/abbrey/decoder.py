from pathlib import Path
from typing import Optional

import pandas as pd

this_directory = Path(__file__).parent


class AbbrDecoder:
    def __init__(
        self, abbr_file_path: str = this_directory / "acronyms_ver0.1.csv"
    ) -> None:
        """
        Main class to decode abbreviation

        NOTE: Currently load the whole file because it's smol
        and lookup process will be faster. If the file became
        larger, lazy loading instead.
        """
        abbr_file = pd.read_csv(abbr_file_path)
        self.abbr_dict = dict(zip(abbr_file["acronym"], abbr_file["detail"]))

    def decode_abbr(self, abbr: str) -> Optional[str]:
        """
        Decode a single abbr.

        Returns:
            Optional[str]: Decoded abbr if searched successfully, else None
        """
        return self.abbr_dict.get(abbr)

    def decode_sentence(self, sentence: str) -> str:
        """
        Decode whole sentence

        Returns:
            str: Decoded sentence if abbr is searched successfully, else
        """
        tokens = sentence.split(" ")

        def _get_abbr_if_any(abbr: str):
            return self.abbr_dict.get(abbr, abbr)

        return " ".join(map(_get_abbr_if_any, tokens))
