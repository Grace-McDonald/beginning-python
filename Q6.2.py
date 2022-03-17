codes = {'489': 'Hong Kong',
         '539': 'Ireland',
         '569': 'Iceland',
         '611': 'Morocco', 
         '890': 'India'}
barcode = input("Please enter a barcode: ")
if len(barcode) != 13:
    print("That's not a valid Barcode")
else:
    country = barcode[0:2]
    print(country)