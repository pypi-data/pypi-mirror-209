from Bio.pairwise2 import align


class Align:
    @staticmethod
    def convert_to_chinese(
        a: list[str], b: list[str]
    ) -> tuple[str, str, dict[str, str]]:
        """Converts two lists of strings to a list of Chinese characters where each unique string is represented by a unique character.

        Returns the converted lists and a dictionary mapping the Chinese characters to the original strings.
        """

        # Initialize charcode to the unicode codepoint of the first Chinese character
        charcode = ord("一") - 1

        # Create a dictionary mapping the unique strings to Chinese characters
        seqs = {seq: chr(charcode + ix) for ix, seq in enumerate(set(a + b))}

        seqs_rev = {v: k for k, v in seqs.items()}
        return (
            "".join([seqs[seq] for seq in a]),
            "".join([seqs[seq] for seq in b]),
            seqs_rev,
        )

    @staticmethod
    def chinese_to_list(a: str, seqs_rev: dict[str, str]) -> list[str]:
        """Converts a string of Chinese characters to a list of strings using a dictionary mapping the Chinese characters to the original strings."""
        return [seqs_rev[seq] for seq in a]

    @classmethod
    def align(cls, new: list[str], base: list[str]) -> list[str]:
        """Aligns two lists of strings using the Needleman-Wunsch algorithm.
        Returns a single list of strings where the strings from the two lists are aligned, priorizing the strings from the base list.
        """
        # If either list is empty, return the other list
        if not all((new, base)):
            return new or base

        # Convert the lists to a string of Chinese characters
        a, b, seqs = cls.convert_to_chinese(new, base)

        # Align the strings
        alignments = align.globalxx(a, b)
        new_aligned, base_aligned = alignments[0][0], alignments[0][1]

        # Combine the aligned strings, use the base string as the default
        combined_aligned = [
            base_char if base_char != "-" else new_char
            for new_char, base_char in zip(new_aligned, base_aligned)
        ]

        # Convert the combined string back to a list of strings
        combined = cls.chinese_to_list(combined_aligned, seqs)

        return combined
