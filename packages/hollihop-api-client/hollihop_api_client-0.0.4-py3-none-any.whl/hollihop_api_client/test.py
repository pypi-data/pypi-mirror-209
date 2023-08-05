import os

from pprint import pprint

from dotenv import load_dotenv
from api import HolliHopAPI

from datetime import datetime


load_dotenv()

hh_api = HolliHopAPI(
    domain=os.environ.get('HH_DOMAIN'),
    api_key=os.environ.get('HH_API_COMMON_KEY')
)

ed_units = hh_api.ed_units.get_ed_units(
    office_or_company_id=2,
    query_days=True
)

test_group = list(filter(lambda ed_unit: ed_unit.name == 'Тест Группа', ed_units))[-1]

first_day_group_lesson = test_group.schedule_items[-1].begin_date

test_student = hh_api.ed_unit_students.get_students(
    ed_unit_id=test_group.id,
    query_payers=True
)[-1]

lessons_dates = [day.date for day in test_group.days]

remaining_lessons = list(filter(lambda date: date > test_student.begin_date, lessons_dates))
if remaining_lessons and test_student.begin_date > first_day_group_lesson:
    if datetime.now() < remaining_lessons[0] and test_student.payers[-1].debt_date == remaining_lessons[0]:
        print(f"Студент {test_student.student_name} новенький и без оплаты")

pprint(remaining_lessons)

# hh_api = HolliHopAPI(
#     domain='https://euro72.t8s.ru/',
#     api_key='xRRqY3uPdxuV4w%2f1u1p6agwGAd4LurhFhKlLx3M795cCfp2iPHD6j3gFZIHVxdhm'
# )

# hh_api = HolliHopAPI(
#     domain='https://aiplus.t8s.ru/',
#     api_key='VdqvXSXu%2Fq1DWiLefLBUihGMn7MHlvSP59HIHoHH7%2BLEtHB5dtznB6sqyJIPjH5w'
# )
#
# pprint(hh_api.locations.get_locations())