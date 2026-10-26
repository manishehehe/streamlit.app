from streamlit.testing.v1 import AppTest
import json, os
if os.path.exists("leaderboard.csv"): os.remove("leaderboard.csv")
BANK={q["id"]:q for q in json.load(open("question_bank.json"))}
def play(level, n, answer_right=True, timed=False):
    at=AppTest.from_file("app.py", default_timeout=30).run()
    at.text_input[0].input("Tester")
    at.radio(key=None) if False else None
    # setup form widgets: radio[1] is difficulty (radio[0] is sidebar)
    [x for x in at.radio if x.label=="Difficulty"][0].set_value(level)
    at.toggle[0].set_value(timed)
    at.select_slider[0].set_value(n)
    [b for b in at.button if "Start" in b.label][0].click().run()
    assert not at.exception, at.exception
    for i in range(n):
        s=at.session_state
        q=BY=BANK[s.order[s.idx]]
        if q["pairs"]:
            for left,right in q["pairs"].items():
                sb=[x for x in at.selectbox if x.label==left][0]
                sb.set_value(right if answer_right else "— select —" )
            if not answer_right:
                # pick a wrong mapping
                vals=list(q["pairs"].values())
                for j,left in enumerate(q["pairs"]):
                    [x for x in at.selectbox if x.label==left][0].set_value(vals[(j+1)%len(vals)])
        elif q["accept"]:
            at.text_input[0].input(q["accept"][0].upper()+"  " if answer_right else "zzz")
        else:
            r=[x for x in at.radio if x.label=="Choose one"][0]
            r.set_value(q["answer"] if answer_right else [o for o in r.options if o!=q["answer"]][0])
        sub=[b for b in at.button if b.label=="Submit answer"][0]
        sub.click().run()
        assert not at.exception, at.exception
        assert at.session_state.last["correct"]==answer_right,(q["id"],at.session_state.last)
        nb=[b for b in at.button if b.label in("Next question ▶","🏁 See results")][0]
        nb.click().run()
        assert not at.exception, at.exception
    assert at.session_state.stage=="result"
    return at
at=play("Mixed",10,True); print("mixed all-correct score",at.session_state.score)
at=play("Adaptive",10,False); print("adaptive wrong, levels:",[BANK[i]["difficulty"] for i in at.session_state.order])
at=play("Adaptive",10,True); print("adaptive right, levels:",[BANK[i]["difficulty"] for i in at.session_state.order])
at=play("Mixed",len(BANK),True); print("full bank ok, score",at.session_state.score)
print(open("leaderboard.csv").read())
