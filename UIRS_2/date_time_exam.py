from yargy import or_, rule
from yargy.pipelines import morph_pipeline
from yargy.predicates import eq, normalized
from yargy.interpretation import fact
from consts import *



""" 
DATE_TIME_EXAM 
"""
Date_time_exam = fact(
    'Date_time_exam',
    ['Date_exam', 'Time_exam']
)

TEXT_INFO = rule(
    normalized('дата'),
    'и',
    normalized('время'),
    normalized('осмотр'),
    eq('\n').optional()
)

DATE_EXAM = DATE.interpretation(
    Date_time_exam.Date_exam
)

TIME_EXAM = TIME.interpretation(
    Date_time_exam.Time_exam
)

DATE_TIME_EXAM = rule(
#    TEXT_INFO,
    DATE_EXAM,
    TIME_EXAM
).interpretation(
    Date_time_exam
)