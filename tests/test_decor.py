# test_decorators.py
 import pytest
 from decorators import log
 import logging
 from io import StringIO

 def test_log_to_console(capsys):
  @log()
  def my_function(x):
  return x * 2

  result = my_function(5)
  captured = capsys.readouterr()
  assert "my_function" in captured.out
  assert "10" in captured.out
  assert result == 10

 def test_log_to_file(tmp_path):
  log_file = tmp_path / "test.log"

  @log(filename=log_file)
  def another_function(x, y):
  return x - y
  another_function(10, 3)

  with open(log_file, "r") as f:
  log_contents = f.read()
  assert "another_function" in log_contents
  assert "7" in log_contents

 def test_log_exception(capsys):
  @log()
  def failing_function(x):
  raise ValueError("Something went wrong")

  with pytest.raises(ValueError, match="Something went wrong"):
  failing_function(10)

  captured = capsys.readouterr()
  assert "failing_function" in captured.out
  assert "ValueError" in captured.out