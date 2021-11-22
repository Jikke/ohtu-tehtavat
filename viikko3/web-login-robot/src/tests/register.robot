*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ismo
    Set Password  laitela123
    Set Password Confirmation  laitela123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 and password at least 8 characters long

Register With Valid Username And Too Short Password
    Set Username  seppo
    Set Password  seppo12
    Set Password Confirmation  seppo12
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 and password at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  seppo
    Set Password  seppo123
    Set Password Confirmation  seppo124
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation must match

Login After Successful Registration
    Set Username  roinatan
    Set Password  roinatan123
    Set Password Confirmation  roinatan123
    Submit Register Credentials
    Go To Login Page
    Set Username  roinatan
    Set Password  roinatan123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  severi
    Set Password  severi123
    Set Password Confirmation  severi321
    Submit Register Credentials
    Go To Login Page
    Set Username  severi
    Set Password  severi123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
