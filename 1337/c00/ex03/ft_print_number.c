#include <unistd.h>

void ft_print_number(void){
	char i;
	i = '1';
	while(i <= '9'){
		write(1, &i, 1);
		i++;
	}
}

int main(){
	ft_print_number();
}
