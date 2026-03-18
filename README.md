This program accepts a list of package weights and categorizes them into Invalid, Very Light, Normal, Heavy, and Overload using loops and conditional statements.

Based on the Personalized Load Index (PLI), the program modifies the categorized lists and generates the final loading plan.

Concepts Used

Lists

For loop

Conditional statements

Modulus operator

List operations

Day - 7:Smart Campus Energy Analyzer

Algorithm Explanation:-

In this program, I first took the number of buildings and their energy readings as input.
Then I used a loop to go through each value and classify it into efficient, moderate, high, or invalid.
I used a dictionary to store these categorized values.
After that, I used list comprehension to filter valid readings and calculate total energy consumption.
I also used a tuple to store total consumption and number of buildings.
Finally, based on conditions like high usage and total energy, I displayed the final result.

Reflection:-
One decision I made was to check total energy consumption first, because even if some buildings are efficient,
overall high usage still means energy is being wasted. I also didn’t use exact equality for balanced condition,
instead I allowed a small difference because real data is rarely perfectly equal.
