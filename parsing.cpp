#include<stdio.h>
#include <math.h>

int number_of_digits(int x);

int main() {
	int number;
	printf("Enter a number to parse:");
	scanf("%d",&number);
	int length=number_of_digits(number);
	//printf("%d\n",length);
	int parsed[length-1]={0};
	int mod;
	int power=0;
	while (1){
		mod=number%10;
		number/=10;
		parsed[length-(power+1)]=mod*(pow(10,power));
		power++;
		if (number<10) {
			mod=number%10;
			parsed[0]=mod*(pow(10,power));
			break;
		}
	}
	for (power=0;power<length;power++) {
		printf("%d",parsed[power]);
		if (power!=(length-1)) {
			printf("+");
		}
	}
	
	return 0;
}

int number_of_digits(int x) {
	int counter=0;
	while (x!=0) {
		x/=10;
		counter++;
	}
	return counter;
}
