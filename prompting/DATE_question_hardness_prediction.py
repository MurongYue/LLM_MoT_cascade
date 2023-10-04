date_hard_prediction_only_question_prompt = """Predict the hardness level of the questions.
Question: Today is Christmas Eve of 1937. What is the date tomorrow in MM/DD/YYYY?
Level: Easy

Question: This is the last day of 1899. What is the date 24 hours later in MM/DD/YYYY?
Level: Easy

Question: Yesterday was April 30, 2021. What is the date 24 hours later in MM/DD/YYYY?
Level: Hard

Question: The current local time is 3:02 pm of 5/4/2004. What is the date yesterday in MM/DD/YYYY?
Level: Easy

Question: Today is 9/7. Jane is watching NFL 2003. What is the date one week ago from today in MM/DD/YYYY?
Level: Easy

Question: Today, 8/3/1997, is a day that we will never forget. What is the date one week from today in MM/DD/YYYY?
Level: Hard

Question: Jane got her job in 2016. Today is her 3-year work anniversary. She still remember that on Dec 2, her second day at work, she spilled coffee on her laptop. What is the date 24 hours later in MM/DD/YYYY?
Level: Hard

Question: Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. What is the date one year ago from today in MM/DD/YYYY?
Level: Easy

"""

date_hard_prediction_with_answer_prompt = """Generate feedback and predict if the generated answer is trustful.
Question: Today is Christmas Eve of 1937. What is the date tomorrow in MM/DD/YYYY?
Explain: Today is the Christmas Eve of 1937, so today is 12/24/1937.
Today is 12/24/1937, the date tomorrow is 12/25/1937.
A: 12/25/1937
Feedback: The answer is correct.
Trustful: Yes

Question: This is the last day of 1899. What is the date 24 hours later in MM/DD/YYYY?
Explain: Today is the last day of 1899, so today is 12/31/1899.
The date 24 hours later of today is 01/01/1900.
A: 01/01/1900
Feedback: The answer is correct.
Trustful: Yes

Question: Yesterday was April 30, 2021. What is the date 24 hours later in MM/DD/YYYY?
Explain: Yesterday was April 30, 2021. Therefore, the date 24 hours later is May 1, 2021.
A: 05/01/2021
Feedback: The answer is NOT correct. Yesterday was April 30, 2021, then today is May 1, 2021. 24 hours later is May 2, 2021.
Trustful: No

Question: The current local time is 3:02 pm of 5/4/2004. What is the date yesterday in MM/DD/YYYY?
Explain: The current local time is 3:02 pm of 5/4/2004
Therefore, today is 05/04/2004.
Yesterday is 05/03/2004.
A: 05/03/2004
Feedback: The answer is correct.
Trustful: Yes

Question: Today is 9/7. Jane is watching NFL 2003. What is the date one week ago from today in MM/DD/YYYY?
Explain: Today is 9/7, Jane is watching NFL 2003. Therefore, today is 09/07/2003.
1 week ago of today is 09/02/2003.
A: 09/02/2003
Feedback: The answer is correct.
Trustful: Yes

Question: Today, 8/3/1997, is a day that we will never forget. What is the date one week from today in MM/DD/YYYY?
Explain: Today is 8/3/1997.
One week from today is 8/10/1997.
A: 8/10/1997
Feedback: The answer is NOT correct. The returned answer should be in MM/DD/YYYY. So 8/10/1997 should be 08/10/1997.
Trustful: No

Question: Jane got her job in 2016. Today is her 3-year work anniversary. She still remember that on Dec 2, her second day at work, she spilled coffee on her laptop. What is the date 24 hours later in MM/DD/YYYY?
Explain: Today is Jane's 3-year work anniversary, which means she started her job on 09/07/2016.
If her second day at work was on Dec 2, then the year must be 2016.
So the date she spilled coffee on her laptop was 12/02/2016.
24 hours later of that date is 12/03/2016.
A: 12/03/2016
Feedback: The answer is NOT correct. Jane got her job in 2016 and Dec 2 is the second day of her work, so her work start date is 12/01/2016. 
Today is her 3-year work anniversary. So today is 12/01/2019, not 12/03/2016.
Trustful: No

Question: Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. What is the date one year ago from today in MM/DD/YYYY?
Explain: Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. Tomorrow is 10/16/1924, so today is 10/15/1924.
One year ago from today is 10/15/1923.
A: 10/15/1923
Feedback: The answer is correct.
Trustful: Yes

"""