# Calcrypt
An encryption method

Welcome to Calcrypt. Calcrypt encrypts and decrypts using the calendar.

# Info
  1.0 calcrypt and calcryptWinfo Classes
  
      calcrypt Class is the main code, calcryptWinfo is the same class, with print lines for getting info. 
      
    1.1 __init__()
    
      Not much happens in the __init__ function. Just sets 2 variables to false which make classes reusable
      
    1.2 createTxt()
    
      This function create a txt file. This file can be used for output of encrypt() function. Takes 3  potential arguments 
      which are 'path', 'sameLine' and 'lineBreak'. 'sameLine' argument decides whether the output will be single or multiple lines.
      Default is 'False'. 'lineBreak' argument sets the line length. Default is 238.
      
    1.3 encrypt()
    
      It is the function where the main event happen. Takes 1 neccesary and 2 potential arguments which are 'text', 'txt' and 'returnList'.
      'text' argument is the text will be encrypted. 'txt' argument is the bool variable, decides where the output will be. Default is 'False'.
      When 'returnList' argument is 'True' function will be returns a listt, otherwise returns a string. Default is 'False' and can not be 'True'
      while 'txt' is 'True'. This function returns encrypted text.
      
    1.4 getKey()
    
      Returns the key of last encrypted text. Keys seperate encrypted letter each other for decrypt. Decrypt function can not work without 'key'.
      
    1.5 decryptString()
    
      Decrypts the encrypted text. Takes 2 neccesary arguments which are 'text' and 'key'. Returns decrypted text.
      
    1.6 decryptTxt()
    
      Decrypts the encrypted txt file. Takes 2 neccesary arguments which are 'path' and 'key'. Returns decrypted text.
  
  
  2.0 Alphabets
  
    These are lists of encrypted and normal letters.
    
    2.1 alphabet
    
      This is the list of normal letters. 
      
    2.2 encrypted_alphabet
    
      This is the list of encrypted letters. Encrpyted letters are matrices. Every letter have a different matrix. For example letter a's matrix is,
      [[0, 1, 1, 0,], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1]]. These matrices are often similar in appearance to their letters on the paper. There is 
      no specific umber of columns and rows, but matrices with more than 4 rows or more than 5 columns can cause problems
      
    2.3 Editing Alphabets
    
      You can edit these alpahates according to yourself. Add or edit existing letters but make sure the encrypted and regular letters belong to the same
      index in their respective lists.
      
      
This is my first individual project and I want to turn it into a library. I would like to thank you in advance if you point out any mistakes of me or something
you would like to suggest.

And sorry for bad grammar, I used google translate and I noticed the words are not correct words but couldn't find better.
