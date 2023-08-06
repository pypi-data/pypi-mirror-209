import base64, string, random, io, os

class InvalidTokenFoundError(Exception):
    def __init__(self, character: str | None = None, /) -> None:
        """Raised if an invalid character or token is present within a string of text
        during the encryption / decryption phase.

        Args:
            character (str | None, optional): The invalid token that was present. Defaults to None.
        """
        if character is None:
            super().__init__()
        else:
            super().__init__(f"Invalid token \"{character}\" is not defined as printable.")

class _EncryptionKeys():
    def __init__(self, __min_length: int, __max_length: int, /) -> None:
        """Generates a pair of encryption and decryption keys at a desired length.

        Args:
            __min_length (int, optional): The minimum length that a key should stand.
            __max_length (int, optional): The maximum length that a key should stand.
        """
        self.__min_length: int = __min_length
        self.__max_length: int = __max_length
        self._encryption_keys: dict[bytes, str] | None = None
        self._decryption_keys: dict[str, bytes] | None = None
        self.__generate_keys(seed = os.urandom(1024))

    def __generate_keys(self, *, seed: bytes) -> None:
        """
        Generates a list of keys bound to a list of characters which are defined in string's printable character list.
        Valid characters: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

        Args:
            seed (bytes): The random seed to generate keys on.
        """
        random.seed(seed)
        encryption_keys: dict[bytes, str] = {}
        decryption_keys: dict[str, bytes] = {}
        characters = string.hexdigits

        for character in string.printable:
            key = ''.join([random.choice(characters) for _ in range(random.randint(self.__min_length, self.__max_length))])
            __char = base64.b64encode(bytes(character.encode().hex(), "UTF-8"))
            encryption_keys[__char] = key
            decryption_keys[key] = __char

        self._encryption_keys = encryption_keys
        self._decryption_keys = decryption_keys
        random.seed(None)

class SecurityLevel():
    def __init__(self, a: int, b: int, /) -> None:
        """
        Args:
            a (int): Minimum key length.
            b (int): Maximum key length.
        """
        self._a: int = a
        self._b: int = b
    @classmethod
    def extremely_low(cls):
        return cls(10, 15)
    @classmethod
    def very_low(cls):
        return cls(10, 30)
    @classmethod
    def low(cls):
        return cls(30, 75)
    @classmethod
    def medium(cls):
        return cls(75, 150)
    @classmethod
    def high(cls):
        return cls(150, 500)
    @classmethod
    def very_high(cls):
        return cls(500, 1000)
    @classmethod
    def extremely_high(cls):
        return cls(1000, 1500)
    @classmethod
    def custom(cls, _min: int, _max: int):
        if _min > _max:
            raise ValueError("Maximum key length must be a greater value than minimum key length.")
        elif _min < 10:
            raise ValueError("Minimum key length must be greater than or equal to 10.")
        return cls(_min, _max)

class SubstitutionCipher(_EncryptionKeys):
    def __init__(self, security_level: SecurityLevel = SecurityLevel.medium()) -> None:
        """A simple substitution cipher encryption tool to encode strings of text.

        Args:
            security_level (SecurityLevel, optional): The security level (length) of each encryption / decryption key. Defaults to SecurityLevel.medium().
        """
        if not isinstance(security_level, SecurityLevel):
            raise TypeError(f"Argument security_level cannot be of type {type(security_level)}")
        super().__init__(security_level._a, security_level._b)
    def encrypt(self, s: str, /) -> bytes:
        """Encrypts a string of text using an arrangement of encryption keys.

        Args:
            s (str): The string to encrypt.

        Raises:
            InvalidTokenFoundError: If an unidentified character is present within the string (s), an InvalidTokenFoundError will be raised.

        Returns:
            bytes: An encrypted byte-string of the original text (s).
        """
        __encrypted_string: io.StringIO = io.StringIO()
        for character in s:
            character = base64.b64encode(character.encode().hex().encode())
            if character not in self._encryption_keys:
                raise InvalidTokenFoundError(character) 
            __encrypted_string.write(self._encryption_keys.get(character))
        return bytes(__encrypted_string.getvalue(), "UTF-8")
    def decrypt(self, s: bytes, /) -> bytes:
        """Decrypts a string of text using an arrangement of decryption keys.

        Args:
            s (bytes): The string to decrypt.

        Raises:
            InvalidTokenFoundError: If an invalid token (or key) is present within the string (s), an InvalidTokenFoundError will be raised.

        Returns:
            bytes: An unencrypted byte-string of the original encrypted text (s).
        """
        __decrypted_string: io.StringIO = io.StringIO()
        while s:
            __match = False
            for k in self._decryption_keys:
                if s.startswith(bytes(k, "UTF-8")):
                    __decrypted_string.write(bytearray.fromhex(base64.b64decode(self._decryption_keys[k].decode()).decode()).decode())
                    s = s[len(k):]
                    __match = True
                    break
            if not __match:
                raise InvalidTokenFoundError()
        return bytes(__decrypted_string.getvalue(), "UTF-8")