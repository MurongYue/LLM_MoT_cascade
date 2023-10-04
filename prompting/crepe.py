crepe_pot1_prompt = """# Answer the question. The answers are from "more likely", "equally likely" and "less likely".
# Goal: Wash sneakers
# Current_Context: Brush off dirt from the surface of the sneakers. Remove shoelaces. Rinse the shoelaces in soapy water and air dry. Apply mild detergent to the sneakers and rub gently.
# Question: What's the likelihood that The sneakers are damp?
# Python code
class Wash_Sneakers():
    # Init from Current_Context
    # Brush off dirt from the surface of the sneakers 
    # Remove shoelaces
    # Rinse the shoelaces in soapy water and air dry
    # Apply mild detergent to the sneakers and rub gently.
    def __init__(self):
        self.event0 = None # event0 is the likelihood that The sneakers are damp.
    def brush_off_dirt(self):
        # After brushing off dirt, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def remove_shoelaces(self):
        # After removing shoelaces, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def rinse_shoelace_in_water(self):
        # After rinsing in water, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def apply_detergent_sneaker(self):
        # After rinsing in water, event0 becomes "more likely"
        self.event0 = "more likely"
    def call_all_funcs_in_order(self):
        self.brush_off_dirt()
        self.remove_shoelaces()
        self.rinse_shoelace_in_water()
        self.apply_detergent_sneaker()
c = Wash_Sneakers()
c.call_all_funcs_in_order()
ans = c.event0

# Goal: Dispose of Dog Poop
# Current_Context: Pick up dog poop. Place the dog poop in a plastic bag. Tie up the bag neatly.
# Question: What's the likelihood that the poop is exposed to air
# Python code
class Dispose_Dog_poop():
    # Init from Current_Context
    # Pick up dog poop.
    # Place the dog poop in a plastic bag.
    # Tie up the bag neatly.
    def __init__(self):
        self.event0 = None # event0 is the likelihood that the poop is exposed to air
    def pick_up_dog_poop(self):
        # After picking up dog poop, event0 becomes "more likely"
        self.event0 = "more likely"
    def place_poop_in_bag(self):
        # After picking up dog poop, event0 becomes "less likely"
        self.event0 = "less likely"
    def tie_up_bag_neatly(self):
        # After picking up dog poop, event0 becomes "less likely"
        self.event0 = "less likely"
    def call_all_funcs_in_order(self):
        self.pick_up_dog_poop()
        self.place_poop_in_bag()
        self.tie_up_bag_neatly()
c = Dispose_Dog_poop()
c.call_all_funcs_in_order()
ans = c.event0

# Goal: Start a YouTube channel
# Current_Context: Decide on a theme and be prepared to stick to it in the long run. Come up with a channel name. 
Register a Google account if you don't have one. Create your YouTube channel with your Google account.  
Procure a banner art and add it to your main page. Upload your first video.
# Question: What's the likelihood that Someone watches a video from my channel.
# Python code
class Start_Youtube_Channel():
    # Init from Current_Context
    # Decide on a theme and be prepared to stick to it in the long run
    # Come up with a channel name.
    # Register a Google account
    # Create your YouTube channel with your Google account
    # Procure a banner art and add it to your main page.
    # Upload your first video.
    def __init__(self):
        self.event0 = None # event0 is the likelihood that someone watches a video from my channel.
    def decide_on_theme(self):
        # After deciding on theme, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def come_up_channel_name(self):
        # After coming up channel name, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def register_Google_account(self):
        # After registering account, event0 becomes "equally likely"  
        self.event0 = "equally likely"
    def create_Youtube_channel(self):
        # After creating Youtube channel, event0 becomes "equally likely"  
        self.event0 = "equally likely"
    def procure_banner(self):
        # After procuring banner, event0 becomes "equally likely"  
        self.event0 = "equally likely"
    def upload_video(self):
        # After uploading video, event0 becomes "more likely"  
        self.event0 = "more likely"
    def call_all_funcs_in_order(self):
        self.decide_on_theme()
        self.come_up_channel_name()
        self.register_Google_account()
        self.create_Youtube_channel()
        self.procure_banner()
        self.upload_video()
c = Start_Youtube_Channel()
c.call_all_funcs_in_order()
ans = c.event0

"""

