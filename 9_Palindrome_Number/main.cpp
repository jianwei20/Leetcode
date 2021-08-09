class Solution {
public:
    bool isPalindrome(int x) {
        
        string rever = to_string(x);
        reverse(rever.begin(), rever.end());
        if(to_string(x) == rever){
            return true;
        }
        else{
            return false;
        }
        
    }
};