codes = {'489': 'Hong Kong',
         '539': 'Ireland',
         '569': 'Iceland',
         '611': 'Morocco', 
         '890': 'India'}
barcode = input("Please enter a barcode: ")
if len(barcode) != 13:
    print("That's not a valid Barcode")
else:
    country = codes[barcode[0:3]]
    manufacturer = barcode[3:8]
    check = barcode[-1]
    print("Country:", country)
    print("Manufacturer:", manufacturer)
    print("Cheack number:", check)