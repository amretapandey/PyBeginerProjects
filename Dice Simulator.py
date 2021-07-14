import random  

print("press y to roll:")
while input() == "y": 
     
    no = random.randint(1,6)    # Gnenerates a random number between 1 and 6
      
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  *  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ *   ]") 
        print("[     ]") 
        print("[   * ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[*    ]") 
        print("[  *  ]") 
        print("[    *]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[*   *]") 
        print("[     ]") 
        print("[*   *]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[*   *]") 
        print("[  *  ]") 
        print("[*   *]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[*   *]")
        print("[*   *]")
        print("[*   *]") 
        print("[-----]") 
        
    print("\npress y to roll:")
