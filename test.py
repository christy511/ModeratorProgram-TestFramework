"""
Author: Christy Lee
LinkedIn: https://www.linkedin.com/in/christy-lee-798b53276/
GitHub Repository: https://github.com/christy511/Moderator-Program.git
"""

from test_functions import is_valid_name, is_chronological

# valid: A-Z english characters (upper/lower) , space char, -
# invalid: a character not in the above list, only space, empty
try:
    # 'try' tests code that may or may not have exceptions
    # 'assert' tests if the whole statement is true. false -> function does not continue
    assert is_valid_name('adam') == True
    assert is_valid_name('adam-ben') == True
    assert is_valid_name('adam ben') == True
    assert is_valid_name('adam - ben - cat ') == True
    assert is_valid_name('aDaM') == True
    assert is_valid_name('J E F F') == True
    assert is_valid_name('-') == True
    assert is_valid_name('47474') == False
    assert is_valid_name('$%^$**') == False
    assert is_valid_name('adam - 123') == False
    assert is_valid_name('ben/adam') == False
    assert is_valid_name(124) == False
    assert is_valid_name(68686.7666) == False
    assert is_valid_name(True) == False
    assert is_valid_name('') == False
    assert is_valid_name('$$$$') == False
    assert is_valid_name('   ') == False
    assert is_valid_name('[]') == False
    assert is_valid_name('ok.  cool') == False
    print('is_valid_name has passed.')
    
except:
    # this will only be executed if test code has error
    print('is_valid_name has failed.')


try:
    assert is_chronological('2022-09-12T00:00:00', '2022-10-10T19:30:05') == True
    assert is_chronological('2022-10-10T19:30:05', '2022-09-12T00:00:00') == False
    assert is_chronological('2022-10-10T19:30:05', 'hi') == False
    assert is_chronological(123, '2022-10-10T19:30:05') == False
    assert is_chronological('20-09-12T00:00:00', '2022-10-10T19:30:05') == False
    assert is_chronological('2022-12-12T00:00:00', '2022-10-10T19:30:05') == False
    assert is_chronological('', '2022-10-10T19:30:05') == False
    assert is_chronological('1996-09-12T16:30:16', '1996-09-12T16:30:15') == False
    assert is_chronological('1996-09-12T16:30:16', '1996-09-12T16:30:16') == False
    assert is_chronological(True, False) == False
    assert is_chronological('   ', '.') == False
    assert is_chronological('slay', 'slay') == False
    assert is_chronological(6686868.909090, 46464.4949) == False
    print('is_chronological has passed.')
except:
    print('is_chronological has failed.')
