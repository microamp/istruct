# -*- coding: utf-8 -*-

import unittest

from istruct import istruct


class TestIStruct(unittest.TestCase):
    def test_simple(self):
        person = istruct("first_name", "last_name")
        p = person(first_name="jim", last_name="raynor")

        self.assertEqual(p.first_name, "jim")
        self.assertEqual(p.last_name, "raynor")

    def test_mutation(self):
        person = istruct("first_name", "last_name")
        p = person(first_name="jim", last_name="raynor")

        # cannot be mutated only created
        with self.assertRaises(AttributeError):
            p.first_name = "james"

        # cannot be mutated only created
        with self.assertRaises(AttributeError):
            p.middle_name = "eugene"

    def test_positional(self):
        person = istruct("first_name", "last_name")

        try:
            # positional args strictly disallowed
            person("jim", "raynor")
            assert False, "You should have never reached here!"
        except TypeError as e:
            self.assertEqual(str(e),
                             "No positional arguments are allowed in istruct "
                             "(2 found)")

    def test_required(self):
        person = istruct("first_name", "last_name")

        # without `last_name` (required)
        with self.assertRaises(TypeError):
            person(first_name="jim")

        # without `first_name` (required)
        with self.assertRaises(TypeError):
            person(last_name="raynor")

    def test_defaults(self):
        person = istruct("first_name", "last_name",
                         middle_name="eugene",
                         email=None,
                         contact_no=None)
        p = person(first_name="jim", last_name="raynor",
                   email="jim.raynor@example.com")

        self.assertEqual(p.first_name, "jim")
        self.assertEqual(p.last_name, "raynor")
        self.assertEqual(p.middle_name, "eugene")  # default
        self.assertEqual(p.email, "jim.raynor@example.com")
        self.assertIsNone(p.contact_no)  # default

    def test_bad_args(self):
        try:
            # `first_name` as positional *and* keyword argument
            istruct("first_name", "last_name", first_name="James")
            assert False, "You should have never reached here!"
        except ValueError as e:
            self.assertEqual(str(e),
                             "Each field must be either required or optional, "
                             "not both: 'first_name'")

    def test_repeated_args(self):
        try:
            # `first_name` and `last_name` repeated multiple times
            istruct("first_name", "last_name", "first_name", "last_name",
                    "last_name", "middle_name")
            assert False, "You should have never reached here!"
        except ValueError as e:
            self.assertEqual(str(e),
                             "Each field cannot be present more than once: "
                             "'first_name', 'last_name'")


if __name__ == "__main__":
    unittest.main()
