#!/usr/bin/env python
# encoding: utf-8

"""TDD implementation of the Human Tower presented on craftsmanship.sv.cmu.edu.

A circus is designing a tower routine consisting of people standing atop one
another's shoulders. For practical and aesthetic reasons, each person must be
both shorter and lighter than the person below him or her.

Given the heights and weights of each person in the circus, write a method to
compute the largest possible number of people in such a tower.
"""


from collections import namedtuple


PERSON = namedtuple('Person', 'weight height')


def tower_sort(people):
    longest_tower = _build_longest_tower([], sorted(people, reverse=True))
    return (len(longest_tower), longest_tower)


def _build_longest_tower(tower_built, remaining_people_sorted):
    if not remaining_people_sorted:
        return tower_built

    longest_tower = tower_built
    for candidate in remaining_people_sorted:
        remaining_people = _remove_candidate(remaining_people_sorted, candidate)
        tower = _build_tower(tower_built, candidate, remaining_people)
        longest_tower = _get_the_longer_tower(tower, longest_tower)

    return longest_tower


def _build_tower(tower_built, candidate, remaining_people):
    if not tower_built:
        tower = _build_longest_tower([candidate], remaining_people)
    elif _candidate_fits_to_top(tower_built, candidate):
        higher_tower = _add_candidate(tower_built, candidate)
        tower = _build_longest_tower(higher_tower, remaining_people)
    else:
        tower = tower_built

    return tower


def _remove_candidate(people, candidate):
    remaining_people = list(people)
    remaining_people.remove(candidate)
    return remaining_people


def _add_candidate(tower_built, candidate):
    higher_tower = list(tower_built)
    higher_tower.append(candidate)
    return higher_tower


def _candidate_fits_to_top(tower, candidate):
    top_person = tower[-1]
    return (candidate.weight < top_person.weight and
            candidate.height < top_person.height)


def _get_the_longer_tower(tower1, tower2):
    return tower1 if len(tower1) > len(tower2) else tower2
