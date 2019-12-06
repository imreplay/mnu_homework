#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char const *argv[]){

  char buf2[10];
  char buf[10];
  printf("It can be overflow : ");
  fflush(stdout);
  fgets(buf, 40,stdin);

  if ( strncmp(buf2, "go", 2) == 0 )
   {
        printf("Good Skill!\n");
        printf("Answer is FLAG{Network_security_is_So_Fun!}\n");
   }

}
