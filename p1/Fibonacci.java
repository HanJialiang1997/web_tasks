import java.math.BigDecimal;

public class Fibonacci {
	public static BigDecimal fib(int n){
		if(n==1)
			return new BigDecimal(1);
		if(n==2)
			return new BigDecimal(1);
		else{
		    BigDecimal num1=new BigDecimal(1);		
		    BigDecimal num2=new BigDecimal(1);		
			int tag=2;
			while(tag<n){
				BigDecimal temp=num2;
				num2=num2.add(num1);
				num1=temp;
				tag++;
			}
			return num2;
		}
	}
	
	public static void printFib(int n){
		for(int i=1;i<=n;i++)
			System.out.println(fib(i)+"    "+i);
	}
	
	public static void main(String[] args) {
		printFib(100);
	}
}
