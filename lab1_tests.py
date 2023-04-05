import subprocess
import re

name1 = "lab1_for.sh"
name2 = "lab1_while.sh"

def test1_reverse():
    command = ['bash', name1, 'a', 'b', 'c']
    res = subprocess.run(command, stdout=subprocess.PIPE)
    assert res.stdout.decode("utf-8") == "c b a\n"

def test1_empty():
    command = ['bash', name1]
    res = subprocess.run(command, stdout=subprocess.PIPE)
    assert res.stdout.decode("utf-8") == " \n"

def test1_single():
    command = ['bash', name1, 'a']
    res = subprocess.run(command, stdout=subprocess.PIPE)
    assert res.stdout.decode("utf-8") == "a\n"

def test2_reverse():
    command = ['bash', name2, 'a', 'b', 'c']
    res = subprocess.run(command, stdout=subprocess.PIPE)
    assert res.stdout.decode("utf-8") == "c b a\n"

def test2_empty():
    command = ['bash', name2]
    res = subprocess.run(command, stdout=subprocess.PIPE)
    assert res.stdout.decode("utf-8") == " \n"

def test2_single():
    command = ['bash', name2, 'a']
    res = subprocess.run(command, stdout=subprocess.PIPE)
    assert res.stdout.decode("utf-8") == "a\n"
test1_reverse()
test1_empty()
test1_single()
print("All tests for \"for\" done succesfully!")

test2_reverse()
test2_empty()
test2_single()
print("All tests for \"while\" done succesfully!")
