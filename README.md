# CSC120-A2: Object-ification

This repository contains starter code for A2: Object-ification, developed for CSC120: Object-Oriented Programming as taught by Prof. R. Jordan Crouser at Smith College in Fall 2022.
  
 `procedural_resale_shop.py` contains a procedural program to perform the basic functions of a computer resale store:
   - buying a computer (add to inventory)
   - selling a computer (remove from inventory)
   - updating the price of an item in the inventory
   - printing the inventory
   - refurbishing a computer (update price based on age of machine, optionally update OS)
   
  `main.py` contains a simple demonstration of each of these functions, plus a helper function to create a "computer"
  
  ## Your task
  
  **Step 1**: Fork this repository so you (and your partners, if applicable) have your own copy of this code.
  
  **Step 2**: Fill in the class definitions in `computer.py` and `oo_resale_shop.py` with the appropriate functionality from the provided procedural code, re-written using Object-Oriented Programming techniques. Consider carefully which classes should be responsible for which behaviors / information:
  - storing information about a specific computer *computer.py
  - storing the inventory for the store *oo_resale_shop.py
  - updating a computer's price *oo_resale_shop.py
  - updating a computer's OS *oo_resale_shop.py
  - buying a computer (add to inventory) *oo_resale_shop.py
  - selling a computer (remove from inventory) *oo_resale_shop.py
  - refurbishing a computer *oo_resale_shop.py

 **Step 3**: Be sure to test your code! The items contained in `rubric.md` are a useful guide.
 
**Step 4**: Fill in `rubric.md` wth your self-assessment and include your reflection on the assignment in `reflection.md`, then submit your repo to Gradescope.
