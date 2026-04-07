class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
            for(int i =0; i<db.length; i++){
                if(id_pw[0].equals(db[i][0]) && id_pw[1].equals(db[i][1])){ //배열은 참조값! 따라서 값을 비교하고 싶으면 각 요소를 비교해야함
                    return "login";
                }
                else if(id_pw[0].equals(db[i][0])&& id_pw[1].equals(db[i][1]) == false){
                    answer = "wrong pw";
                }
            }
        return answer;
    }
}