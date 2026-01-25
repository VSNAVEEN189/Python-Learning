# user = {
# "User name": "ey User",
# "password": "test@123",
# "email": "my_user@example.com",
# "address": "ABC road, 111111",
# "country": "Australia"
# }

# Delete the sensitive information from the dictionary present in a list
# sensitive info ["password", "address"] '''


user = {
"User name": "my User",
"password": "test@123",
"email": "my_user@example.com",
"address": "ABC road, 111111",
"country": "Australia"
}
sensitive_info = ["password", "address"]

for i in sensitive_info:
    print(f"Key: {i}, Value: {user[i]}")
    user.pop(i)

print(user)    
