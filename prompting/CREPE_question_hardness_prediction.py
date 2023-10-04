crepe_hard_prediction_only_question_prompt = """Predict the hardness level of the questions.
Goal: Making Matcha Green Tea the Traditional Way
Current_Context: Boil 3/4 cup (180 ml) of water and pour it into your matcha bowl. Whisk the hot water with a chasen. Discard the hot water from the bowl. Scoop 2 tsp (1.5 heaping teaspoons or 10 g) of matcha into a fine mesh strainer. Sift the matcha into your empty, dry bowl. Pour boiling water into a teacup. Add a small amount of hot water into the matcha bowl and whisk it.
Question: What's the likelihood that I drink the matcha?
Level: Easy

Goal: Boating in lake
Current_Context: Rent a boat. Find a lake which allows boating. Drive to the lake and set the boat in lake.
Question: What's the likelihood that the boat is in lake?
Level: Easy

Goal: Clean White Shoes
Current_Context: Mix dish soap into warm water. Clean the soles and rubber pieces with a magic eraser.
Question: What's the likelihood that the shoes is wet?
Level: Easy

Goal: Germinate Tree Seeds
Current_Context: Add stones and natural compost to a plant pot. Plant the seeds.
Question: What's the likelihood that seeds is in soil?
Level: Easy

Goal: Washing dishes
Current_Context: Put the dirty dishes in the sink. Put dish soap on the sponge. Scrub each dishes with the sponge until clean. . Place each clean dish in the drying rack. . Clean and store the sponge.
Question: What's the likelihood that Bubbles can be seen on the sponge.
Level: Hard

Goal: Bake a potato
Current_Context: Choose the right type of potato. Wash the potato. Season the potato with olive oil and black pepper. Put the potato on a microwavable plate. Put the plate in the microwave and choose a cook time. Microwave the potato.",
Question: What's the likelihood that Smoke can be seen around the potato.
Level: Hard

Goal: Play your first game on the Playstation
Current_Context: Buy a Playstation . Connect the Playstation to the TV. Plug the Playstation to a electrical outlet.
Question: What's the likelihood that the Playstation is powered?
Level: Easy

"""

