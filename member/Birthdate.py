from datetime import date

class Age():
    birth_date=[]
    count_age = 0
    
    def under_age(self,birth_date=[]):
        below_18=[]
        for dates in birth_date:
            today = date.today()
            age = today.year - dates.year-((today.month, today.day)<(dates.month, dates.day))
            if age < 18:
                below_18.append(age)
            else:
                pass
        count_age = len(below_18)
        return count_age

    def over_age(self,birth_date=[]):
        over_18=[]
        for dates in birth_date:
            today = date.today()
            age = today.year - dates.year-((today.month, today.day)<(dates.month, dates.day))
            if age < 18:
                pass
            else:
                over_18.append(age)
        count_age = len(over_18)
        return count_age

age = Age()
print(age.under_age([date(2010,2,16)]))