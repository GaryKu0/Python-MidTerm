TwelveYears=['rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig']
year=int(input('year:'))
year=abs(year-4,)
if year>=12:
    gap=year%12
else:
    gap=year
print(TwelveYears[gap])