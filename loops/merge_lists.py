legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

rawdb = [legacy_customers, new_customers]

print(rawdb)


for legacy_customer in legacy_customers:
        new_customers.append(legacy_customer)

print(new_customers)