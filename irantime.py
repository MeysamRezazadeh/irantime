# https://github.com/MeysamRezazadeh/irantime

from datetime import datetime
import pytz

myMonthDic = {
 1: 'فروردین',
 2: 'اردیبهشت',
 3: 'خرداد',
 4: 'تیر',
 5: 'مرداد',
 6: 'شهریور',
 7: 'مهر',
 8: 'آبان',
 9: 'آذر',
 10: 'دی',
 11: 'بهمن',
 12: 'اسفند',
}
myDayDic = {
 'Saturday': 'شنبه',
 'Sunday': 'یکشنبه',
 'Monday': 'دوشنبه',
 'Tuesday': 'سه شنبه',
 'Wednesday': 'چهارشنبه',
 'Thursday': 'پنجشنبه',
 'Friday': 'جمعه',
}
myNumDic = {
 '1': '۱',
 '2': '۲',
 '3': '۳',
 '4': '۴',
 '5': '۵',
 '6': '۶',
 '7': '۷',
 '8': '۸',
 '9': '۹',
 '0': '۰'
}

timezone = pytz.timezone('Asia/Tehran')
now = datetime.now(timezone)

year = now.year
month = now.month
day = now.day
time = now.time()

m_to_sh = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if (month > 2):
 yearX = year + 1
else:
 yearX = year
days = 355666 + (365 * year) + ((yearX + 3) // 4) - ((yearX + 99) // 100) + ((yearX + 399) // 400) + day + m_to_sh[month - 1]
myYear = -1595 + (33 * (days // 12053))
days %= 12053
myYear += 4 * (days // 1461)
days %= 1461
if (days > 365):
 myYear += (days - 1) // 365
 days = (days - 1) % 365
if (days < 186):
 myMonth = 1 + (days // 31)
 myDay = 1 + (days % 31)
else:
 myMonth = 7 + ((days - 186) // 30)
 myDay = 1 + ((days - 186) % 30)


todayTimeNum = myYear, myMonth, myDay

# اعداد انگلیسی
yearEnglishNum = todayTimeNum[0]
monthEnglishNum = todayTimeNum[1]
dayEnglishNum = todayTimeNum[2]

# اعداد فارسی
yearFarsiNum = ''.join(list(map(lambda ch: myNumDic[ch] if ch in myNumDic else ch, str(yearEnglishNum))))
monthFarsiNum = ''.join(list(map(lambda ch: myNumDic[ch] if ch in myNumDic else ch, str(monthEnglishNum))))
dayFarsiNum = ''.join(list(map(lambda ch: myNumDic[ch] if ch in myNumDic else ch, str(dayEnglishNum))))

# نام روز و ماه ها
todayMonthName = myMonthDic[monthEnglishNum]
todayDayName = myDayDic[now.strftime('%A')]

# ساعت
hour = time.hour
minute = time.minute
second = time.second