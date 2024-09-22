import requests

prompt = """
    Here is my company data:
    net promoter score: 74
    Average rating: 4.358/5
    Sentiments about environment, food, service: +0.99, +0.64, +0.6
    Bad review: "I had dinner at Sampan last week when I was in Philadelphia for a short trip. I selected the chef's tasting menu (5 selections from the menu and 2 mini ice cream cones for $55/pp). I enjoyed some but not all of the dishes I tried. From "Small," I selected the seafood shumai (with pork, soy, and red vinegar), which was one of my favorites. I would order this dish again. From "Satay," I ordered wagyu beef (with apricot and yakitori glaze), which was okay (the beef wasn't very tender, but I didn't have a knife - so one of the pieces on the skewer gave me a hard time (chew chew chew). For "Cold + Hot," I selected the char siu rib (with honey and pickled daikon), which was good except I was expecting a rib with the whole bone still inside and the rib I received only had part of a bone in it (which made it harder to eat - I pulled it off the mini/half bone with my fork, but ended up getting some pieces of what I think was cartilage). You choose one dish from "Meat" or "Fish," and I selected the roasted branzino (with long bean, garlic, and black bean), which was my other favorite dish of the night (very flavorful). From "Sides," I selected the roasted broccoli (with pine nut, white soy, and garlic), which was a little disappointing (it seemed steamed, not roasted - no color on it; the florets were really big, which made it hard to eat with just chopsticks and fork - still no knife; the menu didn't mention chili and the dish was actually just very spicy). The 2 mini ice cream cones were simple and delicious and a great way to end the meal. The service was good, and the restaurant had a cool vibe (modern, fun, bright). I was so surprised how busy it was at 4:30pm on a Saturday (almost packed), but I had a reservation. Overall, it was an okay meal, but I wasn't in love with the food overall."
    Good review: "I heard about this place from a friend. She said this was her favorite asian fusion spot ever! I also happened to be in town during restaurant week, so I had to try it. It was even walking distance from my hotel! EXPERIENCE The Restaurant Week Deal: Small dish, Satay, Cold+ Hot, Meat or Fish, Side dish [5 smaller dishes total] I made a reservation for one, same day, and I arrived early. They were able to seat me at the food bar, which was fun to watch the chefs prepare the food. The server was very kind and patient as I took a while to decide what I wanted, theres so many options! She also gave me some advice on which meat/fish dish to order, and non-alcoholic drink suggestions. The food came out fast. There was a mistake, I received some spring rolls that I did not order, but she immediately recognized the mistake and made sure my actual appetizer was coming. The portions were overall pretty good, especially when I believe the restaurant week deal gave smaller ones, and I was just eating for one! FOOD Chef's Tasting Menu - Restaurant Week (3/5) Beef Mandu (sesame, kimchi, scallion) - the dish was kind of small, two small mandu. They are pan fried. They are just sitting in soy sauce which was not desirable to me. Don't love the kimchi, it was not fermented long enough it seems. The meat filling is spicy. It was not bad, but I would not order it again. (3/5) Wagyu Beef Skewer (apricot, Yakitori glaze) - the yakitori glaze is very salty. The sauce is very fruity sweet, like a jam. They go fine together. Cooked medium well. The beef was not super soft melt in your mouth. I think the short rib skewer would've been the better choice in this case. (5/5) Crispy Shrimp (radish, yuzu, chili aioli) - super crunchy! Kind of like walnut shrimp but spicy, and no nuts. Radish is pickled, refreshing tangy contrast, borderline surprising. (6/5) Glazed Chilean Sea Bass - wow this is so insanely good! Fish and curry are both great. Fish is soft, and succulent, practically melts in your mouth. The yellow curry is light but impactful. Super creamy, very flavorful. Love! (4/5) Crispy Brussels Sprout (puffed rice, fish sauce, chili) - good texture. Well roasted, not dry. Fish sauce is amazing, not overpowering. Not spicy even though it list chili as an ingredient. No gross smelly brussel sprout taste. Quite enjoyable. Ice cream mini cones: (4/5) Chocolate Peanut Butter (no picture) - tastes like a peanut butter cup (5/5) Cinnamon Toast - this one was great! Tastes just like cinnamon toast crunch, but in ice cream form. Would order this separately if I could Drink (3/5) Virgin Summer in Okinawa (mango, pineapple, ginger) - strong ginger flavor! A bit of pineapple taste. Can't really find the mango, kind of just adds texture, to thicken it up. OVERALL The food was really flavorful and creative. I enjoyed everything overall. The service was great, the staff was super nice. I can see why my friend really enjoyed it here. I would most definitely come back if I live here, and they have a chefs tasting menu that is a bit more money, but includes 7 dishes, which still seems like a really solid deal!"

    Provide me actionable insights to improve my business. Mostly provide general insights, but also a few specific insights based on the reviews.
"""

url = "https://proxy.tune.app/chat/completions"
headers = {
    "Authorization": "sk-tune-LWw4p6Gu8psAwdpVfL4eLkwLtNctxp416KL",
    "Content-Type": "application/json",
}
data = {
"temperature": 0.9,
    "messages":  [
    {
        "role": "system",
        "content": "You are an expert on maximizing small businesses. You will be given metrics and reviews and such data. Sometimes you will be asked to give recommendations for the business to improve, other times you will simply summarize what you're given."
    },
    {
        "role": "user",
        "content": prompt,
    }
    ],
    "model": "meta/llama-3.1-8b-instruct",
    "stream": False,
    # "frequency_penalty":  0.2,
    # "max_tokens": 100
}
response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])