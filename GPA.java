
package com.mycompany.mavenproject1;

public class GPA {
    public static void main(String[] args) {
        int age = 25;
        double gpa = 2.0;

        try {
            if (age > 25) {
                throw new AgeOutOfRangeException(age);
            }

            if (gpa < 2.5) {
                throw new LowGpaException(gpa);
            }

            System.out.println("Your application is accepted and is under study.");
        } catch (AgeOutOfRangeException e) {
            System.out.println(e.getMessage());
        } catch (LowGpaException e) {
            System.out.println(e.getMessage());
        }
    }
}

class AgeOutOfRangeException extends Exception {
    int age;

    public AgeOutOfRangeException(int age) {
        this.age = age;
    }
    @Override
    public String getMessage(){
        return ("You are older than the requested age (25 years), you are " + age + "!!!");
    }
}

class LowGpaException extends Exception {
    double gpa;
    public LowGpaException(double gpa) {
        this.gpa = gpa;
    }
    @Override
    public String getMessage(){
       return ("Your GPA "+gpa+" is not sufficient to apply for this job (2.5)");
    }
}