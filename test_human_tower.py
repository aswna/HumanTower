#!/usr/bin/env python
# encoding: utf-8

"""Unit tests for the implementation of Human Tower."""

import unittest

from human_tower import PERSON
from human_tower import tower_sort


class HumanTowerTest(unittest.TestCase):
    def test_human_tower_consists_of_the_largest_possible_number_of_people(self):
        self._no_people_create_1_length_empty_tower()
        self._one_person_creates_1_length_tower_of_the_person()
        self._two_people_with_equal_weight_and_height_create_1_length_tower()
        self._two_people_with_equal_weight_creates_1_length_tower_of_the_higher_person()
        self._two_people_with_equal_height_creates_1_length_tower_of_the_heavier_person()
        self._test_original_example_at_craftsmanship_sv_cmu_edu()
        self._test_example_for_three_people_with_limiting_height()
        self._test_example_for_three_people_with_limiting_weight()
        self._test_example_for_six_people_with_limiting_height()
        self._test_example_for_six_people_with_limiting_weight()

    def _no_people_create_1_length_empty_tower(self):
        no_people = [()]
        self._assert_tower_sort((1, [()]), no_people)

    def _one_person_creates_1_length_tower_of_the_person(self):
        person = [PERSON(70, 180)]
        self._assert_tower_sort((1, [PERSON(70, 180)]), person)

    def _two_people_with_equal_weight_creates_1_length_tower_of_the_higher_person(self):
        two_people_with_equal_weight = [PERSON(70, 180), PERSON(70, 181)]
        self._assert_tower_sort((1, [PERSON(70, 181)]), two_people_with_equal_weight)

    def _two_people_with_equal_height_creates_1_length_tower_of_the_heavier_person(self):
        two_people_with_equal_height = [PERSON(70, 180), PERSON(71, 180)]
        self._assert_tower_sort((1, [PERSON(71, 180)]), two_people_with_equal_height)

    def _two_people_with_equal_weight_and_height_create_1_length_tower(self):
        two_equal_people = [PERSON(70, 180), PERSON(70, 180)]
        self._assert_tower_sort((1, [PERSON(70, 180)]), two_equal_people)

    def _test_original_example_at_craftsmanship_sv_cmu_edu(self):
        example_input = [PERSON(65, 100), PERSON(70, 150), PERSON(56, 90),
                         PERSON(75, 190), PERSON(60, 95), PERSON(68, 110)]
        expected_output = (6, [PERSON(75, 190), PERSON(70, 150),
                               PERSON(68, 110), PERSON(65, 100),
                               PERSON(60, 95), PERSON(56, 90)])
        self._assert_tower_sort(expected_output, example_input)

    def _test_example_for_three_people_with_limiting_height(self):
        example_input = [PERSON(90, 150), PERSON(100, 160), PERSON(110, 100)]
        expected_output = (2, [PERSON(100, 160), PERSON(90, 150)])
        self._assert_tower_sort(expected_output, example_input)

    def _test_example_for_three_people_with_limiting_weight(self):
        example_input = [PERSON(90, 150), PERSON(100, 160), PERSON(80, 170)]
        expected_output = (2, [PERSON(100, 160), PERSON(90, 150)])
        self._assert_tower_sort(expected_output, example_input)

    def _test_example_for_six_people_with_limiting_height(self):
        example_input = [PERSON(120, 160), PERSON(110, 190), PERSON(100, 160),
                         PERSON(90, 180), PERSON(80, 170), PERSON(70, 150)]
        expected_output = (4, [PERSON(110, 190), PERSON(90, 180),
                               PERSON(80, 170), PERSON(70, 150)])
        self._assert_tower_sort(expected_output, example_input)

    def _test_example_for_six_people_with_limiting_weight(self):
        example_input = [PERSON(110, 200), PERSON(80, 190), PERSON(100, 180),
                         PERSON(90, 170), PERSON(80, 160), PERSON(70, 150)]
        expected_output = (5, [PERSON(110, 200), PERSON(100, 180),
                               PERSON(90, 170), PERSON(80, 160),
                               PERSON(70, 150)])
        self._assert_tower_sort(expected_output, example_input)

    def _assert_tower_sort(self, expected_result, people):
        self.assertEqual(expected_result, tower_sort(people))


def run_unit_tests():
    human_tower = unittest.TestLoader().loadTestsFromTestCase(HumanTowerTest)
    all_suites = unittest.TestSuite([human_tower])
    unittest.TextTestRunner(verbosity=2).run(all_suites)

if __name__ == '__main__':
    run_unit_tests()
