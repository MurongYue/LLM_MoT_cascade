tabmwp_cot1_prompting = """
Read the following table regarding "Coins" and then answer a question:
Name | Number of coins
Braden | 76
Camilla | 94
Rick | 86
Mary | 84
Hector | 80
Devin | 83
Emily | 82
Avery | 87
Question: Some friends discussed the sizes of their coin collections. What is the mean of the numbers?
Explain: Let's think step by step.
The numbers of coins of each one are in [76, 94, 86, 84, 80, 83, 82, 87]. 
So the mean of the numbers is (76+94+86+84+80+83+82+87)/8 = 648/8 = 81
Answer: 81

Read the following table and then answer a question:
Price | Quantity demanded | Quantity supplied
$155 | 22,600 | 5,800
$275 | 20,500 | 9,400
$395 | 18,400 | 13,000
$515 | 16,300 | 16,600
$635 | 14,200 | 20,200
Question: Look at the table. Then answer the question. At a price of $155, is there a shortage or a surplus? Choose from the the options: [shortage, surplus]
Explain: Let's think step by step.
At price of $155, the quantity demanded is 22600, the quantity supplied is 5800.
The quantity demanded is larger than the quantity supplied.
Therefore, there is a shortage at a price of $155.
From the options [shortage, surplus], we will choose "shortage".
Answer: shortage

Read the following table regarding "Cans of food collected" and then answer a question:
Name | Number of cans
Samir | 7
Kristen | 4
Dakota | 7
Jamie | 8
Maggie | 9
Question: Samir's class recorded how many cans of food each student collected for their canned food drive. What is the median of the numbers?
Explain: Let's think step by step.
The number of cans of each person are in [7, 4, 7, 8, 9]. 
The median of the numbers are 7.
Answer: 7

Read the following table regarding "" and then answer a question:
toy boat | $5.54
toy guitar | $8.23
set of juggling balls | $5.01
trivia game | $8.18
jigsaw puzzle | $5.30
toy dinosaur | $3.00
Question: Lorenzo has $13.50. Does he have enough to buy a toy guitar and a set of juggling balls? Choose from the the options: [yes, no]
Explain: Let's think step by step.
The price of the toy guitar is $8.23 and the price of a set of juggling balls is $5.01. 
So the total cost for these two is $8.23 + $5.01 = $13.24. 
Lorenzo has $13.50, which is larger than $13.24. So he can afford the money.
From the options [yes, no], we will choose "yes".
Answer: yes

Read the following table regarding "Renting movies last month" and then answer a question:
Number of times | Frequency
0 | 1
1 | 18
2 | 12
3 | 13
4 | 0
Question: Employees at Eve's Movies tracked the number of movies that customers rented last month. How many customers are there in all?
Explain: Let's think step by step.
From the table, we can learn 1 people rent 0 times, 18 people rent 1 times, 12 people rent 2 times, 13 people rent 3 times, 0 people rent 4 times.
The total number of people is 1+18+12+13 = 34.
Answer: 34

Read the following table regarding "Donor levels" and then answer a question:
Donation level | Number of donors
Gold | 15
Silver | 68
Bronze | 58
Question: The Burlington Symphony categorizes its donors as gold, silver, or bronze depending on the amount donated. What fraction of donors are at the bronze level? Simplify your answer.
Explain: Let's think step by step.
The number of bronze level donors is 58.
The total number of donors is 15+68+58 = 141.
The fraction is 58/141.
Answer: 58/141

Read the following table regarding "Cans of food collected" and then answer a question:
Name | Number of cans of food
Dwayne | 649
Regan | 646
Matthew | 668
Winston | 694
Question: Dwayne's class recorded how many cans of food each student collected for their canned food drive. Who collected the fewest cans? Choose from the the options: [Dwayne, Regan, Matthew, Winston]
Explain: Let's think step by step.
From the table, Dwayne collected 649 cans, Regan collected 646 cans, Matthew collected 668 cans and Winston collected 694 cans. 
We can learn that Regan collected the fewest cans.
From the options [Dwayne, Regan, Matthew, Winston], we will choose "Regan".
Answer: Regan

Read the following table regarding "Red gumdrops per bag" and then answer the question:
Stem | Leaf
3 | 0, 0, 2, 2
4 | 2, 2, 4, 6, 6
5 | 1, 8, 8
6 | 0, 7
7 | 9
8 | 1
9 | 0
Question: A machine dispensed red gumdrops into bags of various sizes. What is the smallest number of red gumdrops?
Explain: Let's think step by step.
From the table, the the stem represents the ten digits and the leaf represents the single digits.
So we can covert the table into a list [30, 30, 32, 32, 42, 42, 44, 46, 46, 51, 58, 58, 60, 67, 79, 81, 90].
From the list, we learn that the smallest number of the list is 30.
Answer: 30

"""

