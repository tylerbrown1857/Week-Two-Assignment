__author__ = 'Tyler Brown'
def main():
    x = 1
    while x != 0:
        k = eval(input("Enter a Distance in kilometers:"))
        m = k*.62
        print(k, " kilometers is equal to ", m, " miles.")
        
        
main()