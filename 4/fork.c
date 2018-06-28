#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
  // pipe generation
  int fds[2];
  int pipe_id = pipe(fds);
  char buf[strlen("Hi, son.\n")];


  int pid = fork();
  if (pid == 0) {
    printf("Enter child.\n");
    // child: reads from pipe and answers
    int r = read(fds[0], buf, strlen("Hi, son.\n"));
    printf("Child read. SON REC: %s\n", buf);

  } else if (pid < 0) {
    // error case
    printf("Forking error.\n");

  } else { // father code
    printf("Enter father.\n");
    write(fds[1], "Hi, son.\n", strlen("Hi, son.\n"));
    printf("Father wrote.\n");
  }
}
