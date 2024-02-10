"""
Author: Christy Lee
LinkedIn: https://www.linkedin.com/in/christy-lee-798b53276/
GitHub Repository: https://github.com/christy511/Moderator-Program.git
"""
import sys

all_args = ['-task', '-log', '-forum', '-words', '-people']
provided_args = sys.argv[1:]
# [1:] represents second position onwards so the arguments after after moderator.py onwards is saved

given_args =  provided_args[0:10:2]     # task, log, forum, words, people
# [::2] represents every second word
vals = provided_args[1:10:2]
# files like <task>, <filename>

i = 0
while i < len(all_args):
    # runs through all the elements in all_args

    arg = all_args[i]
    if bool(given_args.count(arg)) == False:
        # counts num of times arg appears in given_args. 0 times (means the argument is not provided)-> false, 1 time -> true
      
        print(f'No {arg.strip("-")} arguments provided.')
        sys.exit()
        #stops program immediately

    i += 1

task_index = (given_args.index('-task'))
# .index() checks which position '-task' is in

task_val = vals[task_index]
# check the above position's VALUE in vals

valid_task_list = ['rank_people', 'validate_forum', 'censor_forum', 'evalauate_forum']
valid_task_val = bool(valid_task_list.count(task_val))
# counts num of times task_val appears in the above list. 0 times (means it's an invalid response, not any of the values from valid_task_list) -> false, 1 time -> true 

if valid_task_val == False:
     print('Task argument is invalid.')
     sys.exit()

i = 0
while i < len(given_args):
    arg_name = given_args[i]
    arg_val = vals[i]

    if arg_name != '-task' and arg_name != '-log':
        try:
            open(arg_val, 'r')      #opens file to check if is readable
        except:
            print(f'{arg_val} cannot be read.')
            sys.exit()
    i += 1

print('Moderator program starting...')





# Validating and interpreting the people files

def validate_header(people_val_data):
# validating header
    
    if people_val_data[0].strip() == '' or people_val_data[1].strip() != '':
#strips \n bc people_val_data prints out the file with '\n' after each line.
# first line should have text, second line should be empty 
        
        return False
    
    else:
        return True

def validate_score(score):
# validating personality score
    
    try:
        score = int(score)       # change to int form since it was previously in list format
        if score >= -10 and score <= 10:
            return True
        else:
            return False
    except:
        return False

def is_valid_name(name):
# validating name
    
    if type(name) != str:
        return False
    if name.count(' ') > 1:
        return False

    name = name.replace(' ', '')
    name = name.replace('-', '')

    if name.isalpha():
        return True
    else:
        return False


poeple_ind = given_args.index('-people')   
people_val = vals[poeple_ind]

log_ind = given_args.index('-log')
log_val = vals[log_ind]
log_file = open(log_val, 'w')       # writing to the log file

people_val_data = open(people_val, 'r').readlines()      # interpreting people file

header_valid = validate_header(people_val_data)
if header_valid  == False:
    log_file.write('Error: people file read. The people file header is incorrectly formatted\n')
    sys.exit()


start = 2       # because names&scores only appear from 3rd line onwards

all_names = []
all_scores = []

while start < len(people_val_data):
    # runs through all lines until end of file

    entry = people_val_data[start].strip().split(',')
    if len(entry) != 2:    # e.g [Plato,5] -> 2 elements. checking format of people entry
        log_file.write(f'Error: people file read. The people entry is invalid on line {start + 1}\n')
        sys.exit()
    else:
        name = entry[0]
        score = entry[1]
        name_valid = is_valid_name(name)
        score_valid = validate_score(score)
        if name_valid == False:
            log_file.write(f"Error: people file read. The user's name is invalid on line {start + 1}\n")
            sys.exit()
        if score_valid == False:
            log_file.write(f"Error: people file read. The personality score is invalid on line {start + 1}\n")
            sys.exit()

        all_scores.append(int(score))     #adding up all scores
        all_names.append(name)       #adding up all names in list

    start += 1


zipped_entry = list(zip(all_names, all_scores))
# aggregates the names and scores in tuple and makes into list

def sort_on(pair):
    return pair[1]      # considering position of score (bc score is second position)

sorted_people = sorted(zipped_entry, reverse=True, key=sort_on)
# sorted -> ascending order. reverse -> descending
# key tells you to sort based on second element which is the score

people_write = open(people_val, 'w')
people_write.write(people_val_data[0])      # score 
people_write.write(people_val_data[1])      # name

i = 0
while i < len(sorted_people):
# goes through users that are ranked based on descending order of scores 
    people = sorted_people[i]
    name = people[0] 
    score = people[1]
    people_write.write(f'{name},{score}\n')

    i += 1




# Validating a file containing the posts in the forum

import datetime

def is_chronological(earlier_dt: str, later_dt: str) -> bool:
    if type(earlier_dt) != str or type(later_dt) != str:
        return False

    try:
        datetime.datetime.strptime(earlier_dt, '%Y-%m-%dT%H:%M:%S')
        datetime.datetime.strptime(later_dt, '%Y-%m-%dT%H:%M:%S')
    except:
        return False

    if later_dt > earlier_dt:
        return True
    else:
        return False


forum_ind = given_args.index('-forum')
forum_val = vals[forum_ind]

forum_data = open(forum_val, 'r').readlines()

