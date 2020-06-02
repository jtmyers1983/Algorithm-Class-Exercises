
char arr[] = { 'C', 'o', 'm', 'p', '\0' }; int i, n = 0;
for (i = 0; i < 5; ++ i) { 
	n = n + (int) arr[i];
	arr[i] += 2; /* Increment the ASCII code by 2 */ 
	System.out.println("%d", arr[i]);
	  }
return 0;
		}
