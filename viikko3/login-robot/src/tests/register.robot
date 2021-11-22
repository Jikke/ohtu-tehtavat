*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  seppo  seppo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle1234
    Output Should Contain  User with username kalle already exists


Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 and password at least 8 characters long

Register With Valid Username And Too Short Password
    Input Credentials  seppo  seppo12
    Output Should Contain  Username must be at least 3 and password at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  seppo  salasanani
    Output Should Contain  Password must contain other than alphabet characters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command