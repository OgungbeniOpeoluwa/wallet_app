# **wallet_app**
## **Table Of Content**
* [Introduction](#Introduction)
* [ SetUp](#Setup)
* [ End-points](#END-POINTS)
* [Features](#Features)

### Setup
1. Ensure Python 3.x install on your system
2. Create an account with git.
3. From your terminal/command prompt clone the repository using this git command
   * git clone <https://github.com/OgungbeniOpeoluwa/wallet_app.git>.
4. install postman to test the application end-points by providing the necessary url and body requests if necessary.



### Introduction
fastWallet is a user-friendly e-wallet application designed to 
simplify financial management. This application is build on django rest
framework and paystack. 

#### Features
* [Register](#Register Request)
* [Login](#Login Request)
* [Fund Wallet](#Fund Walllet Request)
* [Transfer](#Transfer Request)
* [Balance](#Get Balance Request)
* [Transaction](#Get All Transaction Request)

### **_END-POINTS_**

#### **Register Request**
_This api create a new user.it takes username,email,phone number and the password.
The phone number,email and password(min=8,max=16) must be valid to avoid invalid details.__

#### **Request**
* _url :_ http://localhost/9090/user/register
* _Method_ : POST
* Header:
       
    content-type: application/json
* Body:

    ```
  {
    'username':"username",
    'email':"user@gmail.com
    "password":"password"
    }
  ```
  
##### _Fields_
1. username: The user preferred nick_name 
2. email: The user valid email
3. password: The user password

#### _Response 1_
##### _Successful Response_
* _status : OK 200_

* _body:_
    
  ```
  {
    "email":user@gmail.com,
    "username":"username
    }
  ```
##### **_UnSuccessful Response_**