tabmwp_cot2_prompting = """
Read the following table regarding "Trees planted" and then answer a question:
Organization | Number of trees planted
Let it Grow | 464
Mission Reforestation | 463
Plant It | 449
Acorns to Oaks | 436
Question: An environmental agency examined how many trees were planted by different organizations. Which organization planted the fewest trees? Choose from the the options: : [Let it Grow, Mission Reforestation, Plant It, Acorns to Oaks]
Explain: Let's think step by step.
From the table, Let it Grow planted 464 trees, Mission Reforestation planted 463 trees, Plant It planted 449 trees and Acorns to Oaks planted 436 trees. 
We can learn that Plant It planted the fewest trees.
From the options [Let it Grow, Mission Reforestation, Plant It, Acorns to Oaks], we will choose "Plant It".
Answer: Plant It

Read the following table regarding "Hours of babysitting" and then answer a question:
Month | Hours
November | 3
December | 3
January | 7
February | 2
March | 7
April | 2
Question: Justin looked at his calendar to figure out how much time he spent babysitting each month. What is the mean of the numbers?
Explain: Let's think step by step.
From the table, the hours in each month is [3, 3, 7, 2, 7, 2]. 
The mean number is 3+3+7+2+7+2=24.
Answer: 24

Read the following table regarding "Push-up competition (number of push-ups)" and then answer a question:
Stem | Leaf
3 | 1, 7
4 | 5, 8
5 | 0, 0, 0, 2, 2, 3
6 | 1, 3, 4
7 | 0, 3, 7, 8, 9
8 | 0, 1, 5, 6
9 | 0, 0
Question: Mona's P.E. class participated in a push-up competition, and Mona wrote down how many push-ups each person could do. How many people did exactly 50 push-ups?
Explain: Let's think step by step.
From the table, the the stem represents the ten digits and the leaf represents the single digits.
So we can covert the table into a list [31, 37, 45, 48, 50, 50, 50, 52, 52, 53, 61, 63, 64, 70, 73, 77, 78, 79, 80, 81, 85, 86, 90, 90].
The number of those exactly equal to 50 in the list is 3.
Answer: 3

Read the following table regarding "Voicemail messages on Franco's phone" and then answer a question:
Day | Voicemail messages
Monday | 16
Tuesday | 8
Wednesday | 12
Thursday | 10
Friday | 21
Question: Worried about going over his storage limit, Franco monitored the number of undeleted voicemail messages stored on his phone each day. According to the table, what was the rate of change between Tuesday and Wednesday?
Explain: Let's think step by step.
The rate is the change_of_number/change_of_day. 
The change of number from Tuesday to Wednesday is 12-8=4 and the change of day is 1. 
The rate of change is 4/1 = 4.
Answer: 4

Read the following table regarding "Stuffed animal collections" and then answer a question:
Name | Number of stuffed animals
Eva | 49
Keenan | 47
Xavier | 34
Cole | 24
Sally | 31
Question: Some friends compared the sizes of their stuffed animal collections. What is the mean of the numbers?
Explain: Let's think step by step.
Read the numbers from the table and get 49, 47, 34, 24, 31
First, count how many numbers are in the group.
There are 5 numbers.
Now add all the numbers together:
49 + 47 + 34 + 24 + 31 = 185
Now divide the sum by the number of numbers:185/5 = 37
The mean is 37
Answer: 37

Read the following table regarding "" and then answer a question:
78-mm washers | $6.35/lb
39-mm washers | $9.48/lb
50-mm washers | $9.69/lb
44-mm washers | $5.47/lb
Question: Maura wants to buy 1 pound of 78-mm washers, 4 pounds of 50-mm washers, and 4 pounds of 44-mm washers. How much will she spend?
Explain: Let's think step by step.
Find the cost of the 78-mm washers. Multiply:$6.35 * 1 = $6.35
Find the cost of the 50-mm washers. Multiply:$9.69 * 4 = $38.76
Find the cost of the 44-mm washers. Multiply:$5.47 * 4 = $21.88
Now find the total cost by adding:
$6.35 + $38.76 + $21.88 = $66.99
Answer: 66.99

Read the following table regarding "" and then answer a question:
basketball key chain | $0.73
soccer ball key chain | $0.90
puppy key chain | $0.57
cat key chain | $0.71
Question: Brenda has $1.66. Does she have enough to buy a basketball key chain and a soccer ball key chain? "choices": ["yes","no"]
Explain: Let's think step by step.
Add the price of a basketball key chain and the price of a soccer ball key chain:$0.73 + $0.90 = $1.63.
$1.63 is less than $1.66.
From the options ["yes","no"], we will choose "yes".
Answer: yes

Read the following table regarding "" and then answer a question:
Stem | Leaf
1 | 2
2 | 8
3 | 9
4 | 2, 9
5 | 5
6 | 0, 1
7 | 5
8 | 1, 7
9 | 0
Question: Edna counted the number of words per page in her new book. How many pages have at least 60 words but fewer than 100 words?
Explain: Let's think step by step.
From the table, the the stem represents the ten digits and the leaf represents the single digits.
So we can covert the table into a list [12, 28, 39, 42, 49, 55, 60, 61, 75, 81, 87, 90].
In these numbers, the word at least 60 but fewer than 100 is [60, 61, 75, 81, 87, 90].
So the page number is 6.
Answer: 6

"""

