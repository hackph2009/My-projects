books = []
wish_list = []

# إضافة كتب إلى المكتبة
while True:
    book = input("Enter a book you have read (or press Enter to finish): \n")
    if book.strip():
        books.append(book.strip())
        print(f"Your library now: {books}")
    else:
        break
if not books:
    print("Please enter at least one book.")
    exit()

# إضافة كتب إلى قائمة الأمنيات
while True:
    wish = input("Enter a book you wish to have in the future (or press Enter to finish): \n")
    if wish.strip():
        wish_list.append(wish.strip())
        print(f"Your wish list now: {wish_list}")
    else:
        break

# نقل كتاب من قائمة الأمنيات إلى المكتبة
if wish_list:
    got_book = input("Did you get a book from your wish list? (type the name or press Enter to skip): \n")
    if got_book.strip() in wish_list:
        wish_list.remove(got_book.strip())
        books.append(got_book.strip())
        print(f"You got the book!\nYour library: {books}\nYour wish list: {wish_list}")
    elif got_book.strip():
        print(f"This book is not in your wish list.\nYour wish list: {wish_list}")

# التبرع بكتاب
if books:
    donation = input("Do you want to donate a book from your library? (type the name or press Enter to skip): \n")
    if donation.strip() in books:
        books.remove(donation.strip())
        print(f"You donated the book!\nYour final library: {books}")
    elif donation.strip():
        print(f"This book is not in your library.\nYour library: {books}")
    else:
        print(f"Your final library: {books}")
else:
    print("Your library is empty.")