
package com.mycompany.practice;

public class Practice {
    public static void main(String[] args) {
        Class2 obj1 = new Class2("String", 3);
        obj1.show();
        obj1.showstring();
        
    }
}
class Class1 {
    String s;
    public void show(){
        System.out.println("Class1");
    }
    public void showstring(){
        System.out.println(s);
    }
}
class Class2 extends Class1{
    int count = 0;
    Class2(String s, int count){
        super.s = s;
        this.count = count;
    }
    @Override
    public void show(){
        super.show();
    }
    @Override
    public void showstring(){
        super.showstring();
        System.out.println(super.s);
        System.out.println(count);
    }
}