tabmwp_pot1_prompting = """
Read the following table regarding "Coins" and then write Python code to answer a question:
Name | Number of coins
Braden | 76
Camilla | 94
Rick | 86
Mary | 84
Hector | 80
Devin | 83
Emily | 82
Avery | 87
Question: Some friends discussed the sizes of their coin collections. What is the mean of the numbers?
# Python Code, return ans
number_of_coins_for_different_person = [76, 94, 86, 84, 80, 83, 82, 87]
ans = sum(number_of_coins_for_different_person) / len(number_of_coins_for_different_person)

Read the following table and then write Python code to answer a question:
Price | Quantity demanded | Quantity supplied
$155 | 22,600 | 5,800
$275 | 20,500 | 9,400
$395 | 18,400 | 13,000
$515 | 16,300 | 16,600
$635 | 14,200 | 20,200
Question: Look at the table. Then answer the question. At a price of $155, is there a shortage or a surplus? Choose from the the options: [shortage, surplus]
# Python Code, return ans
quantity_demanded_price_155 = 22600
quantity_supplied_price_155 = 5800
if quantity_demanded_at_price_155 > quantity_supplied_at_price_155:
    ans = 'shortage'
else:
    ans = 'surplus'

Read the following table regarding "Cans of food collected" and then write Python code to answer a question:
Samir | 7
Kristen | 4
Dakota | 7
Jamie | 8
Maggie | 9
Question: Samir's class recorded how many cans of food each student collected for their canned food drive. What is the median of the numbers?
# Python Code, return ans
cans = [7, 4, 5, 8, 9]
cans = sorted(cans)
middle1 = (len(cans) - 1) // 2
middle2 = len(cans) // 2
ans = (cans[middle1] + cans[middle2]) / 2

Read the following table regarding "" and then write Python code to answer a question:
toy boat | $5.54
toy guitar | $8.23
set of juggling balls | $5.01
trivia game | $8.18
jigsaw puzzle | $5.30
toy dinosaur | $3.00
Question: Lorenzo has $13.50. Does he have enough to buy a toy guitar and a set of juggling balls? Choose from the the options: ['yes', 'no']
# Python Code, return ans
guitar_price = 8.23
juggling_balls = 5.01
total_money = 13.5
if total_money > juggling_balls + guitar_price:
    ans = "yes"
else:
    ans = "no"

Read the following table regarding "Renting movies last month" and then write Python code to answer a question:
Number of times | Frequency
0 | 1
1 | 18
2 | 12
3 | 13
4 | 0
Question: Employees at Eve's Movies tracked the number of movies that customers rented last month. How many customers are there in all?
# Python Code, return ans
customer_number_for_each_frequency = [1,18,12,13]
ans = sum(customer_number_for_each_frequency)

Read the following table regarding "Donor levels" and then write Python code to answer a question:
Donation level | Number of donors
Gold | 15
Silver | 68
Bronze | 58
Question: The Burlington Symphony categorizes its donors as gold, silver, or bronze depending on the amount donated. What fraction of donors are at the bronze level? Simplify your answer.
# Python Code, return ans
total_donors = 15 + 68 +58
bronze_donors = 58
ans = bronze_donors/total_donors

Read the following table regarding "Cans of food collected" and then write Python code to answer a question:
Name | Number of cans of food
Dwayne | 649
Regan | 646
Matthew | 668
Winston | 694
Question: Dwayne's class recorded how many cans of food each student collected for their canned food drive. Who collected the fewest cans? Choose from the the options: ['Dwayne', 'Regan', 'Matthew', 'Winston']
# Python Code, return ans
can_dict = {'Dwayne': 649, 'Regan':646, 'Matthew':668, 'Winston':694}
min_value = min(can_dict.values())
for key,value in can_dict.items():
    if value == min_value:
        ans = key

Read the following table regarding "Red gumdrops per bag" and then answer the question:
Stem | Leaf
3 | 0, 0, 2, 2
4 | 2, 2, 4, 6, 6
5 | 1, 8, 8
6 | 0, 7
7 | 9
8 | 1
9 | 0
Question: A machine dispensed red gumdrops into bags of various sizes. What is the smallest number of red gumdrops?
# Python Code, return ans
# From the table, the the stem represents the ten digits and the leaf represents the single digits.
gumdrops_number_list = [30, 30, 32, 32, 42, 42, 44, 46, 46, 51, 58, 58, 60, 67, 79, 81, 90].
ans = min(number_list)

"""

