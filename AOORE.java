// ageoutofrangeexception
package com.mycompany.mavenproject1;
import java.util.*;
public class AOORE {
    public static void main(String[] args) {
        int assume_age = 40;
        try{
            if(assume_age > 25)
                throw new AgeOutOfRangeException(assume_age);
            else
                System.out.println("Age is in range");
        }
        catch (AgeOutOfRangeException e){
            System.out.println(e.getMessage());
        }
    }
}
class AgeOutOfRangeException extends Exception{
    int a;
    AgeOutOfRangeException(int age){
        a = age;
    }
    @Override
    public String getMessage() {
        return "You are older than the requested age (25 years), you are " + a + "!!!";
    }
}
