from typing import ByteString, Iterable

def _shift(data: Iterable[int], key: int, direction: int) -> bytearray:
    """
    Utility helper that circularly shifts every byte.

    Each byte ``b`` is transformed into ``(b + direction * key) % 256``.

    Parameters
    ----------
    data : Iterable[int]
        Any iterable of integers 0‒255 (`bytes`, `bytearray`, list, generator…).
    key : int
        Shift magnitude – must be in the range 0‒255.
    direction : int
        ``+1`` to shift forward (encrypt), ``-1`` to shift backward (decrypt).

    Returns
    -------
    bytearray
        A *new* ``bytearray`` containing the shifted bytes.
    """
    return bytearray((b + direction * key) % 256 for b in data)

def encrypt(data: ByteString, key: int) -> bytearray:
    """
    Encrypt *data* with a simple byte‑wise Caesar cipher.

    Parameters
    ----------
    data : ByteString
        Plain bytes to hide (`bytes` or `bytearray`).
    key : int
        How far to shift (0‒255).

    Returns
    -------
    bytearray
        Ciphertext as a ``bytearray``.

    Raises
    ------
    ValueError
        If *key* is outside the 0‒255 range.
    """
    if not(0 <= key <= 255):
        raise ValueError("Key must be between 0 and 255")
    return _shift(data, key, +1)


def decrypt(data: ByteString, key: int) -> bytearray:
    """
    Reverse :func:`encrypt` using the same *key*.

    Parameters
    ----------
    data : ByteString
        Ciphertext produced by :func:`encrypt`.
    key : int
        The original key (0‒255).

    Returns
    -------
    bytearray
        The decrypted, original bytes.

    Raises
    ------
    ValueError
        If *key* is outside the 0‒255 range.
    """
    if not (0 <=key <=255):
        raise ValueError("Key must be between 0 and 255")
    return _shift(data, key, -1)