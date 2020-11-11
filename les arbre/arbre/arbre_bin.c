#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>
#include <math.h>

struct cell{
	int val;
	struct cell * Fg;
	struct cell * Fd;
};
typedef struct cell Arbre;
struct abr{
	int val;
 	int *v;
	float *w;
};	
typedef struct abr abr_t;
struct vect {
	int n ;
	struct vect * vec ;
}
typedef struct vect vect_t ; 

void Aj_In_Arbre(Arbre **arb,int x){
	if(*arb){
		if(x < (*arb)->val)
			return Aj_In_Arbre( &((*arb)->Fg),x);
		return Aj_In_Arbre(& ((*arb)->Fd),x);
	}

	*arb = malloc (sizeof **arb);
	assert(*arb);
	(*arb)-> Fg = (*arb)->Fd = NULL;
	(*arb)->val=x;
}
void print_arbre(Arbre *arb){
	if(arb){
		print_arbre(arb->Fg);
		printf("%d, ",arb->val);
		print_arbre(arb->Fd);
	}
}
void arb_free(Arbre **arb)
{
	if( (*arb)->Fg){
		arb_free(&((*arb)->Fg));
	}
	if( (*arb)->Fd){
		arb_free(&((*arb)->Fd));
	}

	free(*arb);
	
}	
int appartient(Arbre *arb,int x){
    if(!arb)
        return 0 ;
    if(arb->val == x)
        return 1 ;
    return appartient(arb->Fg,x)||appartient(arb->Fd,x);

}
int profondeur(Arbre *arb) {
  int prsg, prsd;
  if (! arb)
	return 0;
  prsg = profondeur (arb->Fg);
  prsd = profondeur (arb->Fd);
  return 1 + (prsg < prsd ? prsd : prsg);
}
int som(Arbre * arb){
    int tmp ; 
    if (! arb)
        return 0;
    tmp = arb->val;
    tmp += som(arb->Fd);
    tmp += som(arb->Fg);
    return tmp ;
}   
int arb_add_value_iter(Arbre **arb,int x){
	while(*arb)
	{
		if(x < (*arb)->val)
			arb = &((*arb)->Fg);
		else
			arb = &((*arb)->Fd);
	}
	*arb = malloc (sizeof **arb);
	assert(*arb);
	(*arb)-> Fg = (*arb)->Fd = NULL;
	(*arb)->val=x;	
}

int nb_noeuds(Arbre *arb){
    if(! arb)
        return 0;
    return( 1+ nb_noeuds(arb->Fd)+nb_noeuds(arb->Fg));
}

Arbre *PtrToVect(Arbre *arb){
	Arbre *new;
	int prof,nb;
	prof = profondeur(arb);
	nb = (2<<(prof -1 ))+1;
	new->val = nb;
	new n = calloc((size_t)nb,sizeof(int));
	assert(new n);
	new = new ptr(n,new,0);
	return new ;
}


int main(int argc, char const *argv[])
{
	Arbre *ab = NULL;
	print_arbre(ab);
	int i;
    int Size = 10 ;
	for (i = 0; i < Size; ++i)
	{	
        Aj_In_Arbre(&ab,i);
		
	}
	print_arbre(ab);
    printf("\n");
    printf("%d \n",appartient(ab,10));
    printf("%d\n",profondeur(ab));
    printf("%d\n",som(ab));
    printf("%d\n",nb_noeuds(ab));
	return 0;
}