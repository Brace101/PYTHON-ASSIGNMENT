print("""
        PHONE-BOOK 
        1. Search
        2. Service Nos.
        3. Add name 
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b'card
        8. Options
        9. Speed dials
        10. Voice tags
    """)
        option = int(input("Enter option: "))

    if option == 8:
        print("""
        OPTIONS
        1. Type of view
        2. Memory Status
        """)
        sub = int(input("Enter option: "))
        if sub == 1:
            print("Type of view")
        elif sub == 2:
            print("Memory Status")
        else:
            print("Enter valid number")
    else:
        print("Selected:", option)


messages_menu():
    print("""
        MESSAGES
        1. Write Message
        2. Inbox
        3. Outbox
        4. Picture Messages
        5. Template
        6. Smileys
        7. Message settings
        8. Info Service
        9. Voice mailbox number
        10. Service command editor
    """)
    option = int(input("Enter option: "))

    if option == 7:
        print("""
            MESSAGE SETTINGS
            1. Set 1
            2. Common
        """)
        sub = int(input("Enter option: "))

        if sub == 1:
            print("""
                MESSAGE SETTINGS 
                1. Message centre number
                2. Message send as
                3. Message validity
            """)
            sub2 = int(input("Enter option: "))
            actions = {
                1: "Message centre number",
                2: "Message send as",
                3: "Message validity"
            }
            print(actions.get(sub2, "Enter valid number"))

        elif sub == 2:
            print("""
                MESSAGE SETTINGS 
                1. Delivery
                2. Reply via same centre
                3. Character support
            """)
            sub2 = int(input("Enter option: "))
            actions = {
                1: "Delivery",
                2: "Reply via same centre",
                3: "Character support"
            }
            print(actions.get(sub2, "Enter valid number"))

        else:
            print("Enter valid number")

    else:
        print("Selected:", option)


call_register_menu():
    print("""
        CALL REGISTER 
        1. Missed Calls
        2. Received
        3. Dialled Numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. Call cost settings
        8. Prepaid credit
    """)
    option = int(input("Enter option: "))

    if option == 5:
        print("""
            SHOW ALL CALL DURATION 
            1. Last call duration
            2. All calls duration 
            3. Received calls duration
            4. Dialled calls duration
            5. Clear timers
        """)
        sub = int(input("Enter option: "))
        print("Selected:", sub)

    elif option == 6:
        print("""
            SHOW CALL COST
            1. Last call cost
            2. All calls cost 
            3. Clear counters
        """)
        sub = int(input("Enter option: "))
        print("Selected:", sub)

    elif option == 7:
        print("""
            CALL COST SETTINGS
            1. Call cost limit
            2. Show costs in
        """)
        sub = int(input("Enter option: "))
        print("Selected:", sub)

    else:
        print("Selected:", option)