tabmwp_pot2_prompting = """
Read the following table regarding "Trees planted" and then write Python code to answer a question:
Organization | Number of trees planted
Let it Grow | 464
Mission Reforestation | 463
Plant It | 449
Acorns to Oaks | 436
Question: An environmental agency examined how many trees were planted by different organizations. Which organization planted the fewest trees? Choose from the the options: : ["Let it Grow", "Mission Reforestation", "Plant It", "Acorns to Oaks"]
# Python Code, return ans
can_dict = {'Let it Grow': 464, 'Mission Reforestation':463, 'Plant It':449, 'Acorns to Oaks':436}
min_value = min(can_dict.values())
for key,value in can_dict.items():
    if value == min_value:
        ans = key

Read the following table regarding "Hours of babysitting" and then write Python code to answer a question:
Month | Hours
November | 3
December | 3
January | 7
February | 2
March | 7
April | 2
Question: Justin looked at his calendar to figure out how much time he spent babysitting each month. What is the mean of the numbers?
# Python Code, return ans
number_of_babysitting_time_in_each_month = [3, 3, 7, 2, 7, 2]
ans = sum(number_of_babysitting_time_in_each_month) / len(number_of_babysitting_time_in_each_month)

Read the following table regarding "Push-up competition (number of push-ups)" and then write Python code to answer a question:
Stem | Leaf
3 | 1, 7
4 | 5, 8
5 | 0, 0, 0, 2, 2, 3
6 | 1, 3, 4
7 | 0, 3, 7, 8, 9
8 | 0, 1, 5, 6
9 | 0, 0
Question: Mona's P.E. class participated in a push-up competition, and Mona wrote down how many push-ups each person could do. How many people did exactly 50 push-ups?
# Python Code, return ans
# From the table, the the stem represents the ten digits and the leaf represents the single digits.
all_number_list = [31, 37, 45, 48, 50, 50, 50, 52, 52, 53, 61, 63, 64, 70, 73, 77, 78, 79, 80, 81, 85, 86, 90, 90]
exactly_50_times = 0
for number in all_number_list:
    if number == 50:
        exactly_50_times += 1
ans = exactly_50_times

Read the following table regarding "Voicemail messages on Franco's phone" and then write Python code to answer a question:
Day | Voicemail messages
Monday | 16
Tuesday | 8
Wednesday | 12
Thursday | 10
Friday | 21
Question: Worried about going over his storage limit, Franco monitored the number of undeleted voicemail messages stored on his phone each day. According to the table, what was the rate of change between Tuesday and Wednesday?
# Python Code, return ans
Tuesday_message_number = 8
Wednesday_message_number = 12
change_in_value = Wednesday_message_number - Tuesday_message_number
change_in_day = 1
rate = change_in_value/change_in_day
ans = rate

Read the following table regarding "Stuffed animal collections" and then answer a question:
Name | Number of stuffed animals
Eva | 49
Keenan | 47
Xavier | 34
Cole | 24
Sally | 31
Question: Some friends compared the sizes of their stuffed animal collections. What is the mean of the numbers?
# Python Code, return ans
number_of_stuffed_animals = [49, 47, 34, 24, 31]
ans = sum(number_of_stuffed_animals)/len(number_of_stuffed_animals)

Read the following table regarding "" and then answer a question:
78-mm washers | $6.35/lb
39-mm washers | $9.48/lb
50-mm washers | $9.69/lb
44-mm washers | $5.47/lb
Question: Maura wants to buy 1 pound of 78-mm washers, 4 pounds of 50-mm washers, and 4 pounds of 44-mm washers. How much will she spend?
# Python Code, return ans
washer_78mm_per_pound = 6.35
washer_50mm_per_pound = 9.69
washer_44mm_per_pound = 5.47
ans = washer_78mm_per_pound + 4 * washer_50mm_per_pound + 4 * washer_44mm_per_pound

Read the following table regarding "" and then answer a question:
basketball key chain | $0.73
soccer ball key chain | $0.90
puppy key chain | $0.57
cat key chain | $0.71
Question: Brenda has $1.66. Does she have enough to buy a basketball key chain and a soccer ball key chain? "choices": ["yes","no"]
# Python Code, return ans
basketball_key_chain = 0.73
soccer_ball_key_chain = 0.90
basketball_soccer_ball_key_chain = basketball_key_chain + soccer_ball_key_chain
Brenda_money = 1.66
if basketball_soccer_ball_key_chain > Brenda_money:
    ans = 'no'
else:
    ans = 'yes'

Read the following table regarding "" and then answer a question:
Stem | Leaf
1 | 2
2 | 8
3 | 9
4 | 2, 9
5 | 5
6 | 0, 1
7 | 5
8 | 1, 7
9 | 0
Question: Edna counted the number of words per page in her new book. How many pages have at least 60 words but fewer than 100 words?
# Python Code, return ans
# From the table, the the stem represents the ten digits and the leaf represents the single digits.
number_of_words =  [12, 28, 39, 42, 49, 55, 60, 61, 75, 81, 87, 90].
ans = 0
for num in number_of_words:
    if num >= 60 and num < 100:
        ans+=1

"""
