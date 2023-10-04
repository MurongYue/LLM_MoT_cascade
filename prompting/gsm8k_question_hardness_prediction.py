gsm_hard_prediction_only_question_prompt = """Predict the hardness level of the questions.
Question: Shawna's workout goal is 30 situps. On Monday, Shawna was only able to do 12 situps, so she decided that she would make up for the rest on Tuesday. However, she was only able to do 19 situps on Tuesday. How many situps would Shawna have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?
Level: Hard

Question: Bert fills out the daily crossword puzzle in the newspaper every day. He uses up a pencil to fill out the puzzles every two weeks. On average, it takes him 1050 words to use up a pencil. How many words are in each crossword puzzle on average?
Level: Easy

Question: Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?
Level: Hard

Question: A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?
Level: Easy

Question: Keiko sent 111 text messages last week. This week she sent 50 less than double what she sent last week. How many text messages did Keiko send last week and this week combined?
Level: Easy

Question: Tommy is making 12 loaves of bread. He needs 4 pounds of flour per loaf. A 10-pound bag of flour costs $10 and a 12-pound bag costs $13. When he is done making his bread, he has no use for flour and so he will throw away whatever is left. How much does he spend on flour if he buys the cheapest flour to get enough?
Level: Hard

Question: A roadwork company is paving a newly constructed 16-mile road. They use a mixture of pitch and gravel to make the asphalt to pave the road. Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make. It takes three truckloads of asphalt to pave each mile of road. The company paved 4 miles of road on one day, then one mile less than double that on the second day. How many barrels of pitch will the company need to finish the remaining road on the third day?
Level: Hard

Question: Ellie has found an old bicycle in a field and thinks it just needs some oil to work well again.  She needs 10ml of oil to fix each wheel and will need another 5ml of oil to fix the rest of the bike. How much oil does she need in total to fix the bike?
Level: Easy

"""

