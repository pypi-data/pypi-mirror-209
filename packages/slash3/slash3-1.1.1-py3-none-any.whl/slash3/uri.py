from re import match
from typing import Any, Optional, Union

from slash3.key import S3Key


class S3Uri:
    """
    An Amazon Web Services S3 URI.

    To construct a URI from a bucket's name and optional key, use the
    `to_uri()` class method instead.
    """

    def __init__(self, uri: str) -> None:
        m = match(r"[sS]3:\/\/([^/]*)(\/(.*))?", uri)

        if not m:
            raise ValueError(f'"{uri}" is not an S3 URI')

        self._bucket = str(m.group(1))
        self._key = S3Key(m.group(3))

    def __add__(self, suffix: str) -> "S3Uri":
        return self.append(suffix)

    def __eq__(self, other: Any) -> bool:
        return self.uri == str(other)

    def __repr__(self) -> str:
        return self.uri

    def __truediv__(self, suffix: str) -> "S3Uri":
        return self.join(suffix)

    def append(self, other: str) -> "S3Uri":
        """
        Appends a string to the URI.

        ```python
        images = S3Uri("s3://circus/staff-")

        steve = images.append("steve.jpg")
        # "s3://circus/staff-steve.jpg"

        # Or use "+":
        penny = images + "penny.jpg"
        # "s3://circus/staff-penny.jpg"
        ```

        To add a suffix with a "/" delimiter, use `join()` instead.
        """

        return S3Uri.to_uri(self._bucket, self._key.append(other))

    @property
    def bucket(self) -> str:
        """
        Bucket.
        """

        return self._bucket

    def join(self, suffix: str) -> "S3Uri":
        """
        Joins a string to the URI with a "/" delimiter.

        ```python
        images = S3Uri("s3://circus/staff")

        steve = images.join("steve.jpg")
        # "s3://circus/staff/steve.jpg"

        # Or use "/":
        penny = images / "penny.jpg"
        # "s3://circus/staff/penny.jpg"
        ```

        To append a string without a "/" delimiter, use `append()` instead.
        """

        return S3Uri.to_uri(self._bucket, self._key.join(suffix))

    @property
    def key(self) -> S3Key:
        """
        Key.
        """

        return self._key

    @property
    def leaf(self) -> str:
        """
        URI leaf.

        In a file system metaphor, the leaf would be the file's name.

        For example, the leaf of "s3://circus/private/clowns.jpg" is
        "clowns.jpg".
        """

        return self.key.leaf

    @property
    def parent(self) -> "S3Uri":
        """
        Parent URI.

        For example, the parent of "s3://circus/private/clowns.jpg" is
        "s3://circus/private/".
        """

        return S3Uri.to_uri(self._bucket, self.key.parent)

    def relative_to(self, parent: Union["S3Uri", str]) -> str:
        """
        Gets the relative key path from this URI to a `parent` URI.

        For example, the relative path to "s3://circus/private/clowns.jpg" from
        "s3://circus/" is "private/clowns.jpg".
        """

        parent = S3Uri(parent) if isinstance(parent, str) else parent

        if parent._bucket != self._bucket:
            raise ValueError(
                f'There is no relative path from "{parent}" to "{self}" '
                "because these URIs describe different buckets"
            )

        return self._key.relative_to(parent.key)

    @staticmethod
    def to_string(bucket: str, key: Optional[Union[S3Key, str]]) -> str:
        """
        Constructs a string S3 URI from a bucket and optional key.

        To construct an `S3Uri` instance, use `to_uri()` instead.
        """

        return f"s3://{bucket}/{key or ''}"

    @classmethod
    def to_uri(
        cls,
        bucket: str,
        key: Optional[Union[S3Key, str]] = None,
    ) -> "S3Uri":
        """
        Constructs an `S3Uri` from a bucket and optional key.
        """

        return cls(cls.to_string(bucket, key=key))

    @property
    def uri(self) -> str:
        """
        URI.
        """

        return self.to_string(self._bucket, self._key)
