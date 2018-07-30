char* reverseString(char* s) {
        char temp ;
        const s_length = strlen(s);
        for(int i= s_length-1,j=0;i>= s_length/2;i--,j++){
            temp=s[i];
            s[i]=s[j];
            s[j]=temp;
        }

    return s;

}