crepe_pot2_prompt = """# Answer the question. The answers are from "more likely", "equally likely" and "less likely".
# Goal: Grind coffee beans
# Current_Context: Prepare a sealed jar. Open the lid of the jar. Open the coffee bean bag. Open the lid of the grinder. Pour some coffee beans to the grinder.
# Question: What's the likelihood that the grinder is empty
# Python code
class Grind_Coffee_Beans():
    # Init from Current_Context
    # Prepare a sealed jar 
    # Open the lid of the jar. 
    # Open the coffee bean bag 
    # Open the lid of the grinder.
    # Pour some coffee beans to the grinder
    def __init__(self):
        self.event0 = None # event0 is the likelihood that the grinder is empty
    def prepare_jar(self):
        # After preparing a sealed jar, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def open_lid_jar(self):
        # After opening the lid of jar, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def open_coffee_bag(self):
        # After opening coffee bag, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def open_lid_grinder(self):
        # After opening lid of grinder, event0 becomes "more likely"
        self.event0 = "more likely"
    def pour_beans_grinder(self):
        # After pouring some coffee beans to the grinder, event0 becomes "less likely"
        self.event0 = "less likely"
    def call_all_funcs_in_order(self):
        self.prepare_jar()
        self.open_lid_jar()
        self.open_coffee_bag()
        self.open_lid_grinder()
        self.pour_beans_grinder()
c = Grind_Coffee_Beans()
c.call_all_funcs_in_order()
ans = c.event0

# Goal: Clean toilet bowl
# Current_Context: Flush toilet. Pour 1/3 cup of bleach into the bowl.
# Question: What's the likelihood that Someone uses the toilet.
# Python code
class Clean_Toilet_Bowl():
    # Init from Current_Context
    # Flush toilet.
    # Pour 1/3 cup of bleach into the bowl.
    def __init__(self):
        self.event0 = None # event0 is the likelihood that Someone uses the toilet.
    def flush_toilet(self):
        # After flushing toilet, event0 becomes "less likely"
        self.event0 = "less likely"
    def pour_bleach_bowl(self):
        # After pouring 1/3 cup of bleach into the bowl, event0 becomes "less likely"
        self.event0 = "less likely"
    def call_all_funcs_in_order(self):
        self.flush_toilet()
        self.pour_bleach_bowl()
c = Clean_Toilet_Bowl()
c.call_all_funcs_in_order()
ans = c.event0

# Goal: Place a Coin in the Door Hinge
# Current_Context: Grab a coin. Open the door slightly.
# Question: What's the likelihood that A person enters through the door.
# Python code
class Place_Coin_Door_Hinge():
    # Init from Current_Context
    # Grab a coin.
    # Open the door slightly.
    def __init__(self):
        self.event0 = None # event0 is the likelihood that A person enters through the door.
    def grab_coin(self):
        # After grabing a coin, event0 becomes "equally likely"
        self.event0 = "equally likely"
    def open_door(self):
        # After opening the door slightly, event0 becomes "more likely"
        self.event0 = "more likely"
    def call_all_funcs_in_order(self):
        self.grab_coin()
        self.open_door()
c = Place_Coin_Door_Hinge()
c.call_all_funcs_in_order()
ans = c.event0

"""

