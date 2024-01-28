date_hints_prompt = """Given the hints(may not be correct), answer the question. 
Question: Jane was born on the last day of Feburary in 2000. Today is her 16-year-old birthday. What is the date 24 hours later in MM/DD/YYYY?
Hints: The answer may be near 02/29/2016 or 03/01/2016.
Answer: Jane was born on the last day of Feburary in 2000, so she born on 02/29/2000.
Today is her 16-year-old birthday. So today is 02/29/2016.
The date 24 hours later than today is 03/01/2016.
A: 03/01/2016

Question: Today, 8/3/1997, is a day that we will never forget. What is the date one week from today in MM/DD/YYYY?
Hints: The answer may be near to 8/10/1997 or 08/10/1997.
Answer: Today is 08/03/1997.
One week from today is 08/10/1997.
A: 08/10/1997

Question: It is 4/19/1969 today. What is the date a month ago in MM/DD/YYYY?
Hints: The answer may be near to 3/19/1969 or 03/19/1969.
Answer: It is 04/19/1969 today. A month ago from today would be 3/19/1969.
A: 03/19/1969

Question: Jane quited her job on Mar 20, 2020. 176 days have passed since then. What is the date 10 days ago in MM/DD/YYYY?
Hints: The answer may be near to 09/03/2020 or 03/10/2020.
Answer: If Jane quit her job on Mar 20, 2020, and 176 days have passed since then, then today's date is 09/12/2020 (counting from Mar 20 to Sep 12 is 176 days).
10 days ago from today is 09/02/2020.
A: 09/02/2020

Question: In the UK, people usually put the day before the month when formatting the date. Therefore, today is 02/01/1987 to them. What is the date today in MM/DD/YYYY?
Hints: The answer may be near to 02/01/1987 or 01/02/1987.
Answer: Today is 01/02/1987 in the UK format.
A: 01/02/1987

Question: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date a month ago in MM/DD/YYYY?
Hints: The answer may be near to 02/12/2002 or 02/11/2002.
Answer: Jane thought today is 03/11/2002, but today is actually 1 day later, which is 03/12/2002.
A month ago from today is 02/12/2002.
A: 02/12/2002

Question: Jane scheduled 3 apointments with 5 poeple for tomorrow (Tue, 7/9/1972). What is the date one week ago from today in MM/DD/YYYY?
Hints: The answer may be near to 07/02/1972 or 07/01/1972.
Answer: If tomorrow is Tue, 7/9/1972, then today is Mon, 7/8/1972.
One week ago from today is Mon, 7/2/1972.
A: 07/02/1972

Question: It was Sept. 1st, 2021 a week ago. What is the date today in MM/DD/YYYY?
Hints: The answer may be near to 09/08/2021 or 07/07/2023.
Answer: If it was Sept. 1st, 2021 a week ago, then today is Sept. 8th, 2021.
Therefore, today's date is 09/08/2021.
A: 09/08/2021

"""