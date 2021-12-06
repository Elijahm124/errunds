dic = {
    "Salads/Bowls": [],
    "Smoothies": [],
    "Culture/Cuisine": [],
    "Burgers": [],
    "Sandwiches/Sliced Bread": [],
    "Roll": [],
    "Hero": [],
    "Wrap": [],
    "Panini": [],
    "Quesadilla": [],
    "Gyro": [],
    "Sides": [],
    "Breakfast": [],
    "Cafe": [],
    "Soups": [],
    "Bagels": [],
    "Fruit": [],
    "Vegetables": [],
    "Meat": [],
    "Candy/Chocolate": [],
    "Kombucha": [],
    "Flavored Drinks": [],
    "Juice": [],
    "Sports/Energy Drinks": [],
    "Tea/Infusions": [],
    "Vinegar Drinks": [],
    "Water": [],
    "Snack Foods": [],
    "Condiments/Sauces": [],
    "Cooking/Baking Ingredients": [],
    "Cold Cuts": [],
    "Cheese Cold Cuts": [],
    "Seafood": [],
    "Eggs": [],
    "Nuts/Seeds": [],
    "Seasonings/Spices": [],
    "Tofu": [],
    "Soy/Vegetarian Products": [],
    "Chewing Tobacco": [],
    "Packaged Soups/Broths": [],
    "Rice, Pasta, Noodles/Grains": [],
    "Frozen Foods": [],
    # "Cereal": [],
    "Desserts": [],
    "Baby Food/Formula": [],
    "Powdered Beverages and Mixes": [],
    "Breads, Rolls/Bakery": [],
    "Large Chips": [],
    "Salsas/Dips": [],
    "Carbonated and Seltzer Drinks": [],
    "Coffee and Dairy Drinks": [],
    "Dairy and Milk": [],
    "Non-Dairy": [],
    "Ice": [],
    "Vitamins/Health Supplements": [],
    "Jams/Spreads/Pantry": [],
    "Cereal and Granola": [],
    "Canned Goods": [],
    "Ground Coffee/Tea Bags": [],
    "Oil/Butter": [],
    "Hemp Infused Drinks": [],
    "Protein Drinks": [],
    "Tonic Drinks": [],
    "Hard Kombucha/Tea": [],
    "Hard Seltzer": [],
    "Beer": [],
    "Wine/Spirit": [],
    "Yogurt": [],
    "Body Care": [],
    "First Aid": [],
    "OTC Medicine/Drugs": [],
    "Sexual Health": [],
    "Vision Care": [],
    "Oral Care": [],
    "Shaving/Grooming": [],
    "Beauty and Cosmetics": [],
    "Deodorant/Antiperspirant": [],
    "Feminine Products": [],
    "COVID-Care": [],
    "Cigarettes": [],
    "Cigars/Loose Tobacco": [],
    "Smoking Pipes": [],
    "Vaporizers/Electronic Cigarettes": [],
    "Fitness, Sports/Outdoor": [],
    "Laundry Care": [],
    "Cleaning Supplies": [],
    "Safety/Security": [],
    "Pest Control": [],
    "Food storage, Utensils/Paper/Plastic Products": [],
    "Home/Kitchen": [],
    "Household Appliances": [],
    "Plants, Garden/Outdoor": [],
    "Tools/Home Improvement": [],
    "Home Decor": [],
    "Bedding/Bath": [],
    "Office Supplies": [],
    "Electronics/Batteries": [],
    "Computer/Cell phone Accessories": [],
    "Greeting Cards": [],
    "Party Supplies": [],
    "Travel Accessories": [],
    "Scarves/Gloves Baby": [],
    "Pet food": [],
    "Pet supplies": [],
    "Automotive": [],
    "Parts/Accessories": [],
    "Candles/ scents ": [],
}

subcategories = "project1/subcategories"
with open(subcategories) as s:
    count = 0
    for i, line in enumerate(s):
        line = line.lower()
        if "cereal" in line or "granola" in line or "breakfast food" in line:
            dic["Cereal and Granola"].append(i)
            count += 1
        elif "seeds" in line or "nuts" in line:
            dic["Nuts/Seeds"].append(i)
            count += 1
        elif "chocolate" in line or "candy" in line or "choclate" in line \
                or "candies" in line or "fruit snack" in line or "bites" in line:
            dic["Candy/Chocolate"].append(i)
            count += 1
        elif "fruit" in line:
            dic["Fruit"].append(i)
            count += 1
        elif "dairy" in line or "milk" in line or "ice cream" in line:
            dic["Dairy and Milk"].append(i)
            count += 1
        elif "snack" in line or "cracker" in line \
                or "pretzel" in line or "bar" in line or "dried" in line:
            dic["Snack Foods"].append(i)
            count += 1
        elif "rice" in line or "grain" in line \
                or "pasta" in line:
            dic["Rice, Pasta, Noodles/Grains"].append(i)
            count += 1
        elif "vegetable" in line:
            dic["Vegetables"].append(i)
            count += 1
        elif "bakery" in line or "bread" in line:
            dic["Breads, Rolls/Bakery"].append(i)
            count += 1
        elif "condiment" in line or "sauce" in line \
                or "dressing" in line:
            dic["Condiments/Sauces"].append(i)
            count += 1
        elif "salsa" in line or "dip" in line \
                or "cream" in line or "hummus" in line:
            dic["Salsas/Dips"].append(i)
            count += 1
        elif "oil" in line or "butter" in line:
            dic["Oil/Butter"].append(i)
            count += 1
        elif "flavored drink" in line:
            dic["Flavored Drinks"].append(i)
            count += 1
        elif "packaged soup" in line or "broth" in line:
            dic["Packaged Soups/Broths"].append(i)
            count += 1
        elif "seafood" in line:
            dic["Seafood"].append(i)
            count += 1
        elif "kombucha" in line:
            dic["Kombucha"].append(i)
            count += 1
        elif "cat food" in line:
            dic["Pet food"].append(i)
            count += 1
        elif "kitchen" in line:
            dic["Home/Kitchen"].append(i)
            count += 1
        elif "tea/coffee" in line or "health care" in line:
            dic["Ground Coffee/Tea Bags"].append(i)
            count += 1
        elif "fragrance" in line:
            dic["Deodorant/Antiperspirant"].append(i)
            count += 1
        elif "cheese" in line:
            dic["Cheese Cold Cuts"].append(i)
            count += 1
        elif "fried" in line or "chip" in line or "pop corn" in line:
            dic["Large Chips"].append(i)
            count += 1
        elif "tea" in line:
            dic["Tea/Infusions"].append(i)
            count += 1
        elif "baby" in line:
            dic["Baby Food/Formula"].append(i)
            count += 1
        elif "cone" in line:
            dic["Jams/Spreads/Pantry"].append(i)
            count += 1
        elif "cook" in line or "brownie" in line \
                or "biscuit" in line or "sandwich" in line \
                or "blondie" in line or "wafel" in line:
            dic["Desserts"].append(i)
            count += 1
        elif "protein drink" in line:
            dic["Protein Drinks"].append(i)
            count += 1
        elif "spice" in line:
            dic["Seasonings/Spices"].append(i)
            count += 1
        else:
            print(i)

print("\n")
print(count)

lst = [0 for i in range(1500)]

for key, values in dic.items():
    for i in values:
        lst[i] = key
print(lst)

new_subcategories = "project1/new_subcategories"
with open(new_subcategories, "w") as ns1:
    ns1.write("")
with open(new_subcategories, "a") as ns2:
    for subcategory in lst:
        ns2.write(f"{subcategory}\n")
