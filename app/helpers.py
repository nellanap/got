from flask import redirect, render_template, request, session
from functools import wraps

# Global variable for correct answers
ans1 = 'Yes'
ans2 = 'Yes'
ans3 = 'Yes'
ans4 = 'Yes'
ans5 = 'Yes'
ans6 = 'Yes'
ans7 = 'Yes'
ans8 = 'Yes'
ans9 = 'Yes'
ans10 = 'Yes'
ans11 = 'Yes'
ans12 = 'Yes'
ans13 = 'Yes'
ans14 = 'Yes'
ans15 = 'Yes'
ans16 = 'Daenerys'
ans17 = 'Daenerys'
ans18 = 'Jamie'
ans19 = 'Jamie'
ans20 = 'Yes'
ans21 = 'Tyrion'
ans22 = 'Jon'
ans23 = 'Yes'
ans24 = 'Hound'
ans25 = 'Yes'
ans26 = 'Yes'
ans27 = 'Yes'
ans28 = 'Yes'
ans29 = 'Yes'
ans30 = 'Yes'

# Global variables for correct weights
wgt1 = 5
wgt2 = 5
wgt3 = 3
wgt4 = 3
wgt5 = 2
wgt6 = 2
wgt7 = 2
wgt8 = 2
wgt9 = 2
wgt10 = 2
wgt11 = 2
wgt12 = 2
wgt13 = 1
wgt14 = 1
wgt15 = 1
wgt16 = 3
wgt17 = 5
wgt18 = 3
wgt19 = 2
wgt20 = 2
wgt21 = 2
wgt22 = 1
wgt23 = 1
wgt24 = 1
wgt25 = 2
wgt26 = 3
wgt27 = 2
wgt28 = 1
wgt29 = 2
wgt30 = 5


def calculate_points(response):
    points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if response.q1 == ans1:
        points.insert(0, wgt1)
    if response.q2 == ans2:
        points.insert(1, wgt2)
    if response.q3 == ans3:
        points.insert(2, wgt3)
    if response.q4 == ans4:
        points.insert(3, wgt4)
    if response.q5 == ans5:
        points.insert(4, wgt5)
    if response.q6 == ans6:
        points.insert(5, wgt6)
    if response.q7 == ans7:
        points.insert(6, wgt7)
    if response.q8 == ans8:
        points.insert(7, wgt8)
    if response.q9 == ans9:
        points.insert(8, wgt9)
    if response.q10 == ans10:
        points.insert(9, wgt10)
    if response.q11 == ans11:
        points.insert(10, wgt11)
    if response.q12 == ans12:
        points.insert(11, wgt12)
    if response.q13 == ans13:
        points.insert(12, wgt13)
    if response.q14 == ans14:
        points.insert(13, wgt14)
    if response.q15 == ans15:
        points.insert(14, wgt15)
    if response.q16 == ans16:
        points.insert(15, wgt16)
    if response.q17 == ans17:
        points.insert(16, wgt17)
    if response.q18 == ans18:
        points.insert(17, wgt18)
    if response.q19 == ans19:
        points.insert(18, wgt19)
    if response.q20 == ans20:
        points.insert(19, wgt20)
    if response.q21 == ans21:
        points.insert(20, wgt21)
    if response.q22 == ans22:
        points.insert(21, wgt22)
    if response.q23 == ans23:
        points.insert(22, wgt23)
    if response.q24 == ans24:
        points.insert(23, wgt24)
    if response.q25 == ans25:
        points.insert(24, wgt25)
    if response.q26 == ans26:
        points.insert(25, wgt26)
    if response.q27 == ans27:
        points.insert(26, wgt27)
    if response.q28 == ans28:
        points.insert(27, wgt28)
    if response.q29 == ans29:
        points.insert(28, wgt29)
    if response.q30 == ans30:
        points.insert(29, wgt30)
    return points



def calculate_score(response):
    score = 0
    if response.q1 == 'Yes':
        score = score + 5
    if response.q2 == 'Yes':
        score = score + 5
    if response.q3 == 'Yes':
        score = score + 3
    if response.q4 == 'Yes':
        score = score + 3
    if response.q5 == 'Yes':
        score = score + 2
    if response.q6 == 'Yes':
        score = score + 2
    if response.q7 == 'Yes':
        score = score + 2
    if response.q8 == 'Yes':
        score = score + 2
    if response.q9 == 'Yes':
        score = score + 2
    if response.q10 == 'Yes':
        score = score + 2
    if response.q11 == 'Yes':
        score = score + 2
    if response.q12 == 'Yes':
        score = score + 2
    if response.q13 == 'Yes':
        score = score + 1
    if response.q14 == 'Yes':
        score = score + 1
    if response.q15 == 'Yes':
        score = score + 1
    if response.q16 == 'Daenerys':
        score = score + 3
    if response.q17 == 'Daenerys':
        score = score + 5
    if response.q18 == 'Jamie':
        score = score + 3
    if response.q19 == 'Jamie':
        score = score + 2
    if response.q20 == 'Yes':
        score = score + 2
    if response.q21 == 'Tyrion':
        score = score + 2
    if response.q22 == 'Jon':
        score = score + 1
    if response.q23 == 'Yes':
        score = score + 1
    if response.q24 == 'Hound':
        score = score + 1
    if response.q25 == 'Yes':
        score = score + 2
    if response.q26 == 'Yes':
        score = score + 3
    if response.q27 == 'Yes':
        score = score + 2
    if response.q28 == 'Yes':
        score = score + 1
    if response.q29 == 'Yes':
        score = score + 2
    if response.q30 == 'Yes':
        score = score + 5
    return score

def calculate_rank(score):
    if (score >= 0) and (score < 20):
        return 'Stonemen'
    if (score >= 20) and (score < 30):
        return 'Unsullied'
    if (score >= 30) and (score < 40):
        return 'Brotherhood'
    if (score >= 40) and (score < 50):
        return 'Iron Banker of Braavos'
    if (score >= 50) and (score < 60):
        return 'Nights Watch'
    if (score >= 60) and (score < 65):
        return 'Maester'
    if score == 65:
        return 'Warg'
    if score == 67:
        return 'Greenseer'
    if score == 68:
        return 'One-Eyed Raven'
    if score == 69:
        return 'Two-Eyed Raven'
    if score == 70:
        return 'Three-Eyed Raven'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
