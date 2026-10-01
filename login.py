def login(username, password):
    if username == "admin" and password == "admin@123":
        return "Login successful\n Redirect to Login Page"
    return "Invalid username or password"

print(login("admin", "1234"))