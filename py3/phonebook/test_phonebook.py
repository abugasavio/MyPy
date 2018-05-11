import pytest
from phonebook.phonebook import Phonebook


@pytest.fixture
def phonebook():
    phonebook = Phonebook()
    yield phonebook
    phonebook.clear()


def test_lookup_entry_by_name(phonebook):
    phonebook.add('Bob', '12345')
    assert "12345" == phonebook.lookup("Bob")


def test_missing_entry_raise_keyerror(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('missing')


# def test_empty_phonebook_is_constistent():
#     self.assertTrue(self.phonebook.is_consistent())
