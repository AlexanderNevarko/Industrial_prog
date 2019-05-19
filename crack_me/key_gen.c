#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int process_login(char* login);
int process_pass(char* pass);
char* generate_password(int log_result);
char* create_letters(int res);
int test(char* login, char* pass);


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        printf("Enter your login\n");
        return 0;
    }
    char* login = argv[1];
    int login_result = process_login(login);

    char* pass = generate_password(login_result);
    printf("Your password: %s\n", pass);
    char* check = test(login, pass) ? "True" : "False";
    printf("Check pass: %s\n", check);
}


int process_login(char* login)
{
    int result = 0xffffffff;
    int temp = 0;
    int N = strlen(login);

    for (int i = 0; i < N; i++)
    {
        result = result ^ login[i];
        for (int j = 7; j >= 0; j--)
        {
            temp = result;
            temp = -(temp & 1);
            result >>= 1;
            temp = temp & 0xedb88320;
            result = result ^ temp;
        }
    }
    printf("Login processed: %d\n", result);
    return result;
}


char* generate_password(int log_result)
{
    printf("entered pass generator\n");
    printf("log:%d\n", log_result);
    log_result = ~log_result;
    printf("log:%d\n", log_result);
    int log_res = log_result & 0xff;
    printf("log:%d\n", log_res);
    int res = log_res;
    
    char* pass = create_letters(res);
    
    printf("fin\n");
    return pass;
}


char* create_letters(int res)
{
    int try = res ^ 0x99;
    if (try >= '!' && try <= '~')
    {
        char* pass = (char*) calloc(1, sizeof(char));
        pass[0] = try;
        return pass; 
    }
    else if (try < '!')
    {
        printf("Interesting case!");
        return NULL;
    }
    else
    {
        
    }
}


int process_pass(char* pass)
{
    int result = 0;
    int N = strlen(pass);
	for (int i = 0; i < N; i++)
	{
		result = result + (pass[i] ^ 0x99);
	}
	
	return result;
}


int test(char* login, char* pass)
{
    printf("test_init\n");
    int log_proc = process_login(login);
    printf("log:%d\n", log_proc);
    int pass_proc = process_pass(pass);
    printf("pass:%d\n", pass_proc);
    log_proc = ~log_proc;
    printf("log:%d\n", log_proc);
    log_proc &= 0xff;
    printf("log:%d\n", log_proc);
    pass_proc &= 0xff;
    printf("pass:%d\n", pass_proc);
    printf("fin\n");
    if (log_proc == pass_proc) return 1;
    else return 0;
}