header_valid = validate_header(forum_data)
# validates header

if header_valid == False:
    log_file.write('Error: forum file read. The forum file header is incorrectly formatted\n')
    sys.exit()


i = 2     # starting from 3rd line onwards since skipping past the header
prev_post_date = None 
forum_saved_data = []
post_occured = True    # post has occured

while i < len(forum_data):
# runs through all lines of entire forum file
    group = forum_data[i:i+3]
    # i:i+3 represents lines 3 to 5 -> datetime, username, post/reply (line 6 is excluded) 
    
    #  the if statement pulls out replies since there is a tab character before all replies
    if group[0].count('    ') == 1 and group[1].count('    ') == 1 and group[2].count('    ') == 1:     
            # group[0] -> datestring, group[1] -> username, group[2] -> reply
        
        reply = group
        
        if post_occured == False:
        # if post has not occured -> replies are placed before the actual post
            
            log_file.write(f'Error: forum file read. The reply is placed before a post on line {i + 1}\n')
            sys.exit()

        date = reply[0].strip()
        name = reply[1].strip()

    # validates datetime format
        try:
            datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        except:
            log_file.write(f'Error: forum file read. The datetime string is invalid on line {i + 1}\n')
            sys.exit()

    # validates name
        if is_valid_name(name) == False:
            log_file.write(f"Error: forum file read. The user's name is invalid on line {i + 2}\n")
            sys.exit()

    # validates chronological order of datetime
        if is_chronological(prev_post_date, date) == False:
            log_file.write(f'Error: forum file read. The reply is out of chronological order on line {i + 1}\n')
            sys.exit()
            
    # pulls out posts
    elif group[0].count('    ') != 1 and group[1].count('    ') != 1 and group[2].count('    ') != 1:
        post = group
        
        date = post[0].strip()
        name = post[1].strip()

    # validates datetime format
        try:
            datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        except:
            log_file.write(f'Error: forum file read. The datetime string is invalid on line {i + 1}\n')
            sys.exit()
        
    # validates name
        if is_valid_name(name) == False:
            log_file.write(f"Error: forum file read. The user's name is invalid on line {i + 2}\n")
            sys.exit()

        post_occured = True

# post is out of chronological order error appears here
        
        prev_post_date = date


    else:
    # inconsistent tab indentation on datetime/username/post or reply -> invalid format 
        
        if group[0].count('    ') == 1:
            log_file.write(f'Error: forum file read. The post has an invalid format on line {i+1}\n')
            sys.exit()
        elif group[1].count('    ') == 1:
            log_file.write(f'Error: forum file read. The post has an invalid format on line {i+1}\n')
            sys.exit()
        elif group[2].count('    ') == 1:
            log_file.write(f'Error: forum file read. The post has an invalid format on line {i+1}\n')
            sys.exit()

    forum_saved_data.append(group)      # saving the group of datetime+user+post
    i += 3      # skips next 3





# Reading and interpreting the word file, censoring

words_ind = given_args.index('-words')
words_val = vals[words_ind]

words_data = open(words_val, 'r').readlines()


header_valid = validate_header(words_data)

if header_valid == False:
    log_file.write('Error: words file read. The words file header is incorrectly formatted\n')
    sys.exit()

i = 2
banned_words = []
while i < len(words_data):
# goes through entire words file 
    
    word = words_data[i].strip()
    if len(word) < 1:
# if there are no characters in the word (blank line)
        
        log_file.write(f'Error: words file read. The banned word is invalid on line {i + 1}\n')
        sys.exit()

    banned_words.append(word)         # list of banned words
    i += 1

i = 0
while i < len(forum_saved_data):    # goes through entire post/reply
    k = 0
    while k < len(banned_words):    # goes through each banned word
        word = banned_words[k]
        group = forum_saved_data[i]
        msg  = group[2]     # filters out third position of the group which is the message
        ms_wds = msg.split()    # split message into word by word

        j = 0
        while j < len(ms_wds):      # goes through each word
            wd = ms_wds[j]      # taking every word from the split message (L306)
            indx = wd.find(word)    # checking if the above word ^ has any of the banned words 
            if indx != -1:      # checking if ^ is found (-1 indicates not found)
                if len(wd) > len(word) and (wd[0].isalpha() and wd[-1].isalpha()):      # 
                    j += 1
                    continue
                else:
                    replaced_wd = wd.replace(wd[indx:len(word)], '*'*len(word))     # replace the overlapped banned words with *    
                    ms_wds[j] = replaced_wd     # replacing the new banned words with * in the original message

            j += 1
        msg = ' '.join(ms_wds)  # ' ' represents the space before each word to form a sentence (since it was originally split to word by word)
        group[2] = msg      # third position of grouping is the message
        if group[0].count('    ') > 1:
            group[2] = '    ' + group[2]
        forum_saved_data[i] = group     # updating the old file

        k += 1
    i += 1

forum_write = open(forum_val, 'w')

i = 0

forum_write.writelines(forum_data[:2])


while i < len(forum_saved_data):
    write_grp = forum_saved_data[i]
    if write_grp[0][0] != ' ':
        forum_write.writelines(write_grp)
    else:
        write_grp[2] = f'\t{write_grp[2]}'
        forum_write.writelines(write_grp)
    forum_write.write('\n')
    i += 1

forum_write.close()