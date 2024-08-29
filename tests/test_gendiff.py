from gendiff.gen_diff import generate_diff


def test_gendiff():
    answer = open('tests/fixtures/right_answer.txt')
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == answer.read()
    answer.close()
