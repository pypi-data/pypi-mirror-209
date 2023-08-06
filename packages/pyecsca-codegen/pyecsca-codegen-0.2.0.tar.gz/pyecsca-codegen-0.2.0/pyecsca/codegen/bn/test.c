#include "bn.h"
#include <stdio.h>

int main(int argc, char* argv[]) {
    if (argc != 4) {
        return 1;
    }
#if REDUCTION == RED_MONTGOMERY
    printf("Montgomery\n");
#elif REDUCTION == RED_BARRETT
    printf("Barrett\n");
#else
    printf("Base\n");
#endif
    math_init();

    bn_t a; bn_init(&a);
    bn_t b; bn_init(&b);
    bn_t mod; bn_init(&mod);
    bn_t c; bn_init(&c);
    mp_read_radix(&a, argv[1], 10);
    mp_read_radix(&b, argv[2], 10);
    mp_read_radix(&mod, argv[3], 10);

    red_t red;
    bn_red_init(&red);
    bn_red_setup(&mod, &red);

    bn_red_encode(&a, &mod, &red);
    bn_red_encode(&b, &mod, &red);
    printf("aEnc = ");
    mp_fwrite(&a, 10, stdout);
    printf("\n");
    printf("bEnc = ");
    mp_fwrite(&b, 10, stdout);
    printf("\n");

    bn_red_mul(&a, &b, &mod, &red, &c);
    bn_red_add(&a, &c, &mod, &red, &c);
    bn_red_mul(&c, &c, &mod, &red, &c);
    bn_red_div(&c, &b, &mod, &red, &c);
    bn_red_sub(&c, &a, &mod, &red, &c);
    bn_red_neg(&c, &mod, &red, &c);
    bn_red_inv(&c, &mod, &red, &c);
    bn_red_sqr(&c, &mod, &red, &c);

    printf("cEnc = ");
    mp_fwrite(&c, 10, stdout);
    printf("\n");

    bn_red_decode(&a, &mod, &red);
    bn_red_decode(&b, &mod, &red);
    bn_red_decode(&c, &mod, &red);
    printf("a = ");
    mp_fwrite(&a, 10, stdout);
    printf("\n");
    printf("b = ");
    mp_fwrite(&b, 10, stdout);
    printf("\n");
    printf("c = ");
    mp_fwrite(&c, 10, stdout);
    printf("\n");
    bn_clear_multi(&a, &b, &c, &mod, NULL);
    bn_red_clear(&red);
    return 0;
}