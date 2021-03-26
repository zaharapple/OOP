import traceback
from datetime import datetime
from models import Employee, Recruiter, Programmer, Candidate, Vacancy


def main():
    try:
        r = Recruiter(name="Sasha", zp_day=150, days=21, email='sasha@com')
        p = Programmer(name="Slava", zp_day=220, days=23, email='sl@com',
                       tech_stack={'have a car ', 'Python', 'JS', 'Git', 'HTML'})
        p2 = Programmer(name="Kostya", zp_day=200, days=24, email='kos@com',
                        tech_stack={'know of English ', 'Python', 'Django', 'flaks', 'react'})
        c = Candidate("Petya", "pet@com", "Razrabotka", "JS", "trenie")
        c2 = Candidate("Katya", "KET@com", "Recruter", "English", "С1")
        c3 = Candidate("Kiril", "Kir@com", "Razrabotkbotka", "Python", "junior")
        v = Vacancy("Programmer", "Python,JS,HTML", "junior")
        v2 = Vacancy("Recruiter", "комуникабельность , знание английского языка", "стаж 1год")

        # print(v)
        # print(v2)
        #
        # print('---------------------------')
        #
        # print(c)
        # # print(c.work())
        # print(c2)
        # print(c3)
        #
        # print('---------------------------')
        #
        # print(r)
        # print(r.work())
        # print(r.cheak_salary())
        #
        # print('---------------------------')
        #
        # print(p)
        # print(p.work())
        # print(p.cheak_salary())
        # print(p.tech_stack)
        #
        # print('---------------------------')
        # print(r == p)  # comparison by salary
        # print('---------------------------')
        # print(p.cheak_salary())
        #
        # print(p2)
        # print(p2.work())
        # print(p2.cheak_salary())
        # print(p2.tech_stack)
        #
        # print('---------------------------')
        # print(p > p2)
        # print()
        #
        # alfaprogr = p + p2
        # print(alfaprogr)
        # print(alfaprogr.work())
        # print(alfaprogr.cheak_salary())
        # print(alfaprogr.tech_stack)
        print(p.full_info)
        Candidate.create_candidat(' candidates.csv')


    except Exception as e:

        with open('logs.txt', 'a+') as log:
            mytime = (datetime.now().ctime())
            log.write(mytime + '\n')
            log.write(traceback.format_exc() + '------------------' + '\n')


if __name__ == '__main__':
    main()
