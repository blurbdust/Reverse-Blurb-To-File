#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>

#define HASH_INDEX 0
char* hash[1024] = {"",""}; 
hash[sizeof(hash) - 1] = '\0';

void process_text_file(FILE *fp){
	char ch;
	char tmp[] = " ";
	int i = 0;
	int max = 2147483647;
	
	rewind(fp);
	
	printf("Now the file in hex: \n");
	while( ( ch = fgetc(fp) ) != EOF ){
      printf("%02X ",ch);
      if( !(++i % 16) ) putc('\n', stdout);
	}
   fclose(fp);
   putc('\n', stdout);
	
}

void displayHexRecord(char *data, int count, int record_length) {
	int	i;
	for (i=0; i < count; i++){
		printf("%02x ", data[i] & 0xff);
	}
	for (; i < record_length; i++){
		printf("	");
	}
	printf(": ");
	for (i=0; i < count; i++) {
		if (isgraph(data[i])){
		putchar(data[i]);
		}
		else{
			putchar('.');
		}	
	}
	putchar('\n');
}

void process_file(FILE *f, long cur_addr, long end, int bytes_per_line) {
	int	record_length, read_count;
	char	*data;
	assert(data = (char*) calloc(sizeof(data[0]), bytes_per_line));
	if (-1 == fseek(f, cur_addr, SEEK_SET)){
		perror("fseek");
	}
	while (1) {
		printf("%05x  ", cur_addr);
		read_count = end - cur_addr;
		if (read_count > bytes_per_line){
			read_count = bytes_per_line;
		}
		record_length = fread(data, sizeof(char), read_count, f);
		
		if (cur_addr == (0)){
			printf("Fired at beginning");
			for (i = 0; i < sizeof(data); i++){
				hash[HASH_INDEX] = data[i];
				HASH_INDEX++;
			}
		}
		else if (cur_addr == (16 * (floor((end / 4.0) / 16.0) ))){
			printf("***Fired quarterway");
			for (i = 0; i < sizeof(data); i++){
				hash[HASH_INDEX] = data[i];
				HASH_INDEX++;
			}
		}
		else if (cur_addr == (16 * (floor((end / 2.0) / 16.0) ))){
			printf("Fired halfway");
			for (i = 0; i < sizeof(data); i++){
				hash[HASH_INDEX] = data[i];
				HASH_INDEX++;
			}
		}
		else if (cur_addr == (16 * (floor((3 * end / 4.0) / 16.0) ))){
			printf("Fired tri-quarterway");
			for (i = 0; i < sizeof(data); i++){
				hash[HASH_INDEX] = data[i];
				HASH_INDEX++;
			}
		}
		else if (cur_addr == (16 * (floor((end / 1.0) / 16.0) ))){
			printf("Fired end");
			for (i = 0; i < sizeof(data); i++){
				hash[HASH_INDEX] = data[i];
				HASH_INDEX++;
			}
		}
		else {
			printf("Catch %d", cur_addr);
		}
		
		displayHexRecord(data, record_length, bytes_per_line);
		if (record_length < bytes_per_line){
			break;
		}
		if (end <= (cur_addr += record_length)){
			break;
		}
	}
	free(data);
}


void process_hash(char* hash){
	//TODO After making the hash first
	
	
	
}


int main (int argc, char **argv){
	clock_t start, end;
	double cpu_time_used;
	start = clock();
	printf("Running main\n");
	int i = 0;
	FILE *fp;
	fp = fopen(argv[1], "rb");
	fseek(fp, 0L, SEEK_END);
	end = ftell(fp);
	printf("End is: %d\n", end);
	rewind(fp);
	
	if (strchr(argv[1], '.') && (fp != NULL)) {
		printf("Found filename\n");
		for (i = 0; i < sizeof(argv[1]); i++){
			hash[HASH_INDEX] = argv[1][i];
		}
		printf("Hash is: %s so far", hash);
		//We are dealing with a file name!
		if (strstr(argv[1], ".txt")){
			process_text_file(fp);
		}
		else {
			process_file(fp, 0 , end, 16);
		}
	}
	else if (i = 0){
		//Dealing with a hash
		printf("In order to reverse my hash, I have to make it first...\n");
	}
	else {
		//I don't know, something bad happened.
		printf("Either no file exists with that name or you messed up big time.\n");
	}
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("It took me %lf seconds to run.", cpu_time_used);
	return 0;
}
