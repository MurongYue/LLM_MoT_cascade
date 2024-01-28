gsm_hints_prompt = """Given the hints(may not be correct), answer the question. 
Question: Tara has a shoebox that is 4 inches tall and 6 inches wide. She puts a square block inside that is 4 inches per side. How many square inches of the box are left uncovered?
Hints: The answer may be near to 24 or 8.
Answer: The shoebox is 24 square inches because 4 x 6 = <<4*6=24>>24
The block is 16 square inches because 4 x 4 = <<4*4=16>>16
There are 8 square inches uncovered because 24 - 16 = <<24-16=8>>8
ans = 8

Question: A train takes 4 hours to reach a destination at a speed of 50 miles per hour. How long would it take if it traveled at 100 miles per hour instead?
Hints: The answer may be near to 2 or 120.
Answer: The distance to the destination is 4 hours * 50 miles/hour = <<4*50=200>>200 miles.
Traveling at 100 miles per hour, it will take 200 miles / (100 miles/hour) = <<200/(100)=2>>2 hours.
ans = 2

Question: Bethany is working at the front desk at Joe’s Gym. There were some people lifting weights when she started her shift. Then 5 more people came in and started running on the treadmill and 2 people left. There are now 19 people in the gym. How many people were lifting weights at the start of Bethany’s shift?
Hints: The answer may be near to 11 or 12.
Answer: We know that 5 people came in and 2 people left after Bethany’s shift started, so there was a net change of 5 – 2 = <<5-2=3>>3 people.
If there are 19 people now in the gym and that is 3 more than when Bethany’s shift started, we know there were 19 – 3 = <<19-3=16>>16 people lifting weights at the start of her shift.
ans = 16

Question: Stacy, Steve and Sylar have 1100 berries total. Stacy has 4 times as many berries as Steve, and Steve has double the number of berries that Skylar has. How many berries does Stacy have?
Hints: The answer may be near to 800 or 1257.14.
Answer: Let x be the number of berries Skylar has.
Steve has 2x berries
Stacy has 4(2x)=8x berries
1100=x+2x+8x
1100=11x
x = <<100=100>>100 berries
Stacy has 8(100)=<<8*100=800>>800 berries
ans = 800

Question: Ronald and his friend Max want to buy a new video game that was just released. The game costs $60. To earn money, they started selling ice cream in their yard, and they sell each ice cream for $5. How many ice creams will they need to sell for both to be able to afford to buy the game?
Hints: The answer may be near to 12 or 24.
Answer: They need $60/game x 2 games= $120 in total.
If one ice cream is sold for $5, they will need to sell $120 ÷ $5/ice cream = <<120/5=24>>24 ice creams.
ans = 24

Question: Karen's students are about to take a standardized test. Karen gets a $500 bonus if their average score is above 75, plus an extra $10 bonus for every additional point the average score increases above 75. So far, Karen has graded 8 tests, and the average is 70. Given that each student can have a maximum score of 150, what combined score do the last two tests need to have for Karen to earn a $600 bonus?
Hints: The answer may be near to 145 or 290.
Answer: First subtract $500 from Karen's goal bonus amount to find how much she makes from the extra $10/point bonus: $600 - $500 = $<<600-500=100>>100
Then divide the extra bonus by the extra rate: $100 / $10/point = <<100/10=10>>10 points
Then add the 10 extra points to the baseline 75 point goal to find the students' average test score: 10 points + 75 points = <<10+75=85>>85 points
Then added the 8 graded tests to the 2 ungraded tests to find the total number of tests: 2 tests + 8 tests = <<2+8=10>>10 tests
Then multiply the 85 point average by the number of tests to find the total number of points the students need to earn: 85 points/test * 10 tests = 850 points
Then multiply the current average by the current number of graded tests to find how many points have been earned so far: 70 points/test * 8 tests = <<70*8=560>>560 points
Then subtract the number of points earned from the number of points needed to find the combine score the last two tests need: 850 points - 560 points = <<850-560=290>>290 points
ans = 290

Question: Koby and Cherie want to light fireworks. Koby has bought 2 boxes of fireworks while Cherie has just 1 box of fireworks. Koby’s boxes each contain 3 sparklers and 5 whistlers. Cherie’s box has 8 sparklers and 9 whistlers. In total, how many fireworks do Koby and Cherie have?
Hints: The answer may be near to 49 or 33.
Answer: Each of Koby’s boxes contain 3 sparklers + 5 whistlers = <<3+5=8>>8 fireworks.
So in total, Koby has 2 boxes * 8 fireworks per box = <<2*8=16>>16 fireworks.
Cherie’s box of fireworks has 8 sparklers + 9 whistlers = <<8+9=17>>17 fireworks.
Koby and Cherie therefore have a combined total of 16 fireworks from Koby + 17 fireworks from Cherie = <<16+17=33>>33 fireworks.
ans = 33

Question: Frank is practicing a new dance move.  It starts with him take 5 steps back, and then 10 steps forward, and then 2 steps back, and then double that amount forward.  How many steps forward is Frank from his original starting point?
Hints: The answer may be near to 9 or 7.
Answer: Frank stars by taking 10 steps forward from a position 5 steps behind where he started, so he's 10-5= <<10-5=5>>5 steps forward in total
Frank then takes 2 steps back, meaning he's now 5-2=<<5-2=3>>3 steps forward in total from where he began
He then takes double the previous amount of 2 steps forward, so he takes 2*2= <<2*2=4>>4 steps forward
Since Frank was 3 steps forward before that, that means Frank finishes 3+4=<<3+4=7>>7 steps forward
ans = 7

"""