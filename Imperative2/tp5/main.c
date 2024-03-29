#include "func.h"
int main(int argc, char const *argv[])
{
    int i,n = 100;
    int tps_init, tps_crt, dtps;

    printf("Temps pour %u avec %10s :\t", n, "fib_iter");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        fib_iter(i%44);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );

    printf("Temps pour %u avec %10s :\t", n, "fib_rec");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        //fib_rec(i%44);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );

    printf("Temps pour %u avec %10s :\t", n, "fib_rec_ter");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        fib_rec_ter(i%44,1,1);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );

    printf("Temps pour %u avec %10s :\t", n, "fib_binet");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        fib_binet(44);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );


    printf("Temps pour %u avec %10s :\t", n, "tri_rec");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        //printf("%d %d\n",i,tri_rec(i,i/2));
        //tri_rec(i%30,i%30/2);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );

    printf("Temps pour %u avec %10s :\t", n, "tri_iter");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        tri_iter(i%30,i%30/2);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );

    printf("Temps pour %u avec %10s :\t", n, "tri_combi");
    tps_init = (int) clock();
    for (i = 0; i < n; i++) {
        tri_combi(i%30,i%30/2);
    }
    tps_crt = (int) clock();
    dtps = tps_crt - tps_init;
    printf(" \t%d\n", dtps );




















}
