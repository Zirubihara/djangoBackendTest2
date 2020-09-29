Co testować
====
Dla każdego modelu przetestuj ścieżkę tworzenia obiektu bezpośrednio przez model jak i przez uderzenie na endpoint. 

Testowanie tworzenia modeli: utwórz model, sprawdź ilość modeli w bazie; spróbuj utworzyć model z niepoprawnymi danymi i sprawdź czy otrzymasz kody błędów, których się spodziewasz.

Testowanie endpointów: utwórz w setUp usera bez uprawnień, spróbuj wykonać operacje, do których user posiada uprawnienia i potwierdź, że się wykonały (20x); wykonaj operacje, których user wykonać nie może i sprawdź czy status code się zgadza (4xx)



Task
====
This section describes which functionalities should the CRM submitted by you have:

- [x] Ability to add users from django's admin panel - PLEASE SHARE WITH US USERNAME AND PASSWORD OF THE SUPERUSER

Users have the following characteristics:
- [x] first and last name
- [x] email - it has to have @anulujkredyt.pl in it
- [x] permission level - either basic or high
- [x] password

- [x] User authentication - login as the email. Do not worry about security aspects for now. Tip: feel free to follow general guidelines for setting up basic authentication: https://docs.djangoproject.com/en/3.1/topics/auth/
4. Ability to add customers, with the following details:
    - [x] first and last name
    - [x] telephopne - no more than 9 digits and no spaces
    - [x] email - needs to have @ character in it
    - [x] first and last name cannot repeat themsleves
    - [ ] only person with high permission level can add customer - **teraz user bez uprawnień może dodać**
- [x] Ability to delete customers from the database - only person with high permission level can do that.
- [ ] Ability to edit customer details given customer's id - **żeby edytować w tym momencie musisz mieć uprawnienia a oni chcieli, żeby do usuwania były tylko potrzebne**
- [ ] Ability to add a purchase done by the customer of one of the cars: red, blue or green **Nie jestem pewien czy tu nie powinien być klucz obcy do innego modelu**
- [x] Ability to list all purchases inside a database with the following characteristics:
    - possibility to filter customers who made the purchase 
- [ ] There has to be an API documentation, separate endpoint, which describes url addresses and their parameters/queries - tip: feel free to Swagger or whatever other documentation tool
- [ ] There has to be unit test coverage and you have to report on that coverage - tip: feel free to use external packages such as django-nose