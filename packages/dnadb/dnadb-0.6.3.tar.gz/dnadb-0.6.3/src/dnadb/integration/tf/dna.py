import numpy as np
import numpy.typing as npt
import tensorflow as tf

from ... import dna

BASE_LOOKUP_TABLE = tf.constant(dna.BASE_LOOKUP_TABLE)
BASE_REVERSE_LOOKUP_TABLE = dna.BASE_REVERSE_LOOKUP_TABLE
IUPAC_AUGMENT_LOOKUP_TABLE = dna.IUPAC_AUGMENT_LOOKUP_TABLE

# DNA Sequence Encoding/Decoding -------------------------------------------------------------------

def encode(sequences: str|npt.NDArray[np.str_]) -> npt.NDArray[np.uint8]:
    """
    Encode a DNA sequence into an integer vector representation.
    """
    ascii = tf.strings.unicode_decode(sequences, output_encoding="UTF-8")
    return tf.gather(BASE_LOOKUP_TABLE, ascii - 65)


def decode(sequences: tf.Tensor) -> str:
    """
    Decode a DNA sequence integer vector representation into a string of bases.
    """
    ascii = tf.gather(BASE_REVERSE_LOOKUP_TABLE, sequences)
    return tf.strings.unicode_encode(ascii, output_encoding="UTF-8")


# def encode_kmers(
#     sequences: npt.NDArray[np.uint8],
#     kmer: int,
#     ambiguous_bases: bool = False
# ) -> npt.NDArray[np.int64]:
#     """
#     Convert DNA sequences into sequences of k-mers.
#     """
#     slices = [slice(0, s) for s in sequences.shape[:-1]]
#     edge_slices = slice((kmer - 1) // 2, (kmer - 1) // -2)
#     num_bases = len(BASES + (AMBIGUOUS_BASES if ambiguous_bases else ""))
#     powers = np.arange(kmer).reshape((1,)*len(slices) + (-1,))
#     kernel = num_bases**powers
#     return sp.ndimage.convolve(sequences, kernel)[(*slices, edge_slices)]


# def decode_kmers(
#     sequences: np.ndarray,
#     kmer: int,
#     ambiguous_bases: bool = False
# ) -> npt.NDArray[np.uint8]:
#     """
#     Decode sequence of k-mers into 1-mer DNA sequences.
#     """
#     slices = [slice(0, s) for s in sequences.shape[:-1]]
#     edge_slice = slice(-1, sequences.shape[-1])
#     num_bases = len(BASES + (AMBIGUOUS_BASES if ambiguous_bases else ""))
#     powers = np.arange(kmer - 1, -1, -1)
#     kernel = num_bases**powers
#     edge = (sequences[(*slices, edge_slice)] % kernel[:-1]) // kernel[1:]
#     return np.concatenate([sequences // kernel[0], edge], axis=-1).astype(np.uint8)


# def augment_ambiguous_bases(
#     sequence: str,
#     rng: np.random.Generator = np.random.default_rng()
# ) -> str:
#     """
#     Replace the ambiguous bases in a DNA sequence at random with a valid concrete base.
#     """
#     return decode_sequence(replace_ambiguous_encoded_bases(encode_sequence(sequence), rng))


# def replace_ambiguous_encoded_bases(
#     encoded_sequences: npt.NDArray[np.uint8],
#     rng: np.random.Generator = np.random.default_rng()
# ) -> npt.NDArray[np.uint8]:
#     """
#     Replace the ambiguous bases in an encoded DNA sequence at random with a valid concrete base.
#     """
#     augment_indices = rng.integers(0, 12, size=encoded_sequences.shape)
#     return IUPAC_AUGMENT_LOOKUP_TABLE[encoded_sequences, augment_indices]


# def to_rna(dna_sequence: str) -> str:
#     """
#     Convert an RNA sequence to DNA.
#     """
#     return dna_sequence.replace('T', 'U')


# def to_dna(rna_sequence: str) -> str:
#     """
#     Convert a DNA sequence to RNA.
#     """
#     return rna_sequence.replace('U', 'T')
