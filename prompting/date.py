date_CoT1_prompting = """
Q: Today is Christmas Eve of 1937. What is the date tomorrow in MM/DD/YYYY?
Explain: Today is the Christmas Eve of 1937, so today is 12/24/1937.
Today is 12/24/1937, the date tomorrow is 12/25/1937.
A: 12/25/1937

Q: This is the last day of 1899. What is the date 24 hours later in MM/DD/YYYY?
Explain: Today is the last day of 1899, so today is 12/31/1899.
The date 24 hours later of today is 01/01/1900.
A: 01/01/1900

Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 24 hours later in MM/DD/YYYY?
Explain: If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later than 06/01/1943.
Therefore, today is 06/02/1943.
24 hours later of today is 06/03/1943.
A: 06/03/1943

Q: The current local time is 3:02 pm of 5/4/2004. What is the date yesterday in MM/DD/YYYY?
Explain: The current local time is 3:02 pm of 5/4/2004
Therefore, today is 05/04/2004.
Yesterday is 05/03/2004.
A: 05/03/2004

Q: Today is 9/7. Jane is watching NFL 2003. What is the date one week ago from today in MM/DD/YYYY?
Explain: Today is 9/7, Jane is watching NFL 2003. Therefore, today is 09/07/2003.
1 week ago of today is 09/02/2003.
A: 09/02/2003

Q: Yesterday was 12/31/1929. Today could not be 12/32/1929 because December has only 31 days. What is the date a month ago in MM/DD/YYYY?
Explain: Yesterday was 12/31/1929.Therefore, today is 01/01/1930.
A month ago of today is 12/01/1929.
A: 12/01/1929

# Q: Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. What is the date one year ago from today in MM/DD/YYYY?
Explain: Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. Tomorrow is 10/16/1924, so today is 10/15/1924.
One year ago from today is 10/15/1923.
A: 10/15/1923

"""

date_CoT2_prompting = """
Q: Today is Apr 10, 1985. Jane's appointment will be 3 days later. What is the date one week from today in MM/DD/YYYY?
Explain: Today is Apr 10, 1985,  Jane's appointment will be 3 days later. So today is 04/10/1985. The date one week from today is 04/17/1985.
A: 04/17/1985

Q: Yesterday, Jan 21, 2011, Jane ate 2 pizzas and 5 wings. What is the date one week from today in MM/DD/YYYY?
Explain: Yesterday, Jan 21, 2011, Jane ate 2 pizzas and 5 wings. Then today is 01/22/2011. THe date one week from today is 01/29/2011.
A: 01/29/2011

Q: Tomorrow is 11/12/2019. What is the date today in MM/DD/YYYY?
Explain: Tomorrow is 11/12/2019, then today is 11/11/2019. The date today is 11/11/2019.
A: 11/11/2019

Q: This is the last day of 1899. What is the date yesterday in MM/DD/YYYY?
Explain: This is the last day of 1899, then today is 12/31/2019. The date yesterday is 12/30/2019.
A: 12/30/2019

Q: Jane scheduled 3 apointments with 5 poeple for tomorrow (Tue, 7/9/1972). What is the date 24 hours later in MM/DD/YYYY?
Explain: Jane scheduled 3 apointments with 5 poeple for tomorrow (Tue, 7/9/1972). Tomorrow is 07/09/1972, then today is 07/08/1972. The date 24 hours later is 07/09/1972.
A: 07/09/1972

Q: Today is the second day of the third month of 1966. What is the date one year ago from today in MM/DD/YYYY?
Explain: Today is the second day of the third month of 1966, then today is 03/02/1966.
One year ago from today is 03/02/1965.
A: 03/02/1965

Q: Jane is celebrating the last day of Jan 2012. What is the date tomorrow in MM/DD/YYYY?
Explain: Jane is celebrating the last day of Jan 2012. Then today is 01/31/2012. The date tomorrow is 02/01/2012.
A: 02/01/2012

"""

