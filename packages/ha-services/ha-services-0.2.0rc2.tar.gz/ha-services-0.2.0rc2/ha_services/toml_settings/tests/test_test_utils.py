from pathlib import Path
from unittest import TestCase

from ha_services.toml_settings.test_utils.data_class_utils import replace_dataclass_values, replace_path_values
from ha_services.toml_settings.tests.fixtures import ComplexExample, PathExample2


class TestUtilsTestCase(TestCase):
    def test_replace_dataclass_values(self):
        instance = ComplexExample()

        # Check before:
        self.assertEqual(instance.foo, 'bar')
        self.assertEqual(instance.sub_class_one.number, 123)
        self.assertEqual(instance.sub_class_two.something, 0.5)

        new_data = {
            'foo': 'NEW',
            'sub_class_two': {
                'something': 456,
            },
        }
        replace_dataclass_values(instance, data=new_data)

        # Check after:
        self.assertEqual(instance.foo, 'NEW')
        self.assertEqual(instance.sub_class_one.number, 123)  # unchanged?
        self.assertEqual(instance.sub_class_two.something, 456)

    def test_replace_path_values(self):
        instance = PathExample2()

        # Check before:
        self.assertEqual(instance.path, Path('/foo/baz'))
        self.assertEqual(instance.sub_path.path, Path('/foo/bar'))

        replace_path_values(instance)

        # Check after:
        self.assertEqual(instance.path, '/foo/baz')
        self.assertEqual(instance.sub_path.path, '/foo/bar')
