This is a demo UML.
For this we used django to simulate the server, using MVC and SQL application
for this demo I used sqlite.
for demo proposites I develop 15 endpoints

method get route =/client/view gives all clients from database
method post route =/client/view insert a client on database
method get route =/client/detail/<int:client_id> get client from database
method put route =/client/detail/<int:client_id> update client from database
method delete route =/client/detail/<int:client_id> delete client from database

method get route =/account/view gives all accounts from database
method post route =/account/view insert a account on database
method get route =/account/detail/<int:account_id> get account from database
method put route =/account/detail/<int:account_id> update account from database
method delete route =/account/detail/<int:account_id> delete account from database

method get route =/account/transaction/view gives all transactions from database
method post route =/account/transaction/view insert a transaction on database
method get route =/account/transaction/detail/<int:transaction_id> get transaction from database
method put route =/account/transaction/detail/<int:transaction_id> update transaction from database
method delete route =/account/transaction/detail/<int:transaction_id> delete transaction from database

superuser information:
superuser: agustin
password: admin