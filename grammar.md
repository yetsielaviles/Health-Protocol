# Grammar Definitions for Health-Protocol Language

**Tokens**

    Character ::= a-z | A-Z
    Operator ::= ' | , | . | - | whitespace
    Digit ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |9
    LeftParenthesis ::= (
    RightParenthesis ::= )
    Colon ::= :
    Comma ::= ,
    Assign ::= =
    
**Grammar**
    
    Exp ::= Create LeftParenthesis NAME RightParenthesis Colon 
            | Protocols Colon
            | Beds Colon
            | Beds LeftParenthesis Digit RightParenthesis Colon
            | Doctors  LeftParenthesis AVAILABLE RightParenthesis Colon
            | Doctors Colon
            | Patients Colon
            | Services Colon
            | Info LeftParenthesis ID RightParenthesis Colon
            | AddDoctor LeftParenthesis NAME Comma BIRTHDATE Comma SSN Comma AVAILABILITY Comma ID RightParenthesis Colon
            | AddPatient LeftParenthesis NAME Comma BIRTHDATE Comma SSN Comma Protocol Comma ID RightParenthesis Colon
            | Update LeftParenthesis ID Comma AVAILABILITY RightParenthesis Colon
    AVAILABILITY ::= Yes | No
    BIRTHDATE ::= {0-2 Digit | 3 0-1} / {0 1-9} | {1 0-2} / Digit Digit Digit Digit
    SSN ::= Digit Digit Digit Digit
    NAME ::= Character+ {{Operator Character}? Character* }*
    ID ::= Character {Character | Digit}* 