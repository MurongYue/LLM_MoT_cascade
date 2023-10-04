asdiv_pot1_prompt = """
# Question: Isabella's hair is 18 inches long. By the end of the year her hair is 24 inches long. How much hair did she grow?
# Python code, return ans
Isabella_hair_before = 18
Isabella_hair_after_year = 24
hair_growth = Isabella_hair_after_year - Isabella_hair_before
ans = hair_growth

# Question: Robin had 18 pieces of gum. Her brother gave her some more pieces. Now Robin has 44 pieces in all. How many pieces of gum did Robin's brother give her?
# Python code, return ans
pieces_before = 18
pieces_after = 44
pieces_brother_give = pieces_after - pieces_before
ans = pieces_brother_give

# Question: Gavin has 23 shirts. 6 are blue the rest are green. How many green shirts does Gavin have?
# Python code, return ans
num_total_shirt = 23
num_blue_shirt = 6
num_green_shirt = num_total_shirt - num_blue_shirt
ans = num_green_shirt

# Question: When he arrived there, he went on to climb to the top of the falls. It usually takes 30 minutes for someone to get to the top. Stanley took time to see the view so his climb took 7 times longer than the usual. How many minutes did it take Stanley to get to the top?
# Python code, return ans
usual_time_to_top = 30
Steve_time_to_top = 7*usual_time_to_top
ans = Steve_time_to_top

# Question: Marian's friends were coming over that afternoon so she made 480 bite-sized pretzels. If one serving is equal to 12 pretzels, how many servings of bite-sized pretzels was Marian able to prepare?
# Python code, return ans
total_size_pretzels = 480
each_one_size = 12
num_serving = total_size_pretzels/each_one_size
ans = num_serving

# Question: Kelly has 121 Nintendo games. How many does she need to give away so that she will have 22 games left?
# Python code, return ans
num_of_total_games = 121
num_of_left_games = 22
num_give_away = num_of_total_games - num_of_left_games
ans = num_give_away

# Question: There are 250 vitamins in a bottle. Gil takes 12 vitamins per day. How many vitamins short of his usual 12 vitamins is Gil on the day the bottle runs out?
# Python code, return ans
num_of_vitamins_in_bottle = 250
cost_per_day = 12
ans = num_of_vitamins_in_bottle%cost_per_day

# Question: Caitlin is on the 13th step of a giant slide. She walked down 4 steps to talk to her friend Dana. Then she walked up 12 steps to the top. How many steps does the giant slide have?
# Python code, return ans
start_step = 13
walk_down_step = 4
walk_to_top = 12
ans = start_step - walk_down_step + walk_to_top

"""

asdiv_pot2_prompt = """
# Question: Omar loves to play checkers. He played 37 games yesterday. He played 49 games today. Omar lost 18 games. How many games did he win?
# Python code, return ans
game_played_yesterday = 37
game_played_today = 49
game_total_played = game_played_yesterday + game_played_today
game_lost = 18
game_win = game_total_played - game_lost
ans = game_win

# Question: At the carnival, 6 friends bought 27 tickets. If they wanted to split all the tickets so each friend got the same amount, how many more tickets would they need to buy?
# Python code, return ans
ticket_num = 27
friend_num = 6
i = 0
while friend_num * i > ticket_num:
    i += 1
tickets_to_buy = friend_num * i - ticket_num

# Question: Ted and Fred measured their height. Fred's height is 98 inches. Ted is 39 inches tall. What's the difference between Ted's height and Fred's height?
# Python code, return ans
Fred_height = 98
Ted_height = 39
different_height = Fred_height - Ted_height
ans = different_height

# Question: Sachin says that he has 6 books more than the 6 times of the books Priyanka has. Sachin has 42 books. How many books does Priyanka have?
# Python code, return ans
Sachin_books = 42
Priyanka_books = (Sachin_books - 6)/6
ans = Priyanka_books

# Question: If 10 years ago he was 25 years old, how old is Rojer now?
# Python code, return ans
ten_years_ago_age = 25
current_age = ten_years_ago_age + 10
ans = current_age

# Question: Tiffany was sending out birthday invitations to her friends. She sent out nine on Monday and eight on Tuesday. How many did she send total?
# Python code, return ans
sent_on_Monday = 9
sent_on_Tuesday = 8
ans = sent_on_Monday + sent_on_Tuesday

# Question: Jake has six fewer peaches than Steven. Steven has 13 peaches. How many peaches does Jake have?
# Python code, return ans
Steven_peaches = 13
Jake_peaches = Steven_peaches - 6
ans = Jake_peaches

# Question: Lino picked up 292 shells at the seashore in the morning and 324 shells in the afternoon. How many shells did he pick up in all?
# Python code, return ans
shell_morning = 292
shell_afternoon = 324
total_shell = shell_morning + shell_afternoon
ans = total_shell

"""

