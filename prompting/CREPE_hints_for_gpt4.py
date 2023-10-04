crepe_hints_prompt = """Given the hints(may not be correct), answer the question with "more likely", "equally likely" or "less likely". 
Goal: Buy a flight ticket from SF to Hawaii.
Context: Open google flights and check the flights availability during the dates wanted. Choose non-stop flights and check if the time slots work. After deciding right time slots and price, proceed to buy tickets. Got an email confirmation of reservation.
Question: Jane was born on the last day of Feburary in 2000. Today is her 16-year-old birthday. What is the date 24 hours later in MM/DD/YYYY?
Hints: The answer may be near "more likely" or "less likely".
Explain: For step 1, after checking flights availability, that I can refund the ticket if it is refundable is "equally likely" because I haven't purchased the ticket yet.
For step 2, after choosing non-stop flights and checking if the time slots work, that I can refund the ticket if it is refundable is "equally likely" because I haven't purchased the ticket yet.
For step 3, after deciding on the right time slots and price and proceeding to buy tickets, that I can refund the ticket if it is refundable is "less likely" because I have already purchased the ticket.
For step 4, after getting an email confirmation of reservation, that I can refund the ticket if it is refundable is "more likely" because I can check the terms and conditions of the ticket and see if it is refundable or not.
Therefore, in the final step, the event is "more likely".
Answer: more likely

Goal: Make a bed
Context: Strip the sheets from the mattress and pillows.
Question: What's the likelihood that the mattress is covered?
Hints: The answer may be near "more likely" or "less likely".
Explain: Since we have only completed the first step of stripping the sheets from the mattress and pillows, it is "less likely" that the mattress is covered.
Answer: less likely

Goal: Changing a flat tire with a spare tire
Context: Grab spare tire from bottom layer of the trunk. Place spare tire on the side. Lift car using scissor jack. Grab wrench to unbolt flat tire bolts.
Question: What's the likelihood that flat tire is secured?
Hints: The answer may be near "less likely" or "equally likely".
Explanation: For step 1, after grabbing the spare tire, that the flat tire is secured is "equally likely" because we haven't done anything to secure the flat tire yet.
For step 2, after placing the spare tire on the side, that the flat tire is secured is "equally likely" because we haven't done anything to secure the flat tire yet.
For step 3, after lifting the car using a scissor jack, that the flat tire is secured is "less likely" because the car is lifted and the flat tire may move around.
For step 4, after grabbing the wrench to unbolt the flat tire bolts, that the flat tire is secured is "less likely" because we are removing the bolts that secure the tire.
Therefore, in the final step, the event is "less likely".
Answer: less likely

"""