#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(10-i)
    print("Happy New Year!")

def square_integers(int_list):
    stuff = []
    for num in int_list:
        stuff.append(num * num)
    return stuff

def fizzbuzz():
    for i in range(100):
        fizz = (i+1) % 3 == 0
        buzz = (i+1) % 5 == 0
        if fizz and buzz:
            print('FizzBuzz')
        elif fizz:
            print('Fizz')
        elif buzz:
            print('Buzz')
        else:
            print(i+1)

fizzbuzz()
