# Secure-Password-Generator
  This program uses the modules- string and secrets.
   secrets module to generate sequences of random characters that are secure
  for cryptographic applications
   string module to create string of possible characters to be used

  1. First, a string is created using strings module that contains uppercase and
  lowercase letter, digits, and special characters.

  2. Required password length is taken as input from user.
     
	3. If user chooses ‘no constraints’:
		3.1. Using secrets module, random characters are generated from alphabet and
		stored in a string pwd till pwd is of required length.
		3.2. Password pwd is printed.
	
	4. If user chooses ‘yes constraints’:
		4.1. Required constraints are taken as input from the user.
		4.2. Using secrets module, random characters are generated from alphabet and
		stored in a string pwd till pwd is of required length.
		4.3. Password pwd is checked if it matches given constraints.
			4.3.1. If it matches constraints, the password is printed.
			4.3.2. If it doesn’t match the constraints, a new password pwd is generated
			till it matches the given constraints
