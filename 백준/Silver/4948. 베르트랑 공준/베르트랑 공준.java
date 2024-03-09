import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
	
	static boolean prime[];
	static int answer[];
	static int answer1=0;
	
	
	
	static int isPrime(int max) {
		
		Arrays.fill(prime, true);
		prime[0]=prime[1]=false;
		int count=0;
		
		for(int i=2;i<=Math.sqrt(max*2);i++){
			if(prime[i])
				for(int j=i*i;j<=max*2+1;j+=i) {
					prime[j]=false;
				}
		}
		
		for(int i=max+1;i<=max*2;i++) {
			if(prime[i]) {
				count++;
			}
		}
		
		return count;
	
		//answer[answer1]=count;
		//answer1++;
		
	}
	
	public static void main(String[] args)throws NumberFormatException, IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num;
		
		while(true) {

			int n = Integer.parseInt(br.readLine());
			if(n==0) {
				break;
			}
			
			prime=new boolean[2*n+2];
			int answer=isPrime(n);
			System.out.println(answer);
				
			}
			
		}
		
		
		
		
	}


