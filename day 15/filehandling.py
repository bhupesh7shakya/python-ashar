try:
    f=open("filensame.txt")

    # f.write("\nk cha")
    print(f.readlines())
    f.close()
    
except FileNotFoundError:
    print("FIle could not be found")

except:
    print('Something went wrong')

# import os

# os.remove("filensame.txt")