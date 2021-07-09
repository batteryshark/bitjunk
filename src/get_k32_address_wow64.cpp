#include <stdio.h>
#include <Windows.h>



int main(int argc, const char* argv[]) {
	if (argc != 2) { return -1; }
	
	HMODULE h_module = LoadLibraryA("Kernel32.dll");
	if (!h_module) { return -1; }
	printf("%p", GetProcAddress(h_module, argv[1]));
	return 0;
}