# # lend-a-book-api
Flask based API
The primary objective of developing this API was twofold: to enhance my Python skills and gain practical experience with Flask framework. Additionally, the project aimed to foster a sustainable book reading community within a close-knit group. As avid readers, myself and my friends maintain individual home libraries. The API serves as a platform where we can conveniently access and browse through each other's book collections, enabling us to explore new reading options and make informed choices.

In order to run this application you can use the requiremnts.txt file using the following commad:  

```bash
  $ pip install -r requirements.txt
```

In order to create the add the following line **db.create_all()** like below and run the api.
```bash
  if __name__ == '__main__':
    db.create_all()
    app.run()
```
WORK IN PROGRESS ...

Future developments:

-add the ability to create an account

-the ability to see your own library

-the ability to check if a book is available or not

-the ability to lend a book for a defined amount of time

-the ability to return a book

-the ability to login

-the ability to have a secure user session

