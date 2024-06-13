year = int(input("Enter the number :"))
if (year % 4 == 0) and (year % 400 == 0) and (year != 100):
    print(f"{year} is an leap year",year)
else:
    print(f"{year} is not leap year",year)
