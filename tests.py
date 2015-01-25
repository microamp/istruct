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

        # strictly disallow positional args
        with self.assertRaises(TypeError):
            person("jim", "raynor")

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


if __name__ == "__main__":
    unittest.main()
