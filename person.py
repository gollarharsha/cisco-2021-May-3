#!/usr/bin/env python3

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return f'{self.first} {self.last}'

    def greet(self):
        return f'Hello, {self.fullname()}'
