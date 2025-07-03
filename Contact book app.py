# Contact Book App #


contacts = {}


while True:
    print("\n Contact book app")
    print("1.Create contact")
    print("2.View contact")
    print("3.Update contact")
    print("4.Delete contact")
    print("5.Search contact")
    print("6.Count contact")
    print("7.Exit")
    
    choice = input("Enter your choice:  ")
    
    
    if choice == '1':
        name = input("Enter your name:  ")
        if name in contacts :
            print(f"Contact name {name} already exists!")
            
        else :
            age = input("Enter age:  ")
            email = input("Enter email:  ")
            mobile = input("Enter mobile number:  ")
            
            contacts[name] = {'age' : int(age),'email': email,'mobile': int(mobile)}
            
            print(f"Contact name {name} has been created successfully!")
            
            
            
    elif choice == '2':
        name = input("Enter your name to view: ")
        if name in contacts :
            contact = contacts[name]
            print(f'Name : {name} , Age : {age}, email : {email} , Mobile Number : {mobile}')
            
        else :
            print("Contact not found !")
            
    elif choice == '3':
            name = input("Enter name to update contact :  ")
            if name in contacts :
                age = input("Enter updated age:  ")
                email = input ("Enter updated email:  ")
                mobile = input("Enter updated mobile number:  ")
                contacts[name] = {'age' : int(age),'email': email,'mobile': int(mobile)}
                print("Contact updated successfully!")
                
            else :
                 print("Contact not found !")
                 
    elif choice == '4' :
        name = input("Enter contact name to delete :  ")
        if name in contacts :
            del contacts [name]
            print(f'contact name {name} had been deleted successfully !')
            
        else :
              print ("Contact not found!")
              
              
    elif choice == '5' :
         search_name = input ("Enter contact name to seaech:  ")
         found = False
         for name, contact in contacts.items():
              if search_name.lower() in name.lower():
                 print(f'Found = Name: {name}  ,age: {age} , email: {email} , Mobile Number: {mobile}')
                 found = True
               
         if not found:
                   print("no contact found with that name")
                   
    elif choice == '6':
        print(f"Total contacts in your book : {len(contacts)}")
        
    elif choice == '7':
         print('Good bye...Closing the program')
         break
         
    else :
         print("Invalid input ")