import hashlib

def crack_pass(inputPass, type):
    iteration = 0
    try:
        wordlist = input("Enter wordlist path/name.ext: ")
        wordlist_obj = open(wordlist, "r")
        # clean up e handles
    except UnboundLocalError:
        print("Couldn't find the file specified, did you provide the extension?")
    except FileNotFoundError:
        print("Couldn't find the file specified, did you provide the path if not in current directory?")
    type = type.lower()
    if type == "md5":
        iteration +=1
        for password in wordlist_obj:
            encoded_pass = password.encode("utf-8")
            digest = hashlib.md5(encoded_pass.strip()).hexdigest()
            if digest == inputPass:
                print(f"Completed in {iteration} iterations")
                print("Password found: " + password)
                exit()

    elif type == "sha256":
        for password in wordlist_obj:
            iteration +=1
            encoded_pass = password.encode("utf-8")
            digest = hashlib.sha256(encoded_pass.strip()).hexdigest()
            if digest == inputPass:
                print(f"Completed in {iteration} iterations")
                print("Password found: " + password)
                exit()              
    elif type == "sha512":
          
        for password in wordlist_obj:
            iteration +=1
            encoded_pass = password.encode("utf-8")
            digest = hashlib.sha512(encoded_pass.strip()).hexdigest()
            if digest == inputPass:
                print(f"Completed in {iteration} iterations")
                print("Password found: " + password)
                exit()
    else:
        print("No values found in the wordlist match the hash. (Add handling for bad algo)")

inputPass = input("Enter the hash to crack:")
type = input("Enter the hash type for example, md5, sha256: ")
crack_pass(inputPass, type) 
