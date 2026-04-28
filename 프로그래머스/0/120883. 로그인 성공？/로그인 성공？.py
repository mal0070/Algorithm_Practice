def solution(id_pw, db):
    #id와 pw가 모두 일치하면 login
    #id 없음 -> fail
    #id만 일치 -> wrong pw
    if id_pw in db:
        return "login"

    for x in db:
        if id_pw[0] == x[0] and id_pw[1]!=x[1]:
            return "wrong pw"
        
    return "fail"