asdiv_cot1_prompt = """Please answer the math question and return a number as answer.
Question: Isabella's hair is 18 inches long. By the end of the year her hair is 24 inches long. How much hair did she grow?
Answer: Isabella's hair is 18 inches long and 24 inches long. 
So the length she grow in one year is 24 - 18 = 6
ans = 6

Question: Robin had 18 pieces of gum. Her brother gave her some more pieces. Now Robin has 44 pieces in all. How many pieces of gum did Robin's brother give her?
Answer: Robin had 18 pieces of gum before and has 44 pieces after. 
So Robin's brother give her 44 - 18 = 26
ans = 26

Question: Gavin has 23 shirts. 6 are blue the rest are green. How many green shirts does Gavin have?
Answer: Gavin has 23 shirts and 6 are blue the rest are green.
So the green shirt is 23 - 6 = 17
ans = 17

Question: When he arrived there, he went on to climb to the top of the falls. It usually takes 30 minutes for someone to get to the top. Stanley took time to see the view so his climb took 7 times longer than the usual. How many minutes did it take Stanley to get to the top?
Answer: It usually takes 30 minutes to the top. Stanley took 7 times longer than the usual.
So the time Stanley takes is 7 * 30 = 210
ans = 210

Question: Marian's friends were coming over that afternoon so she made 480 bite-sized pretzels. If one serving is equal to 12 pretzels, how many servings of bite-sized pretzels was Marian able to prepare?
Answer: There are total 480 bite-sized pretzels and one serving is equal to 12 pretzel.
So the number of servings is 480/12 = 40
ans = 40

Question: Kelly has 121 Nintendo games. How many does she need to give away so that she will have 22 games left?
Answer: Kelly has 121 Nintendo games before and have 22 games left after giving.
So the number of she give away is 121 - 22 = 99
ans = 99

Question: There are 250 vitamins in a bottle. Gil takes 12 vitamins per day. How many vitamins short of his usual 12 vitamins is Gil on the day the bottle runs out?
Answer: There are 250 vitamins in a bottle and Gil takes 12 vitamins per day.
The short is the remaining. So we get 250 % 12 = 10
ans = 10

Question: Caitlin is on the 13th step of a giant slide. She walked down 4 steps to talk to her friend Dana. Then she walked up 12 steps to the top. How many steps does the giant slide have?
Answer: Caitlin is on the 13th step of a giant slide and walked down 4 steps. So now she is on 13 - 4 = 9 steps.
Then she walked 12 steps to the top. The total steps is 12 + 9 = 21 steps.
ans = 21

"""

asdiv_cot2_prompt = """Please answer the math question and return a number as answer.
Question: Omar loves to play checkers. He played 37 games yesterday. He played 49 games today. Omar lost 18 games. How many games did he win?
Answer: Omar played 37 games yesterday and 49 games today. So he played 37 + 49 = 86 games.
He lost 18 games. So he win 86 - 18 = 64 games
ans = 64

Question: At the carnival, 6 friends bought 27 tickets. If they wanted to split all the tickets so each friend got the same amount, how many more tickets would they need to buy?
Answer: 6 friends bought 27 tickets. If they want to split all the tickets equally, they need at least 30 tickets.
So they still need to buy 30 - 27 = 3 tickets.
ans = 3

Question: Ted and Fred measured their height. Fred's height is 98 inches. Ted is 39 inches tall. What's the difference between Ted's height and Fred's height?
Answer: Fred's height is 98 inches. Ted is 39 inches tall.
So the difference is 98 - 39 = 59 inches.
ans = 59

Question: Sachin says that he has 6 books more than the 6 times of the books Priyanka has. Sachin has 42 books. How many books does Priyanka have?
Answer: Let's assume Priyanka has x books. Then we get 6x + 6 = 42
we get the x = 6.
ans = 6

Question: If 10 years ago he was 25 years old, how old is Rojer now?
Answer: If 10 years ago he was 25 years old, now he is 25 + 10 = 35 years.
ans = 35

Question: Tiffany was sending out birthday invitations to her friends. She sent out nine on Monday and eight on Tuesday. How many did she send total?
Answer: She sent out 9 on Monday and 8 on Tuesday. So she sent 9 + 8 = 17 totally.
ans = 17

Question: Jake has six fewer peaches than Steven. Steven has 13 peaches. How many peaches does Jake have?
Answer: Jake has x peaches. x + 6 =13.
Thus, we get x = 7.
ans = 7

Question: Lino picked up 292 shells at the seashore in the morning and 324 shells in the afternoon. How many shells did he pick up in all?
Answer: Lino picked 292 + 324 = 616 shells total.
ans = 616

"""