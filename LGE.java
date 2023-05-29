// LowGpaException
package com.mycompany.mavenproject1;

public class LGE {
    public static void main(String[] args) {
        double assume_gpa = 2;
        try{
            if(assume_gpa < 2.5)
            throw new LowGpaException();
        }
        catch (LowGpaException e){
            System.out.println(e.getMessage());
        }
    }
}
class LowGpaException extends Exception{
    public LowGpaException() {
        super("Your GPA is not sufficient to apply for this job (2.5)");
    }
}