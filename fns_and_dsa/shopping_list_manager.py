

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            items = input("Enter items to be added: ").split()
            shopping_list += items
            
        elif choice == '2':
            remove_items = input("Enter item(s) to be removed: ").split()
            for item in remove_items:
                if item in remove_items:
                    shopping_list.remove(item)
            
        elif choice == '3':
            for item in shopping_list:
                print(item, end=" ")
            print()
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()