crepe_cot1_prompt = """Answer the question. The final answers are from "more likely", "equally likely" and "less likely".
Goal: Wash sneakers
Current_Context: Brush off dirt from the surface of the sneakers. Remove shoelaces. Rinse the shoelaces in soapy water and air dry. Apply mild detergent to the sneakers and rub gently.
Question: What's the likelihood that The sneakers are damp?
Explain: 
For step 1, after brushing off dirt, the sneakers are damp is "equally likely" because there is no change for the dampness of the shoes.
For step 2, after removing shoelaces, the sneakers are damp is "equally likely" because there is no change for the dampness of the shoes.
For step 3, after rinsing the shoelaces in soapy water and air dry, the sneakers are damp is "equally likely" because we removed the shoelace from the sneaker so we don't change the dampness of sneaker.
For step 4, after applying mild detergent to the sneakers and rubbing gently, the sneakers are damp is "more likely" because we put mild detergent to the sneakers.
Therefore, in the final step, the event is "more likely".
Answer: more likely

Goal: Dispose of Dog Poop
Current_Context: Pick up dog poop. Place the dog poop in a plastic bag. Tie up the bag neatly.
Question: What's the likelihood that the poop is exposed to air
Explain: 
For step 1, after picking up dog poop, that the poop is exposed to air is "equally likely" because there is no change for the air.
For step 2, after placing the dog poop in a plastic bag, that the poop is exposed to air is "less likely" because the dog poop is in a plastic bag now.
For step 3, after tie up the bag neatly, that the poop is exposed to air is "less likely" because when we tied up the bag neatly, the dog poop is not exposed to the air.
Therefore, in the final step, the event is "less likely".
Answer: less likely

Goal: Start a YouTube channel
Current_Context: Decide on a theme and be prepared to stick to it in the long run. Come up with a channel name. Register a Google account if you don't have one. Create your YouTube channel with your Google account.  Procure a banner art and add it to your main page. Upload your first video.
Question: What's the likelihood that Someone watches a video from my channel.
Explain: 
For step 1, after deciding on a theme, that someone watches a video from my channel is "equally likely" because there is no video yet.
For step 2, after coming up with a channel name, that someone watches a video from my channel is "equally likely" because there is no video yet in the channel.
For step 3, after registering a Google account, that someone watches a video from my channel is "equally likely" because there is no video yet in the channel.
For step 4, after creating your YouTube channel, that someone watches a video from my channel is "equally likely" because there is no video yet in the channel.
For step 5, after procuring a banner art, that someone watches a video from my channel is "equally likely" because there is no video yet in the channel.
For step 6, after uploading your first video, that someone watches a video from my channel is "more likely" because you uploaded a video then someone may have a chance to watch it.
Therefore, in the final step, the event is "more likely".
Answer: more likely

"""

crepe_cot2_prompt = """Answer the question. The final answers are from "more likely", "equally likely" and "less likely".
Goal: Grind coffee beans
Current_Context: Prepare a sealed jar. Open the lid of the jar. Open the coffee bean bag. Open the lid of the grinder. Pour some coffee beans to the grinder.
Question: What's the likelihood that the grinder is empty
Explain: 
For step 1, after preparing a sealed jar, that the grinder is empty is "equally likely" because there is no change for the grinder.
For step 2, after opening the lid of the jar, that the grinder is empty is "equally likely" because there is no change for the grinder.
For step 3, after opening the coffee bean bag, that the grinder is empty is "equally likely" because there is no change for the grinder.
For step 4, after opening the lid of the grinder, that the grinder is empty is "equally likely" because we don't pour anything into it.
For step 5, after pouring some coffee beans to the grinder, that the grinder is empty is "less likely" because we pour something into it, then the grinder may not empty now.
Therefore, in the final step, the event is "less likely".
Answer: less likely

Goal: Clean toilet bowl
Current_Context: Flush toilet. Pour 1/3 cup of bleach into the bowl.
Question: What's the likelihood that Someone uses the toilet.
Explain: 
For step 1, after flushing toilet, that Someone uses the toilet is "less likely" because we need to wait until there is no one using the toilet, then we can clean the bowl.
For step 2, after pouring 1/3 cup of bleach into the bowl, that Someone uses the toilet is "less likely" because we need to wait until there is no one using the toilet, then we can pour the blench.
Therefore, in the final step, the event is "less likely".
Answer: less likely

Goal: Place a Coin in the Door Hinge
Current_Context: Grab a coin. Open the door slightly.
Question: What's the likelihood that A person enters through the door.
Explain: 
For step 1, after grabing a coin, that A person enters through the door is "equally likely" because there is no change for the door.
For step 2, after opening the door slightly, that A person enters through the door is "more likely" because we open the door, then a person may enter through the door now.
Therefore, in the final step, the event is "more likely".
Answer: more likely

"""