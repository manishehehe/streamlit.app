from streamlit.testing.v1 import AppTest
import json
BANK={q["id"]:q for q in json.load(open("question_bank.json"))}
at=AppTest.from_file("app.py", default_timeout=30).run()
[b for b in at.button if "Start" in b.label][0].click().run()
def cur(): return BANK[at.session_state.order[at.session_state.idx]]
# make current question a 4-option MCQ deterministically
at.session_state.order[0]="Q01"; at.session_state.shown_options=list(BANK["Q01"]["options"])
at.run()
[b for b in at.button if "Hint" in b.label][0].click().run()
print("used_hint",at.session_state.used_hint, [i.value for i in at.info])
[b for b in at.button if "50:50" in b.label][0].click().run()
q=cur(); r=[x for x in at.radio if x.label=="Choose one"][0]
print(q["id"],"options after 50:50",r.options, q["answer"] in r.options)
r.set_value(q["answer"]); [b for b in at.button if b.label=="Submit answer"][0].click().run()
print(at.session_state.last)
[b for b in at.button if b.label=="Next question ▶"][0].click().run()
at.session_state.q_start -= 500
at.run(); print("timeout:",at.session_state.last, [e.value for e in at.error])
print("exceptions:",at.exception)
