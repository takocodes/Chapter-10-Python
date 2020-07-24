# Programmer: Christine Doan
# Prompt: Add/subtract times, convert inputted AM/PM to military, ask for military time.

# Convert AM/PM to military
# def fromamPM(s):
#     if s[-2:] == 'AM' and s[:2] == '12':
#         return '00' + s[2:-2]

#     elif s[-2:] == 'AM':
#         return s[:-2]

#     elif s[-2:] == 'PM' and s[:2] == '12':
#         return s[:-2]

#     else:
#         return str(int(s[:2]) + 12) + s[2:8]

class Clock:
    def __init__(self, hour, minute):
        self.hour = (abs(hour % 24))
        self.minute = (abs(minute % 60))

    def __str__(self):
        if self.hour < 10:
            self.hour = str(self.hour).zfill(2)
        if self.minute < 10:
            self.minute = str(self.minute).zfill(2)

        converted = str(self.hour) + str(self.minute)
        return converted

    def totalMinutes(self):
        return int(self.hour) * 60 + int(self.minute)
    
    def add(self, other):
        y = self.minute + other.minute
        x = self.hour + other.hour
        return Clock(x, y)
    
    def subtract(self, other):
        x = self.hour - other.hour
        y = self.minute - other.minute
        return Clock (x, y)

def main():
    h1 = int(input('First Hour - Enter a number for hour: '))
    min1 = int(input('First Minutes - Enter a number for minutes: '))

    h2 = int(input('Second Hour - Enter a number for hour: '))
    min2 = int(input('Second Minutes - Enter a number for minutes: '))

    t1 = Clock(h1, min1)
    t2 = Clock(h2, min2)

    t3added = t1.add(t2)
    t3subtr = t1.subtract(t2)


    print('Your first time in military is', t1)
    print('Your second time in military is', t2)
    print('The addition for both times are', t3added)
    print('The subtraction for both times are', t3subtr)
    print('The total minutes past midnight for time 1 is',t1.totalMinutes(), 'minutes.')
    print('The total minutes past midnight for time 2 is', t2.totalMinutes(), 'minutes.')

main()


