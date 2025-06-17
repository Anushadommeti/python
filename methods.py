skills=["python-eAsy","java-difficult","js-easY","react-Easy","html-EASY","git-moderate"]
for x in skills:
    if x.lower().find("easy")!=-1:
        print(x)

skills=["python-eAsy   ",
        "java-difficult",
        "   easy-js",
        "react-Easy   ",
        "     EASY-html",
        "git-moderate"]
for y in skills:
    if y.lower().find("easy")!=-1:
        op=y.strip()
        print(op)
        