date_PoT1_prompting = """
# Write Python Code to solve the following questions.
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# Q: Today is Christmas Eve of 1937. What is the date tomorrow in MM/DD/YYYY?
# today is Christmas Eve of 1937, then today is 12/24/1937
today = date(1937, 12, 24)
# tomorrow
date_tomorrow = today + relativedelta(days=1)
# The answer formatted with %m/%d/%Y is
ans = date_tomorrow.strftime('%m/%d/%Y')

# Q: This is the last day of 1899. What is the date 24 hours later in MM/DD/YYYY?
# Today is the last day of 1899, then today is 12/31/1899
today = date(1899, 12, 31)
# 24 hours later
days_from_today = today + relativedelta(hours=24)
# The answer formatted with %m/%d/%Y is
ans = days_from_today.strftime('%m/%d/%Y')

# Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 24 hours later in MM/DD/YYYY?
# If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
today = date(1943, 6, 1) + relativedelta(days=1)
# 24 hours later
later = today + relativedelta(hours=24)
# The answer formatted with %m/%d/%Y is
ans = later.strftime('%m/%d/%Y')

# Q: The current local time is 3:02 pm of 5/4/2004. What is the date yesterday in MM/DD/YYYY?
# The current local time is 3:02 pm of 5/4/2004, then today is 5/4/2004
today = date(2004, 5, 4)
# yesterday
yesterday = today - relativedelta(days=1)
# The answer formatted with %m/%d/%Y is
ans = yesterday.strftime('%m/%d/%Y')

# Q: Today is 9/7. Jane is watching NFL 2003. What is the date one week ago from today in MM/DD/YYYY?",
# Today is 9/7, Jane is watching NFL 2003, then today is 09/07/2003
today = date(2003, 9, 7)
# 1 week ago,
one_week_ago = today - relativedelta(weeks=1)
# The answer formatted with %m/%d/%Y is
ans = one_week_ago.strftime('%m/%d/%Y')

# Q: Yesterday was 12/31/1929. Today could not be 12/32/1929 because December has only 31 days. What is the date a month ago in MM/DD/YYYY?
# Yesterday was 12/31/1929, then today is 12/31/1929
today = date(1930, 1, 1)
# a month ago
later = today - relativedelta(months=1)
# The answer formatted with %m/%d/%Y is
ans = later.strftime('%m/%d/%Y')

# Q: Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. What is the date one year ago from today in MM/DD/YYYY?
# tomorrow meeting is 10/16/1924, then today is 10/15/1924
today = datetime(1924, 10, 16) - relativedelta(days=1)
# one year ago
yesterday = today - relativedelta(years=1)
# The answer formatted with %m/%d/%Y is
ans = yesterday.strftime('%m/%d/%Y')

"""

date_PoT2_prompting = """
# Write Python Code to solve the following questions.
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# Q: Today is Apr 10, 1985. Jane's appointment will be 3 days later. What is the date one week from today in MM/DD/YYYY?
# today is Apr 10, 1985, then today is 04/10/1985
today = date(1985, 4, 10)
# one week from today
one_week_from_today = today + relativedelta(weeks=1)
# The answer formatted with %m/%d/%Y is
ans = one_week_from_today.strftime('%m/%d/%Y')

# Q: Yesterday, Jan 21, 2011, Jane ate 2 pizzas and 5 wings. What is the date one week from today in MM/DD/YYYY?
# Yesterday, Jan 21, 2011, then today is Jan 22, 2011
today = date(2011, 1, 22)
# one week from today
one_week_from_today = today + relativedelta(weeks=1)
# The answer formatted with %m/%d/%Y is
ans = one_week_from_today.strftime('%m/%d/%Y')

# Q: Tomorrow is 11/12/2019. What is the date today in MM/DD/YYYY?
# Tomorrow is 11/12/2019, then today is 11/11/2019
today = date(2019, 11, 11)
# The answer formatted with %m/%d/%Y is
ans = today.strftime('%m/%d/%Y')

# Q: This is the last day of 1899. What is the date yesterday in MM/DD/YYYY?
# This is the last day of 1899, then today is 12/31/1899
today = date(1899, 12, 31)
# the date yesterday
yesterday = today - relativedelta(days=1)
# The answer formatted with %m/%d/%Y is
ans = yesterday.strftime('%m/%d/%Y')

# Q: Jane scheduled 3 apointments with 5 poeple for tomorrow (Tue, 7/9/1972). What is the date 24 hours later in MM/DD/YYYY?
# Jane scheduled 3 apointments with 5 poeple for tomorrow (Tue, 7/9/1972), then today is 07/08/1972
today = date(1972, 7, 8)
# date 24 hours later
date_24_hours_later = today + relativedelta(hours=24)
# The answer formatted with %m/%d/%Y is
ans = date_24_hours_later.strftime('%m/%d/%Y')

# Q: Today is the second day of the third month of 1966. What is the date one year ago from today in MM/DD/YYYY?
# Today is the second day of the third month of 1966, then today is 03/02/1966
today = date(1966, 3, 2)
# one year ago
one_year_ago = today - relativedelta(years=1)
# The answer formatted with %m/%d/%Y is
ans = one_year_ago.strftime('%m/%d/%Y')

# Q: Jane is celebrating the last day of Jan 2012. What is the date tomorrow in MM/DD/YYYY?
# Jane is celebrating the last day of Jan 2012, then today is 01/31/2012
today = date(2012, 1, 31)
# tomorrow
tomorrow = today + relativedelta(days=1)
# The answer formatted with %m/%d/%Y is
ans = tomorrow.strftime('%m/%d/%Y')

"""