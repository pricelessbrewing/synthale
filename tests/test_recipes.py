"""Contains tests for the synthale.recipes module."""

import pybeerxml

from synthale.recipes import MarkdownRecipe, load_file, load_all_files


def test_load_file(capsys):
    """Load the sample XML file and ensure the name is parsed."""
    result = load_file('tests/recipes/weizen.xml')
    assert result[0].recipe.name == 'Weizen'

    result = load_file('tests/recipes/bad-file')
    captured = capsys.readouterr()
    assert result == []
    assert captured.err == ('Error parsing tests/recipes/bad-file: '
                            'syntax error: line 1, column 0\n')


def test_load_all_files():
    """Load all sample XML files and ensure the count is correct."""
    result = load_all_files('tests/recipes')
    result.sort(key=lambda item: item.recipe.name)
    assert len(result) == 2
    assert result[0].recipe.name == 'Coffee Stout'
    assert result[1].recipe.name == 'Weizen'


def test_markdown_recipe_filename():
    """Validate a generated markdown recipe's filename."""
    xml_recipe = pybeerxml.Recipe()
    xml_recipe.name = 'Validate@!#This!'
    recipe = MarkdownRecipe(xml_recipe)
    assert recipe.filename == 'validate_this.md'


def test_markdown_recipe_markdown():
    """Validate the generated markdown."""
    xml_recipe = pybeerxml.Recipe()
    xml_recipe.name = 'Foobar'
    recipe = MarkdownRecipe(xml_recipe)
    assert recipe.markdown == 'Foobar\n======'
