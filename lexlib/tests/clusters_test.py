#!/usr/bin/env python3

from pytest import *
from ..clusters import *


class TestClusters:
    # def __init__(self):
        # self.words = ["kAt", "dcg", "dIg", "kAts", "At", "skAt", "sc"]
        # ["A", "c", "I", "i"] = ["A", "c", "I", "i"]

    def test_handles_words_with_onset_and_offset(self):
        words = ["kAt", "dcg", "dIg", "kAts", "skAt"]
        result = clusters(words, ["A", "c", "I", "i"])
        assert result == ["k", "t", "d", "g", "d", "g", "k", "ts", "sk", "t"]

    def test_handles_empty_onset(self):
        words = ["At", "It"]
        result = clusters(words, ["A", "c", "I", "i"])
        assert result == ["t", "t"]

    def test_handles_empty_coda(self):
        words = ["sc", "bi", "fli"]
        result = clusters(words, ["A", "c", "I", "i"])
        assert result == ["s", "b", "fl"]

    def test_handles_multisyllabic_words(self):
        words = ["AktIG", "scftli", "bItmAp"]
        result = clusters(words, ["A", "c", "I", "i"])
        assert result == ["kt", "G", "s", "ftl", "b", "tm", "p"]

    def test_handles_sequential_vowels(self):
        # No, these aren't actually words
        words = ["AiG", "blftiIi", "bAGliclt"]
        result = clusters(words, ["A", "c", "I", "i"])
        assert result == ["G", "blft", "b", "Gl", "lt"]

    def test_positional_handles_monosyllabics_with_onset_and_coda(self):
        words = ["kAt", "dcg", "dIg", "kAts", "skAt"]
        initial, medial, final = positional_clusters(words, ["A", "c", "I", "i"])
        assert initial == ["k", "d", "d", "k", "sk"]
        assert not medial
        assert final == ["t", "g", "g", "ts", "t"]

    def test_positional_handles_empty_onset(self):
        words = ["At", "It"]
        initial, medial, final = positional_clusters(words, ["A", "c", "I", "i"])
        assert not initial
        assert not medial
        assert final == ["t", "t"]

    def test_positional_handles_empty_coda(self):
        words = ["sc", "bi", "fli"]
        initial, medial, final = positional_clusters(words, ["A", "c", "I", "i"])
        assert initial == ["s", "b", "fl"]
        assert not medial
        assert not final

    def test_positional_handles_multisyllabic_words(self):
        words = ["AktIG", "scftli", "bItmAp"]
        initial, medial, final = positional_clusters(words, ["A", "c", "I", "i"])
        assert initial == ["s", "b"]
        assert medial == ["kt", "ftl", "tm"]
        assert final == ["G", "p"]

    def test_positional_handles_sequential_vowels(self):
        # No, these aren't actually words
        words = ["AiG", "blftiIi", "bAGliclt"]
        initial, medial, final = positional_clusters(words, ["A", "c", "I", "i"])
        assert initial == ["blft", "b"]
        assert medial == ["Gl"]
        assert final == ["G", "lt"]
