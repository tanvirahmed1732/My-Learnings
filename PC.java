
package com.mycompany.practice;

public class PC {
    public static void main(String[] args) {
        T t = new T();
        new Producer(t);
        new Consumer(t);
        System.out.println("OVER");
    }
}
class T{
    int n;
    boolean set = false;
    synchronized int get(){
        while(!set)
            try{
                wait();
            }catch(InterruptedException e){
                System.out.println(e.getMessage());
            }
        System.out.println("Got "+n);
        set = false;
        notify();
        return n;
    }
    synchronized void put(int n){
        while(set)
            try{
                wait();
            }catch(InterruptedException e){
                System.out.println(e.getMessage());
            }
        this.n = n;
        set = true;
        System.out.println("Put " +n);
        notify();
    }
}
class Consumer extends Thread{
    T t;
    Consumer(T t){
        this.t = t;
        start();
    }
    public void run(){
        int i = 0;
        while(i<50){
            t.get();
            i++;
        }
    }
}
class Producer extends Thread{
    T t;
    Producer(T t){
        this.t = t;
        start();
    }
    public void run(){
        int i = 0;
        while(i<50){
            t.put(i++);
        }
    }
}