crepe_hard_prediction_with_answer_prompt = """Generate feedback and predict if the generated answer is trustful.
Goal: Making Matcha Green Tea the Traditional Way
Current_Context: Boil 3/4 cup (180 ml) of water and pour it into your matcha bowl. Whisk the hot water with a chasen. Discard the hot water from the bowl. Scoop 2 tsp (1.5 heaping teaspoons or 10 g) of matcha into a fine mesh strainer. Sift the matcha into your empty, dry bowl. Pour boiling water into a teacup. Add a small amount of hot water into the matcha bowl and whisk it.
Question: What's the likelihood that I drink the matcha?
Explain:For step 1, after boiling water and pouring it into the matcha bowl, that I drink the matcha is "less likely" because the matcha has not been prepared yet.
For step 2, after whisking the hot water with a chasen, that I drink the matcha is "less likely" because the matcha has not been prepared yet.
For step 3, after discarding the hot water from the bowl, that I drink the matcha is "less likely" because the matcha has not been prepared yet.
For step 4, after scooping matcha into a fine mesh strainer and sifting it into the bowl, that I drink the matcha is "equally likely" because the matcha has been prepared but not yet added to the teacup.
For step 5, after pouring boiling water into a teacup, that I drink the matcha is "less likely" because the matcha has not been added to the teacup yet.
For step 6, after adding a small amount of hot water into the matcha bowl and whisking it, that I drink the matcha is "more likely" because the matcha has been prepared and added to the teacup.
Therefore, in the final step, the event is "more likely".
Feedback: The answer is correct.
Trustful: Yes

Goal: Boating in lake
Current_Context: Rent a boat. Find a lake which allows boating. Drive to the lake and set the boat in lake.
Question: What's the likelihood that the boat is in lake?
Explain: For step 1, after renting a boat, that the boat is in the lake is "less likely" because the boat is not yet in the lake.
For step 2, after finding a lake which allows boating, that the boat is in the lake is "equally likely" because we have found a lake but the boat is not yet in the lake.
For step 3, after driving to the lake and setting the boat in the lake, that the boat is in the lake is "more likely" because we have set the boat in the lake.
Therefore, in the final step, the event is "more likely".
Feedback: The answer is correct.
Trustful: Yes

Goal: Clean White Shoes
Current_Context: Mix dish soap into warm water. Clean the soles and rubber pieces with a magic eraser.
Question: What's the likelihood that the shoes is wet?
Explain: For step 1, after mixing dish soap into warm water, the likelihood that the shoes are wet is "less likely" because the shoes have not been directly exposed to water yet.
For step 2, after cleaning the soles and rubber pieces with a magic eraser, the likelihood that the shoes are wet is "more likely" because the magic eraser is damp and may have transferred some moisture to the shoes.
Therefore, in the final step, the event is "more likely".
Feedback: The answer is correct.
Trustful: Yes

Goal: Germinate Tree Seeds
Current_Context: Add stones and natural compost to a plant pot. Plant the seeds.
Question: What's the likelihood that seeds is in soil?
Explain: For step 1, after adding stones and natural compost to a plant pot, the likelihood that the seeds are in soil is "less likely" because the stones and natural compost are added to the pot, but the seeds are not yet planted in the soil.
For step 2, after planting the seeds, the likelihood that the seeds are in soil is "more likely" because the seeds are now planted in the soil.
Therefore, in the final step, the event is "more likely".
Feedback: The answer is correct.
Trustful: Yes

Goal: Washing dishes
Current_Context: Put the dirty dishes in the sink. Put dish soap on the sponge. Scrub each dishes with the sponge until clean. . Place each clean dish in the drying rack. . Clean and store the sponge.
Question: What's the likelihood that Bubbles can be seen on the sponge.
Explain: For step 1, after putting the dirty dishes in the sink, that bubbles can be seen on the sponge is "less likely" because there is no sponge involved yet.
For step 2, after putting dish soap on the sponge, that bubbles can be seen on the sponge is "more likely" because we put dish soap on the sponge.
For step 3, after scrubbing each dish with the sponge until clean, that bubbles can be seen on the sponge is "more likely" because the sponge is being used to clean the dishes.
For step 4, after placing each clean dish in the drying rack, that bubbles can be seen on the sponge is "less likely" because we are not using the sponge anymore.
For step 5, after cleaning and storing the sponge, that bubbles can be seen on the sponge is "less likely" because we have cleaned the sponge and there is no soap left on it.
Therefore, in the final step, the event is "less likely".
Feedback: When cleaning the sponge, we would be more likely to see the bubbles.
Trustful: No

Goal: Bake a potato
Current_Context: Choose the right type of potato. Wash the potato. Season the potato with olive oil and black pepper. Put the potato on a microwavable plate. Put the plate in the microwave and choose a cook time. Microwave the potato.",
Question: What's the likelihood that Smoke can be seen around the potato.
Explain: For step 1, after choosing the right type of potato, that smoke can be seen around the potato is "less likely" because the type of potato chosen does not affect the likelihood of smoke.
For step 2, after washing the potato, that smoke can be seen around the potato is "less likely" because washing the potato does not affect the likelihood of smoke.
For step 3, after seasoning the potato with olive oil and black pepper, that smoke can be seen around the potato is "less likely" because seasoning the potato does not affect the likelihood of smoke.
For step 4, after putting the potato on a microwavable plate, that smoke can be seen around the potato is "less likely" because placing the potato on a plate does not affect the likelihood of smoke.
For step 5, after putting the plate in the microwave and choosing a cook time, that smoke can be seen around the potato is "less likely" because choosing the cook time does not affect the likelihood of smoke.
For step 6, after microwaving the potato, that smoke can be seen around the potato is "less likely" because if the potato is cooked properly, it should not produce smoke.
Therefore, in the final step, the event is "less likely".
Feedback: When microwaving the potato, we would be more likely to see the smoke than we put it here without heating.
Trustful: No

Goal: Play your first game on the Playstation
Current_Context: Buy a Playstation . Connect the Playstation to the TV. Plug the Playstation to a electrical outlet.
Question: What's the likelihood that the Playstation is powered?
Explain: For step 1, after buying a Playstation, that the Playstation is powered is "less likely" because it needs to be connected to an electrical outlet to be powered.
For step 2, after connecting the Playstation to the TV, that the Playstation is powered is "less likely" because it still needs to be connected to an electrical outlet to be powered.
For step 3, after plugging the Playstation to an electrical outlet, that the Playstation is powered is "more likely" because it is now connected to a power source.
Therefore, in the final step, the event is "more likely".
Feedback: The answer is correct.
Trustful: Yes

"""