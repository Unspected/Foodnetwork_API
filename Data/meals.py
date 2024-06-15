from enum import Enum, auto

main_course_storage = [
    {
        "id": 1,
        "mealName": "Spaghetti Carbonara",
        "mealThumb": "https://example.com/images/spaghetti_carbonara.jpg",
        "calories_100g": {"protein": 5, "fat": 3, "carbs": 25},
        "cookInstruction": "Cook spaghetti according to package instructions. In a separate pan, cook pancetta until crispy. Beat eggs and mix with grated Parmesan. Combine spaghetti with pancetta, then mix in egg and cheese mixture off the heat to avoid scrambling. Serve immediately.",
        "ingredients": [
            {"ingredient": "Spaghetti", "measurement": "200g"},
            {"ingredient": "Pancetta", "measurement": "100g"},
            {"ingredient": "Eggs", "measurement": "2"},
            {"ingredient": "Parmesan Cheese", "measurement": "50g"},
            {"ingredient": "Salt", "measurement": "to taste"},
            {"ingredient": "Black Pepper", "measurement": "to taste"}
        ]
    },
    {
        "id": 2,
        "mealName": "Chicken Alfredo",
        "mealThumb": "https://example.com/images/chicken_alfredo.jpg",
        "calories_100g": {"protein": 5, "fat": 3, "carbs": 25},
        "cookInstruction": "Cook pasta according to package instructions. In a pan, cook chicken breasts until browned and cooked through. Remove chicken and set aside. In the same pan, melt butter, add garlic and cook for 1 minute. Add cream and bring to a simmer. Stir in Parmesan until melted and sauce thickens. Toss cooked pasta with sauce and top with sliced chicken. Serve with parsley garnish.",
        "ingredients": [
            {"ingredient": "Fettuccine", "measurement": "200g"},
            {"ingredient": "Chicken Breasts", "measurement": "2"},
            {"ingredient": "Butter", "measurement": "50g"},
            {"ingredient": "Garlic", "measurement": "2 cloves"},
            {"ingredient": "Heavy Cream", "measurement": "200ml"},
            {"ingredient": "Parmesan Cheese", "measurement": "50g"},
            {"ingredient": "Parsley", "measurement": "to garnish"}
        ]
    },
    {
        "id": 3,
        "mealName": "Beef Stroganoff",
        "mealThumb": "https://example.com/images/beef_stroganoff.jpg",
        "calories_100g": {"protein": 5, "fat": 3, "carbs": 25},
        "cookInstruction": "Cook egg noodles according to package instructions. In a pan, sauté onions and mushrooms until softened. Add sliced beef and cook until browned. Stir in flour and cook for 1 minute. Add beef broth and bring to a simmer. Stir in sour cream and mustard, and cook until sauce thickens. Serve over egg noodles.",
        "ingredients": [
            {"ingredient": "Egg Noodles", "measurement": "200g"},
            {"ingredient": "Beef Strips", "measurement": "300g"},
            {"ingredient": "Onion", "measurement": "1"},
            {"ingredient": "Mushrooms", "measurement": "200g"},
            {"ingredient": "Flour", "measurement": "2 tbsp"},
            {"ingredient": "Beef Broth", "measurement": "500ml"},
            {"ingredient": "Sour Cream", "measurement": "100ml"},
            {"ingredient": "Dijon Mustard", "measurement": "1 tbsp"},
            {"ingredient": "Salt", "measurement": "to taste"},
            {"ingredient": "Black Pepper", "measurement": "to taste"}
        ]
    }
]

meal_by_category = {
    "main_course": main_course_storage
}


class MealsCategory(Enum):
    MAIN_COURSE = main_course_storage


def get_category_meals(category: str):
    if category == "main_course_storage":
        return main_course_storage