"""
the cookie Jar class plus a solid pytest suite.

Classes & state: Jar encapsulates state (_size, _capacity) and behavior (methods).
The leading underscore is a Python convention for “internal” attributes.

__init__: the constructor validates inputs up front, a best practice to keep objects always-valid.

__str__: defines the human-readable representation. Repeating a string with * is a Pythonic way to render n cookies

Defensive checks: both deposit and withdraw validate type and domain (non-negative, within capacity/availability)
and raise ValueError on violations—exactly what the spec expects.

Properties: @property exposes read-only attributes so users can access jar.size
and jar.capacity like fields, but you keep control internally.

What @property does
@property turns a method into an attribute-like getter.
With it, you can write jar.capacity (not jar.capacity()),
but under the hood Python calls the function to compute/return the value.

So in our class:
self._capacity and self._size are the internal (“private-ish”) fields.
The leading underscore is a Python convention: “this is for internal use.”

capacity and size are the public read-only attributes that expose those values safely.


"""


class Jar:
    def __init__(self, capacity = 12):
        # non-negative int capacity
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError('capacity must be a non-negative int')
        self._capacity = capacity
        self._size = 0 # cookies currently in the jar

    def __str__(self):
        # n == size == number of emojis
        return '🍪' * self._size

    def deposit(self, n):
        # n cookies
        if not isinstance(n, int) or n < 0:
            raise ValueError('deposit amount must be a non-negative int')
        if self._size + n > self._capacity:
            raise ValueError('deposit would exceed capacity')
        self._size += n

    def withdraw(self, w):
        # remove w cookies, error if not enough cookies to remove
        if not isinstance(w, int) or w < 0:
            raise  ValueError('withdraw amount must be a non-negative int')
        if w > self._size:
            raise ValueError('not enough cookies to withdraw')
        self._size -= w

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size