gsm_hard_prediction_with_answer_prompt = """Generate feedback and predict if the generated answer is trustful.
Question: Shawna's workout goal is 30 situps. On Monday, Shawna was only able to do 12 situps, so she decided that she would make up for the rest on Tuesday. However, she was only able to do 19 situps on Tuesday. How many situps would Shawna have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?
Answer: Shawna's goal is 30 situps, and she has already done 12 + 19 = <<12+19=31>>31 situps.\nTo meet her goal, she needs to do 30 - 31 = <<30-31=-1>>-1 situps.\nSince she can't do negative situps, she doesn't need to do any more situps to meet her goal.\nans = 0
Feedback: The answer is incorrect. The goal is 30 situps everyday. So the total is 3*30 = 90 rather than 30.
Trustful: No

Question: Bert fills out the daily crossword puzzle in the newspaper every day. He uses up a pencil to fill out the puzzles every two weeks. On average, it takes him 1050 words to use up a pencil. How many words are in each crossword puzzle on average?
Answer: Bert uses up a pencil every 2 weeks, so he uses up 1/14th of a pencil each day.\nIf it takes him 1050 words to use up a pencil, then he uses 1050/14 = <<1050/14=75>>75 words per day on average.\nSince he fills out the crossword puzzle every day, that means each crossword puzzle has 75 words on average.\nans = 75
Feedback: The answer is correct.
Trustful: Yes

Question: Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?
Answer: Henry took 9 pills a day for 14 days, so he took a total of 9*14=<<9*14=126>>126 pills.\nHe bought 4 pills at $1.50 each, so he spent 4*$1.50=$<<4*1.5=6>>6 on those pills.\nHe bought 126-4=<<126-4=122>>122 of the other pills.\nEach of the other pills cost $5.50 more than the $1.50 pills, so they cost $1.50+$5.50=$<<1.5+5.5=7>>7 each.\nHe spent 122*$7=$<<122*7=854>>854 on the other pills.\nIn total, he spent $6+$854=$<<6+854=860>>860 on the pills.\nans = 860
Feedback: The answer is incorrect. The 4 pills cost 1.50 is in 9 pills, not in 9*14 pills.
Trustful: No

Question: A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?
Answer: For the two heavy washes, the washing machine will use 20 gallons per load, so 2 * 20 = <<2*20=40>>40 gallons of water will be used.\nFor the three regular washes, the washing machine will use 10 gallons per load, so 3 * 10 = <<3*10=30>>30 gallons of water will be used.\nFor the one light wash, the washing machine will use 2 gallons of water.\nFor the two bleached loads, the washing machine will use an extra light wash cycle, so 2 * 2 = <<2*2=4>>4 gallons of water will be used.\nIn total, the washing machine will use 40 + 30 + 2 + 4 = <<40+30+2+4=76>>76 gallons of water.\nans = 76
Feedback: The answer is correct.
Trustful: Yes

Question: Keiko sent 111 text messages last week. This week she sent 50 less than double what she sent last week. How many text messages did Keiko send last week and this week combined?
Answer: Double the amount of text messages Keiko sent last week is 111 * 2 = <<111*2=222>>222.\nSo this week she sent 222 - 50 = <<222-50=172>>172 text messages.\nTherefore, Keiko sent a total of 111 + 172 = <<111+172=283>>283 text messages last week and this week combined.\nans = 283
Feedback: The answer is correct.
Trustful: Yes

Question: Tommy is making 12 loaves of bread. He needs 4 pounds of flour per loaf. A 10-pound bag of flour costs $10 and a 12-pound bag costs $13. When he is done making his bread, he has no use for flour and so he will throw away whatever is left. How much does he spend on flour if he buys the cheapest flour to get enough?
Answer: Tommy needs 4 * 12 = <<4*12=48>>48 pounds of flour in total.\nHe can buy two 10-pound bags for a total of $10 * 2 = $<<10*2=20>>20.\nHe would have 20 - 48 = <<20-48=-28>>-28 pounds of flour left over, which he will throw away.\nAlternatively, he can buy one 12-pound bag for $13.\nHe would have 12 - 48 = <<12-48=-36>>-36 pounds of flour left over, which he will throw away.\nTherefore, he should buy the two 10-pound bags for $20.\nans = 20
Feedback: The answer is incorrect. We need to compare the cost to buy 10-pound bag and 12-pound bag.
Trustful: No

Question: A roadwork company is paving a newly constructed 16-mile road. They use a mixture of pitch and gravel to make the asphalt to pave the road. Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make. It takes three truckloads of asphalt to pave each mile of road. The company paved 4 miles of road on one day, then one mile less than double that on the second day. How many barrels of pitch will the company need to finish the remaining road on the third day?
Answer: Each mile of road requires 3 truckloads of asphalt, which means 3 * 2 = <<3*2=6>>6 bags of gravel per mile of road.\nSince each bag of gravel requires 5 barrels of pitch, that means each mile of road requires 6 * 5 = <<6*5=30>>30 barrels of pitch.\nOn the first day, the company paved 4 miles of road, which means they used 4 * 30 = <<4*30=120>>120 barrels of pitch.\nOn the second day, they paved one mile less than double the first day, which means they paved (2 * 4 - 1) = <<2*4-1=7>>7 miles of road.\nSo on the second day, they used 7 * 30 = <<7*30=210>>210 barrels of pitch.\nThe total distance of the road is 16 miles, and they paved 4 + 7 = <<4+7=11>>11 miles on the first two days, which means they have 16 - 11 = <<16-11=5>>5 miles left to pave.\nTo pave 5 miles, they will need 5 * 30 = <<5*30=150>>150 barrels of pitch.\nans = 150
Feedback: The answer is incorrect. Five times as many bags of gravel as it does barrels of pitch to make. So the barrels of pitch is 6/5 = 1.2 for each truck, not 30.
Trustful: No

Question: Ellie has found an old bicycle in a field and thinks it just needs some oil to work well again.  She needs 10ml of oil to fix each wheel and will need another 5ml of oil to fix the rest of the bike. How much oil does she need in total to fix the bike?
Answer: To fix both wheels, Ellie needs 10 ml of oil per wheel, so she needs 10 * 2 = <<10*2=20>>20 ml of oil.\nAdding the oil needed for the rest of the bike, Ellie needs 20 + 5 = <<20+5=25>>25 ml of oil in total to fix the bike.\nans = 25
Feedback: The answer is correct.
Trustful: Yes

"""