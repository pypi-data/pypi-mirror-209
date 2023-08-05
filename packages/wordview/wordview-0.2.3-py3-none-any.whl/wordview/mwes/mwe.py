import json
from pathlib import Path
from typing import Dict, List, Union

import pandas
from nltk import word_tokenize

from wordview import logger
from wordview.mwes.am import calculate_am
from wordview.mwes.mwe_utils import get_counts


class MWE(object):
    """
    Represents a Multiword Expression.
    """

    def __init__(
        self,
        df: pandas.DataFrame,
        text_column: str,
        mwe_types: List[str] = ["NC"],
        tokenize=False,
    ) -> None:
        """Initialize a new MWE object with the given df, text_column and mwe_types.

        Args:
            df (pandas.DataFram): DataFrame with a text_column that contains the corpus.
            text_column (str): Specifies the column of DataFrame where text data resides.
            mwe_types (List): Types of MWEs to be extracted. Supports: NC for Noun-Noun and JNC for Adjective-Noun compounds. Example: ['NC', 'JNC'].
            tokenize (bool): Tokenize the content of `df[text_column]`.

        Returns:
            None
        """
        self.df = df
        self.text_column = text_column
        for mt in mwe_types:
            if mt not in ["NC", "JNC"]:
                raise ValueError(f"{mt} type is not recognized.")
        self.mwe_types = mwe_types
        if tokenize:
            logger.info(
                '"tokenize" flag set to True. This might lead to a slow instantiation.'
            )
            self.df[text_column] = self.df[text_column].apply(self._tokenize)
        else:
            self._check_tokenized()

    def _tokenize(self, x):
        """Helper function to tokenize and join the results with a space.

        Args:
            x:

        Returns:
            None
        """
        return " ".join(word_tokenize(x))

    def _check_tokenized(self) -> None:
        """Helper function to check if the content of text_column is tokenized.

        Args:
            None

        Returns:
            None
        """
        if self.df[self.text_column].shape[0] > 200:
            tests = self.df[self.text_column].sample(n=200).tolist()
        else:
            tests = self.df[self.text_column].sample(frac=0.8).tolist()
        num_pass = 0
        for t in tests:
            try:
                if " ".join(word_tokenize(t)) == t:
                    num_pass += 1
            except Exception as E:
                logger.error(f"Could not tokenize and join tokens in {t}: \n {E} ")

        if float(num_pass) / float(len(tests)) < 0.8:
            logger.warning(
                f"It seems that the content of {self.text_column} in the input data frame is not (fully) tokenized.\nThis can lead to poor results. Consider re-instantiating your MWE instance with 'tokenize' flag set to True.\nNote that this might lead to a slower instantiation."
            )

    def build_counts(self, counts_filename: str = "") -> Union[None, Dict]:  # type: ignore
        """Create various count files to be used by downstream methods
        by calling wordview.mwes.mwe_utils.

        Args:
            counts_filename (str): Filename for storing counts.

        Returns:
            None when no counts_filename is provided, otherwise res which is a dictionary of counts.
        """
        logger.info("Creating counts...")
        res = get_counts(
            df=self.df, text_column=self.text_column, mwe_types=self.mwe_types
        )
        if not counts_filename:
            return res
        else:
            try:
                with open(counts_filename, "w") as file:
                    json.dump(res, file)
            except Exception as e:
                logger.error(e)
                raise e

    def extract_mwes(
        self,
        am: str = "pmi",
        mwes_filename: str = "",
        counts_filename: str = "",
        counts: Dict = {},
    ) -> Dict:
        """
        Extract MWEs from counts_filename with respect to the association measure specified by `am`.

        Args:
            am (str): The association measure to be used. Can be any of [pmi, npmi]
            mwes_filename (str): File for storing MWEs. Defaults to None.
            counts_filename (str): File to read counts from.

        Returns:
            Dictionary of MWEs.
        """
        if counts:
            count_data = counts
        else:
            try:
                with open(counts_filename, "r") as file:
                    count_data = json.load(file)
            except Exception as e:
                logger.error(e)
                logger.error(
                    "Counts must be provided either via input argument `counts` or `counts_filename`. Argument `counts` is not specified and it seems like there was an error reading the counts from `counts_filename`."
                )
                raise e

        logger.info(f"Extracting {self.mwe_types} based on {am}")
        mwe_am_dict = calculate_am(
            count_data=count_data, am=am, mwe_types=self.mwe_types
        )
        if mwes_filename:
            try:
                with open(mwes_filename, "w") as file:
                    json.dump(mwe_am_dict, file)
            except Exception as e:
                logger.error(e)
                raise e
            finally:
                return mwe_am_dict
        else:
            return mwe_am_dict
