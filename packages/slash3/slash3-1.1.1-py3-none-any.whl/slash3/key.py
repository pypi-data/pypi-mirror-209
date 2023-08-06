from typing import Any, Optional, Union

from slash3.logging import logger

MAX_LENGTH = 1024


class S3Key:
    """
    An Amazon Web Services S3 key.
    """

    def __init__(self, key: Optional[str] = None) -> None:
        logger.debug('Creating new S3Key from "%s"', key)
        key = key or ""

        if key.startswith("/"):
            raise ValueError(
                f'S3 keys cannot start with the delimiter "/" ("{key}")',
            )

        if "//" in key:
            raise ValueError(
                f'S3 keys cannot contain consecutive "/" delimiters ("{key}")',
            )

        if len(key) > MAX_LENGTH:
            raise ValueError(
                f"S3 keys cannot be longer than {MAX_LENGTH} characters "
                f'("{key}" has {len(key)} characters)',
            )

        self._key = key or ""

    def __add__(self, other: str) -> "S3Key":
        return self.append(other)

    def __eq__(self, other: Any) -> bool:
        return self._key == str(other)

    def __len__(self) -> int:
        return len(self._key)

    def __repr__(self) -> str:
        return self._key

    def __truediv__(self, other: str) -> "S3Key":
        return self.join(other)

    def append(self, suffix: str) -> "S3Key":
        """
        Appends a string to the key.

        ```python
        images = S3Key("images/staff-")

        steve = images.append("steve.jpg")
        # "images/staff-steve.jpg"

        # Or use "+":
        penny = images + "penny.jpg"
        # "images/staff-penny.jpg"
        ```

        To add a suffix with a "/" delimiter, use `join()` instead.
        """

        logger.debug('Appending base "%s" and suffix "%s"', self._key, suffix)

        if self._key.endswith("/") and suffix.startswith("/"):
            base = self.normal_right(self._key, slash=True)
            logger.debug('Base normalised to "%s"', base)
            suffix = self.normal_left(suffix)
        else:
            base = self._key

        return S3Key(base + suffix)

    def join(self, suffix: str) -> "S3Key":
        """
        Joins a string to the key with a "/" delimiter.

        ```python
        images = S3Key("images/staff")

        steve = images.join("steve.jpg")
        # "images/staff/steve.jpg"

        # Or use "/":
        penny = images / "penny.jpg"
        # "images/staff/penny.jpg"
        ```

        To append a string without a "/" delimiter, use `append()` instead.
        """

        logger.debug('Joining base "%s" and suffix "%s"', self._key, suffix)

        base = self.normal_right(self._key, slash=True) if self._key else self._key
        logger.debug('Base normalised to "%s"', base)

        suffix = self.normal_left(suffix)
        logger.debug('Suffix normalised to "%s"', suffix)

        return S3Key(base + suffix)

    @property
    def key(self) -> str:
        """
        Key.

        For example, "private/clowns.jpg".
        """

        return self._key

    @property
    def leaf(self) -> str:
        """
        Key leaf.

        In a file system metaphor, the leaf would be the file's name.

        For example, the leaf of "private/clowns.jpg" is "clowns.jpg".
        """

        return self.relative_to(self.parent)

    @staticmethod
    def normal_left(key: str, slash: bool = False) -> str:
        """
        Normalises the left of the key.

        If `slash` is true then the key is returned with exactly one leading
        slash, otherwise the key is returned with no leading slashes.
        """

        while key.startswith("/"):
            key = key[1:]

        return "/" + key if slash else key

    @staticmethod
    def normal_right(key: str, slash: bool = False) -> str:
        """
        Normalises the right of the key.

        If `slash` is true then the key is returned with exactly one trailing
        slash, otherwise the key is returned with no trailing slashes.
        """

        while key.endswith("/"):
            key = key[:-1]

        return key + "/" if slash else key

    @property
    def parent(self) -> "S3Key":
        """
        Parent key.

        For example, the parent of "private/clowns.jpg" is "private/".
        """

        logger.debug('Determining the parent of key "%s"', repr(self))

        if self._key == "":
            logger.debug("Empty key has no parent")
            return self

        if self._key.endswith("/"):
            key = self._key[0:-1]
        else:
            key = self._key

        if "/" not in key:
            logger.debug("Root key parent is the root")
            return S3Key()

        index = key.rindex("/") + 1

        logger.debug('Final "/" in key "%s" is at index %s', self._key, index)

        parent_key = self._key[0:index]

        logger.debug('Key "%s" parent is "%s"', self._key, parent_key)

        return S3Key(parent_key)

    def relative_to(self, parent: Union["S3Key", str]) -> str:
        """
        Gets the relative key path from this key to a `parent` key.

        For example, the relative path to "private/clowns.jpg" from parent
        "private" is "clowns.jpg".
        """

        logger.debug(
            'Calculating the relative key from "%s" to "%s"',
            self,
            parent,
        )

        parent = str(parent)
        normal = self.normal_right(parent, slash=True) if parent else parent

        logger.debug('Normalised the parent key to "%s"', normal)

        if not self._key.startswith(normal):
            raise ValueError(f'"{parent}" is not a parent of "{self}"')

        relative_key = self._key[len(normal) :]  # noqa: E203

        logger.debug(
            'The relative path from "%s" to "%s" is "%s"',
            parent,
            self,
            relative_key,
        )

        return relative_key
