#include<stdio.h>

void fun1(){
	printf("This is fun 1");
	void fun2(){
		printf("This is fun 2 within fun1");
	} 
	fun2();

}

int main(){
	fun1();
	return 0;
}
