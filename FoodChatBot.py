class FoodChatBot:
    
    def init(self):
        self.currentUser = None
        self.foodItems = []

        pizzaMargarita = FoodItem("Pizza Margherita", 800, 12.99,
                False, False, True, False, False, True,
                False, False, False)
        self.foodItems.append(pizzaMargarita)

    def start(self):
        input("Press Enter to start: ")
        while True:
            print("Welcome to Jou3an, the app that helps you everyday! \n")
            print("Do you have any dietary restrictions?: ")
            dietaryRestriction = input()

            filteredItems = self.filterFoodItems(dietaryRestriction)
            if len(filteredItems) == 0:
                print("We couldn't find any " + dietaryRestriction + " food options.")
                break
            else:
                print("Here are some food options that meet your criteria:")
                for item in filteredItems:
                    print(item.getName())
                break
                    
    def filterFoodItems(self, dietaryRestriction):
        filteredItems = []

        for item in self.foodItems:
            if item.isHalal() and dietaryRestriction.lower() == "halal":
                filteredItems.append(item)
            elif item.isSeafood() and dietaryRestriction.lower() == "seafood":
                filteredItems.append(item)
            elif item.isVegan() and dietaryRestriction.lower() == "vegan":
                filteredItems.append(item)
            elif item.isKosher() and dietaryRestriction.lower() == "kosher":
                filteredItems.append(item)
            elif item.isHas_nuts() and dietaryRestriction.lower() == "no nuts":
                filteredItems.append(item)
            elif item.isVegetarian() and dietaryRestriction.lower() == "vegetarian":
                filteredItems.append(item)
            elif item.isHasLactose() and dietaryRestriction.lower() == "no lactose":
                filteredItems.append(item)
            elif dietaryRestriction.lower() == "no":
                filteredItems.append(item)
                
        return filteredItems
